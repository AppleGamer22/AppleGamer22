# TryHackMe [CC: Pen Testing](https://tryhackme.com/room/ccpentesting) Network Utilities
### References
* Lyon, G. (2021). `nmap` Reference Guide. nmap.org. https://nmap.org/book/man.html
* Offensive Security. (2019). `meterpreter` Basic Commands. Offensive Security. https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/
* Reeves, OJ. (2021). `OJ/gobuster/README.md`. GitHub. https://github.com/OJ/gobuster/blob/master/README.md
* Sullo, C. (2021). `sullo/nikto/README.md`. GitHub. https://github.com/sullo/nikto/blob/master/README.md
## `nmap`
### What does nmap stand for?
**Answer**: `network mapper`
### How do you specify which port(s) to scan?
**Answer**: `-p`
### How do you do a "ping scan"(just tests if the host(s) is up)?
**Answer**: `-sn`
### What is the flag for a UDP scan? 
**Answer**: `-sU`
### How do you run default scripts?
**Answer**: `-sC`
### How do you enable "aggressive mode"(Enables OS detection, version detection, script scanning, and traceroute)?
**Answer**: `-A`
### What flag enables OS detection?
**Answer**: `-O`
### How do you get the versions of services running on the target machine?
**Answer**: `-sV`
### How many ports are open on the machine?
```bash
$ nmap -sV -sC <MACHINE_IP>
Starting Nmap 7.91 ( https://nmap.org ) at 2021-04-17 12:50 AEST
Nmap scan report for <MACHINE_IP>
Host is up (0.28s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.29 seconds
```
**Answer**: `1`
### What service is running on the machine?
**Answer**: `Apache`
### What is the version of the service?
**Answer**: `2.4.18`
### What is the output of the http-title script(included in default scripts)
**Answer**: `Apache2 Ubuntu Default Page: It works`
## Netcat (`nc`)
### How do you listen for connections?
**Answer**: `-l`
### How do you enable verbose mode(allows you to see who connected to you)?
**Answer**: `-V`
### How do you specify a port to listen on?
**Answer**: `-p`
### How do you specify which program to execute after you connect to a host (one of the most infamous)?
**Answer**: `-e`
### How do you connect to udp ports
**Answer**: `-u`
## `gobuster`
### How do you specify directory/file brute forcing mode?
**Answer**: `dir`
### How do you specify dns bruteforcing mode?
**Answer**: `dns`
### What flag sets extensions to be used?
**Answer**: `-x`
### What flag sets a wordlist to be used?
**Answer**: `-w`
### How do you set the username for basic authentication(If the directory requires a username/password)?
**Answer**: `-U`
### How do you set the password for basic authentication?
**Answer**: `-P`
### How do you set which status codes gobuster will interpret as valid?
**Answer**: `-s`
### How do you skip ssl certificate verification?
**Answer**: `-k`
### How do you specify a `User-Agent`?
**Answer**: `-a`
### How do you specify a HTTP header?
**Answer**: `-H`
### What flag sets the URL to bruteforce?
**Answer**: `-u`
### What is the name of the hidden directory?
```bash
$ gobuster dir -u http://10.10.113.116 -w $(pwd)/directory-list-2.3-small.txt
/secret               (Status: 301) [Size: 315] [--> http://<MACHINE_IP>/secret/]
```
**Answer**: `secret`
### What is the name of the hidden file with the extension `xxa`
```bash
$ gobuster dir -u http://10.10.113.116 -w $(pwd)/directory-list-2.3-small.txt -x xxa
/password.xxa         (Status: 200) [Size: 12]
```
**Answer**: `password`
## `nikto`
### How do you specify which host to use?
**Answer**: `-h`
### What flag disables SSL?
**Answer**: `-nossl`
### How do you force SSL?
**Answer**: `-ssl`
### How do you specify authentication (username + pass)?
**Answer**: `-id`
### How do you select which plugin to use?
**Answer**: `-Plugins`
### Which plugin checks if you can enumerate apache users?
```bash
$ nikto -list-plugins
Plugin: apacheusers
 Apache Users - Checks whether we can enumerate usernames directly from the web server
 Written by Javier Fernandez-Sanguinoi Pena, Copyright (C) 2008 CIRT Inc.
 Options:
  home: Look for ~user to enumerate
  dictionary: Filename for a dictionary file of users
  cgiwrap: User cgi-bin/cgiwrap to enumerate
  enumerate: Flag to indicate whether to attempt to enumerate users
  size: Maximum size of username if bruteforcing
```
**Answer**: `apacheusers`
### How do you update the plugin list?
**Answer**: `-update`
### How do you list all possible plugins to use?
**Answer**: `-list-plugins`