# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 2
## What is the path of the hidden page?
```bash
$ gobuster dir -u http://10.10.192.75:3000 -w $(pwd)/directory-list-2.3-medium.txt
/home                 (Status: 302) [Size: 28] [--> /login]
/login                (Status: 200) [Size: 1713]
/admin                (Status: 302) [Size: 27] [--> /home]
/Home                 (Status: 302) [Size: 28] [--> /login]
/assets               (Status: 301) [Size: 179] [--> /assets/]
/css                  (Status: 301) [Size: 173] [--> /css/]
/Login                (Status: 200) [Size: 1713]
/js                   (Status: 301) [Size: 171] [--> /js/]
/logout               (Status: 302) [Size: 28] [--> /login]
/sysadmin             (Status: 200) [Size: 1733]
```

**Answer**: `/sysadmin`
## What is the password you found?
1. `view-source:http://10.10.222.52:3000/sysadmin`:
```html
<!--
Admin portal created by arctic digital design - check out our github repo
-->
```
2. `https://github.com/ashu-savani/arctic-digital-design`:
> ### Arctic Digital Design
> arctic digital design used for advent of cyber
>
> Previous versions of this software have been shipped out. The credentials to log in are:
>
> * username: admin
> * password: defaultpass
>
> **the login portal accepts usernames instead of emails**

**Answer**: `defaultpass`
## What do you have to take to the 'partay'?
> ### Prep for Christmas
>  Hey all - Please don't forget to BYOE(Bring Your Own Eggnog) for the partay!!

**Answer**: `Eggnog`