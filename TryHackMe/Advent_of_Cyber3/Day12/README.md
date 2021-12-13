# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 12
### References
* Cyber Insecurity. (2021). Advent of Cyber 3 (2021) - Day 12 - Sharing Without Caring - TryHackMe [YouTube Video]. In YouTube. https://youtu.be/BQqjJwFLLII

## Scan the target server with the IP `<MACHINE_IP>`. Remember that MS Windows hosts block pings by default, so we need to add `-Pn`. How many TCP ports are open?
```bash
$ nmap -Pn <MACHINE_IP>
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-12 23:35 EST
PORT     STATE SERVICE
22/tcp   open  ssh
111/tcp  open  rpcbind
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
2049/tcp open  nfs
3389/tcp open  ms-wbt-server
```

**Answer**: `7`
## Which port is detected by `nmap` as NFS or using the `mountd` service?
```bash
$ nmap -sV -Pn <MACHINE_IP>
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH for_Windows_7.7 (protocol 2.0)
111/tcp  open  rpcbind       2-4 (RPC #100000)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
2049/tcp open  mountd        1-3 (RPC #100005)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

**Answer**: `2049`
## How many network shares did you find?
```bash
$ showmount -e <MACHINE_IP>
/share        (everyone)
/admin-files  (everyone)
/my-notes     (noone)
/confidential (everyone)
```

**Answer**: `4`
## How many network shares show `everyone`?
**Answer**: `3`
## What is the title of file `2680-0.txt` from the network share `share`?
```bash
$ mkdir /tmp/share
$ sudo mount <MACHINE_IP>:/share /tmp/share
$ ls /tmp/share
132-0.txt  2680-0.txt
$ head /tmp/share/2680-0.txt
Title: Meditations

Author: Marcus Aurelius

Translator: Meric Casaubon

Release Date: June, 2001 [eBook #2680]
[Most recently updated: March 8, 2021]

Language: English
```

**Answer**: `Meditations`
## It seems that Grinch Enterprises has forgotten their SSH keys on our system. One of the shares contains a private key used for SSH authentication (`id_rsa`). What is the name of the share?
```bash
$ mkdir /tmp/confidential
$ sudo mount <MACHINE_IP>:/confidential /tmp/confidential
$ tree /tmp/confidential/
/tmp/confidential/
└── ssh
    ├── id_rsa
    └── id_rsa.pub
```

**Answer**: `confidential`
## We can calculate the MD5 sum of a file using `md5sum <FILENAME>`. What is the MD5 sum of `id_rsa`?
```bash
$ md5sum /tmp/confidential/ssh/id_rsa
3e2d315a38f377f304f5598dc2f044de  /tmp/confidential/ssh/id_rsa
```

**Answer**: `3e2d315a38f377f304f5598dc2f044de`