# TryHackMe [Linux Fundamentals Part 1](https://www.tryhackme.com/room/linuxfundamentalspart1)
### References
* Try Hack Me. (2021). Learn the Linux Fundamentals - Part 1 [YouTube Video]. In YouTube. https://youtu.be/kPylihJRG70
* Wikipedia Contributors. (2021, May 30). Linux kernel. Wikipedia; Wikimedia Foundation. https://en.wikipedia.org/wiki/Linux_kernel
## A Bit of Background on Linux
### What year was the first release of a Linux operating system?
* According to [Wikipedia](https://en.wikipedia.org/wiki/Linux_kernel):
> It was conceived and created in 1991 by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)<sup>[[9]](https://en.wikipedia.org/wiki/Linux_kernel#cite_note-qqGYY-9)</sup> for his [i386](https://en.wikipedia.org/wiki/Intel_80386)-based PC, and it was soon adopted as the kernel for the [GNU operating system](https://en.wikipedia.org/wiki/GNU),<sup>[[10]](https://en.wikipedia.org/wiki/Linux_kernel#cite_note-2Ifyf-10)</sup> which was created as a [free](https://en.wikipedia.org/wiki/Free_software) replacement for [UNIX](https://en.wikipedia.org/wiki/UNIX).<sup>[[11]](https://en.wikipedia.org/wiki/Linux_kernel#cite_note-832_F.Supp._7902-11)</sup>

**Answer**: `1991`
## Running Your First few Commands
### If we wanted to output the text **"TryHackMe"**, what would our command be?
**Answer**: `echo TryHackMe`
### What is the username of who you're logged in as on your deployed Linux machine?
```
tryhackme@linux1:~$ whoami
tryhackme
```
**Answer**: `tryhackme`
## Interacting With the Filesystem!
### On the Linux machine that you deploy, how many folders are there?
```
tryhackme@linux1:~$ ls
access.log  folder1  folder2  folder3  folder4
```
**Answer**: `4`
### Which directory contains a file? 
```
tryhackme@linux1:~$ ls folder4
note.txt
```
**Answer**: `folder4`
### What is the contents of this file?
```
tryhackme@linux1:~$ cat folder4/note.txt
Hello World!
```
**Answer**: `Hello World!`
### Use the `cd` command to navigate to this file and find out the new current working directory. What is the path?
```
tryhackme@linux1:~$ cd folder4
tryhackme@linux1:~/folder4$ pwd
/home/tryhackme/folder4
```
**Answer**: `/home/tryhackme/folder4`
## Searching for Files
### Use grep on `access.log` to find the flag that has a prefix of `THM`. What is the flag?
```
tryhackme@linux1:~$ grep "THM*" access.log 
13.127.130.212 - - [04/May/2021:08:35:26 +0000] "GET THM{ACCESS} lang=en HTTP/1.1" 404 360 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77
.0.3865.120 Safari/537.36"
```
**Flag**: `THM{ACCESS}`
## An Introduction to Shell Operators
### If we wanted to run a command in the background, what operator would we want to use?
**Answer**: `&`
### If I wanted to replace the contents of a file named "passwords" with the word "password123", what would my command be?
**Answer**: `echo password123 > passwords`
### Now if I wanted to add "tryhackme" to this file named "passwords" but also keep "passwords123", what would my command be?
**Answer**: `echo tryhackme >> passwords`


