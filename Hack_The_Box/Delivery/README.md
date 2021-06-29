# Hack The Box [Delivery](https://app.hackthebox.eu/machines/Delivery)
### References
* https://drt.sh/posts/htb-delivery/

```bash
$ sudo nmap -sS -sV -sC -p- 10.10.10.222
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-27 19:57 AEST
Nmap scan report for 10.10.10.222
Host is up (0.030s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 9c:40:fa:85:9b:01:ac:ac:0e:bc:0c:19:51:8a:ee:27 (RSA)
|   256 5a:0c:c0:3b:9b:76:55:2e:6e:c4:f4:b9:5d:76:17:09 (ECDSA)
|_  256 b7:9d:f7:48:9d:a2:f2:76:30:fd:42:d3:35:3a:80:8c (ED25519)
80/tcp   open  http    nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: Welcome
8065/tcp open  unknown
```