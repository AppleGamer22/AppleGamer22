# TryHackMe [Linux Fundamentals Part 3](https://www.tryhackme.com/room/linuxfundamentalspart3)
### References
* Try Hack Me. (2021). Learn the Linux Fundamentals - Part 3 [YouTube Video]. In YouTube. https://youtu.be/bwgaZCb2ft8
## Terminal Text Editors
### Edit `task3` located in `tryhackme`'s home directory using Nano. What is the flag?
```
$ ssh tryhackme@10.10.42.183
tryhackme@10.10.42.183's password: tryhackme
tryhackme@linux3:~$ $ cat task3 
THM{TEXT_EDITORS}
```
**Flag**: `THM{TEXT_EDITORS}`
## General/Useful Utilities
### Use Python's `http.server` module to start a web server in the home directory of the `tryhackme` user on the deployed instance and Download the `.flag.txt` file.
```
tryhackme@linux3:~$ ls -la
total 44
drwxr-xr-x 5 tryhackme tryhackme 4096 May 30 07:26 .
drwxr-xr-x 4 root      root      4096 May  4 18:14 ..
-rw------- 1 tryhackme tryhackme    0 May  5 14:20 .bash_history
-rw-r--r-- 1 tryhackme tryhackme  220 May  4 18:14 .bash_logout
-rw-r--r-- 1 tryhackme tryhackme 3771 May  4 18:14 .bashrc
drwx------ 2 tryhackme tryhackme 4096 May 30 07:26 .cache
drwx------ 3 tryhackme tryhackme 4096 May  5 11:46 .config
-rw-r--r-- 1 root      root        20 May  5 12:05 .flag.txt
drwxrwxr-x 3 tryhackme tryhackme 4096 May  4 18:20 .local
-rw-r--r-- 1 tryhackme tryhackme  807 May  4 18:14 .profile
-rw-rw-r-- 1 tryhackme tryhackme   66 May  5 11:28 .selected_editor
-rw-r--r-- 1 tryhackme tryhackme   18 May  5 13:11 task3
tryhackme@linux3:~$ cat .flag.txt 
THM{WGET_WEBSERVER}
```
**Flag**: `THM{WGET_WEBSERVER}`
## Processes 101
### If we were to launch a process where the previous ID was `300`, what would the ID of this new process be?
**Answer**: `301`
### If we wanted to **cleanly** kill a process, what signal would we send it?
**Answer**: `SIGTERM`
### Locate the process that is running on the deployed instance (10.10.42.183). What flag is given?
```
tryhackme@linux3:~$ ps aux | grep 'THM'
root         667  0.0  0.1   2356   592 ?        S    07:24   0:00 THM{PROCESSES}
```
**Flag**: `THM{PROCESSES}`
### What command would we use to stop the service `myservice`?
**Answer**: `systemctl stop myservice`
### What command would we use to start the same service on the boot-up of the system?
**Answer**: `systemctl enable myservice`
### What command would we use to bring a previously backgrounded process back to the foreground?
**Answer**: `fg`
## Maintaining Your System: Automation
### How frequently will the crontab on the deployed instance run?
```
tryhackme@linux3:~$ crontab -l
@reboot /var/opt/processes.sh
```
**Answer**: `@reboot`
## Maintaining Your System: Logs
### What is the IP address of the user who visited the site?
```
tryhackme@linux3:~$ ls -l /var/log/apache2/
total 12
-rw-r----- 1 root adm    0 May 30 07:24 access.log
-rwxrwxrwx 1 root adm  209 May  4 18:19 access.log.1
-rw-r----- 1 root adm  277 May 30 07:24 error.log
-rwxrwxrwx 1 root adm 2001 May  5 14:21 error.log.1
-rw-r----- 1 root adm    0 May  4 18:13 other_vhosts_access.log
tryhackme@linux3:~$ cat /var/log/apache2/access.log.1
10.9.232.111 - - [04/May/2021:18:18:16 +0000] "GET /catsanddogs.jpg HTTP/1.1" 200 51395 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
```
**Answer**: `10.9.232.111`
### What file did they access?
**Answer**: `catsanddogs.jpg`