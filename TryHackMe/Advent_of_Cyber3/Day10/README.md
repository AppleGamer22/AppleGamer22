# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 10
### References
* Wylie, P. (2021). TryHackMe! Advent of Cyber 3 - DAY10 | Offensive is The Best Defense [YouTube Video]. In YouTube. https://youtu.be/yHjD_07r5xs

## Help McSkidy and run `nmap -sT <MACHINE_IP>`. How many ports are open between 1 and 100?
```bash
$ nmap -sT <MACHINE_IP>
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

**Answer**: `2`
## What is the smallest port number that is open?
**Answer**: `22`
## What is the service related to the highest port number you found in the first question?
**Answer**: `HTTP`
## Now run `nmap -sS <MACHINE_IP>`. Did you get the same results (`Y`/`N`)?
```bash
$ sudo nmap -sS <MACHINE_IP>
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

**Answer**: `Y`
## 
If you want Nmap to detect the version info of the services installed, you can use `nmap -sV 10.10.232.60`. What is the version number of the web server?
```bash
$ nmap -sV 10.10.232.60
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.49
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

**Answer**: `Apache httpd 2.4.49`
## By checking the [vulnerabilities related to the installed web server](https://httpd.apache.org/security/vulnerabilities_24.html), you learn that there is a critical vulnerability that allows path traversal and remote code execution. Now you can tell McSkidy that Grinch Enterprises used this vulnerability. What is the CVE number of the vulnerability that was solved in version `2.4.51`?
* According to [Apache Software Foundation](https://httpd.apache.org/security/vulnerabilities_24.html):

> ### Fixed in Apache HTTP Server 2.4.51
> #### critical: Path Traversal and Remote Code Execution in Apache HTTP Server 2.4.49 and 2.4.50 (incomplete fix of CVE-2021-41773) ([CVE-2021-42013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-42013))


**Answer**: `CVE-2021-42013`
## McSkidy asks you to check if there is some service listening on an uncommon port, that is outside the 1000 common ports that Nmap scans by default. She explains that adding `-p1-65535` or `-p-` will scan all 65,535 TCP ports instead of only scanning the 1000 most common ports. What is the port number that appeared in the results now?
```bash
$ nmap -sT -p- 10.10.232.60
PORT      STATE    SERVICE
22/tcp    open     ssh
80/tcp    open     http
3636/tcp  filtered servistaitsm
20212/tcp open     unknown
```
**Answer**: `20212`
## What is the name of the program listening on the newly discovered port?
```bash 
$ nmap -sV -p 20212 10.10.232.60
PORT      STATE SERVICE VERSION
20212/tcp open  telnet  Linux telnetd
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

**Answer**: `telnetd`