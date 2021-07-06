# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 4
### References
* MuirlandOracle. (2020, January 6). MuirlandOracle. MuirlandOracle’s Blog. https://muirlandoracle.co.uk/2020/01/06/tryhackme-christmas-2019-challenge-write-up/
## How many visible files are there in the home directory(excluding `./` and `../`)?
```bash
[mcsysadmin@ip-10-10-241-85 ~]$ ls -l
total 116
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file1
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file2
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file3
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file4
-rw-rw-r-- 1 mcsysadmin mcsysadmin     8 Dec  4  2019 file5
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file6
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file7
-rw-rw-r-- 1 mcsysadmin mcsysadmin 13545 Dec  4  2019 file8
```
**Answer**: `8`
## What is the content of `file5`?
```bash
[mcsysadmin@ip-10-10-241-85 ~]$ cat file5
recipes
```
**Answer**: `recipes`
## Which file contains the string `password`?
```bash
[mcsysadmin@ip-10-10-241-85 ~]$ grep -l -e "password" -f *
file6
```
**Answer**: `file6`
## What is the IP address in a file in the home folder?
```bash
[mcsysadmin@ip-10-10-241-85 ~]$ cat * | grep -Eo "([0-9]{1,3}[\.]){3}[0-9]{1,3}"
10.0.0.05
```
**Answer**: `10.0.0.05`
## How many users can log into the machine?
```bash
[mcsysadmin@ip-10-10-241-85 ~]$ cat /etc/passwd | grep "bash" | wc -l
3
```
**Answer**: `3`
## What is the SHA1 hash of `file8`?
```bash
[mcsysadmin@ip-10-10-241-85 ~]$ sha1sum file8
fa67ee594358d83becdd2cb6c466b25320fd2835  file8
```
## What is `mcsysadmin`’s password hash?
```bash
[mcsysadmin@ip-10-10-241-85 ~]$ locate shadow | grep bak
/var/shadow.bak
[mcsysadmin@ip-10-10-241-85 ~]$ cat /var/shadow.bak | grep "mcsysadmin"
mcsysadmin:$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/:18234:0:99999:7:::
```
**Answer**: `$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/`