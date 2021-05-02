# TryHackMe [Wreath](https://www.tryhackme.com/room/wreath) Task 5
### References
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 5: Webserver - Enumeration [YouTube Video]. In YouTube. https://youtu.be/3ddDBa6tAq0
## How many of the first 15000 ports are open on the target?
* Use `nmap` to check for the first 15000 ports
  * Port 22 open for SSH
  * Port 80 is open for HTTP
  * Port 443 is open for HTTPS
  * Port 10000 is open forsnet-sensor-mgmt
```
$ nmap -p-15000 -vv 10.200.100.200
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-22 16:12 AEST
Initiating Ping Scan at 16:12
Scanning 10.200.100.200 [2 ports]
Completed Ping Scan at 16:12, 0.28s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 16:12
Completed Parallel DNS resolution of 1 host. at 16:12, 0.03s elapsed
Initiating Connect Scan at 16:12
Scanning 10.200.100.200 [15000 ports]
Discovered open port 22/tcp on 10.200.100.200
Discovered open port 443/tcp on 10.200.100.200
Discovered open port 80/tcp on 10.200.100.200
Connect Scan Timing: About 2.43% done; ETC: 16:33 (0:20:46 remaining)
Connect Scan Timing: About 5.39% done; ETC: 16:31 (0:17:51 remaining)
Connect Scan Timing: About 8.46% done; ETC: 16:30 (0:16:25 remaining)
Connect Scan Timing: About 11.80% done; ETC: 16:29 (0:15:04 remaining)
Connect Scan Timing: About 15.50% done; ETC: 16:28 (0:13:43 remaining)
Connect Scan Timing: About 19.43% done; ETC: 16:28 (0:12:31 remaining)
Connect Scan Timing: About 23.69% done; ETC: 16:27 (0:11:20 remaining)
Connect Scan Timing: About 28.90% done; ETC: 16:26 (0:09:53 remaining)
Connect Scan Timing: About 33.62% done; ETC: 16:26 (0:08:55 remaining)
Connect Scan Timing: About 38.57% done; ETC: 16:25 (0:07:59 remaining)
Connect Scan Timing: About 44.15% done; ETC: 16:25 (0:06:59 remaining)
Discovered open port 10000/tcp on 10.200.100.200
Connect Scan Timing: About 50.56% done; ETC: 16:24 (0:05:53 remaining)
Connect Scan Timing: About 56.05% done; ETC: 16:24 (0:05:07 remaining)
Connect Scan Timing: About 61.79% done; ETC: 16:24 (0:04:20 remaining)
Connect Scan Timing: About 68.33% done; ETC: 16:23 (0:03:29 remaining)
Connect Scan Timing: About 74.42% done; ETC: 16:23 (0:02:45 remaining)
Connect Scan Timing: About 80.76% done; ETC: 16:23 (0:02:02 remaining)
Connect Scan Timing: About 87.97% done; ETC: 16:22 (0:01:14 remaining)
Completed Connect Scan at 16:22, 600.70s elapsed (15000 total ports)
Nmap scan report for 10.200.100.200
Host is up, received syn-ack (0.81s latency).
Scanned at 2021-04-22 16:12:40 AEST for 601s
Not shown: 14995 filtered ports
Reason: 14394 no-responses and 601 host-unreaches
PORT      STATE  SERVICE          REASON
22/tcp    open   ssh              syn-ack
80/tcp    open   http             syn-ack
443/tcp   open   https            syn-ack
9090/tcp  closed zeus-admin       conn-refused
10000/tcp open   snet-sensor-mgmt syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 601.04 seconds
```
**Answer**: `4`
## What OS does `nmap` think is running?
```
$ nmap -p 22,80,443,10000 -sV 10.200.100.200
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-22 16:32 AEST
Nmap scan report for 10.200.100.200
Host is up (0.28s latency).

PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.0 (protocol 2.0)
80/tcp    open  http     Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
443/tcp   open  ssl/http Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
10000/tcp open  http     MiniServ 1.890 (Webmin httpd)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.89 seconds
```
**Answer**: `centOS`
## Open the IP in your browser -- what site does the server try to redirect you to?
**Answer**: `https://thomaswreath.thm/`
## What is Thomas' mobile phone number?
1. From `https://thomaswreath.thm/`:
> ### Contact
> #### Address
> 21 Highland Court,
> Easingwold,
> East Riding,
> Yorkshire,
> England,
> YO61 3QL
> 
> #### Phone Number
> 01347 822945
> 
> #### Mobile Number
> +447821548812
> 
> #### Email
> me@thomaswreath.thm

**Answer**: `+447821548812`
## What server version does `nmap` detect as running here?
**Answer**: `MiniServ 1.890 (Webmin httpd)`
## What is the CVE number for this exploit?
* According to [Exploit Database](https://www.exploit-db.com/exploits/47230), the CVE number is `CVE-2019-15107`.

**Answer**: `CVE-2019-15107`

