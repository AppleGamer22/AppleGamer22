# TryHackMe [Linux Fundamentals Part 2](https://www.tryhackme.com/room/linuxfundamentalspart2)
### References
* Try Hack Me. (2021). Learn the Linux Fundamentals - Part 2 [YouTube Video]. In YouTube. https://youtu.be/7Zt2Mp2IeBI
## Accessing Your Linux Machine Using SSH (Deploy)
```
$ ssh tryhackme@10.10.60.59
tryhackme@10.10.60.59's password: tryhackme
tryhackme@linux2:~$
```
## Introduction to Flags and Switches
### What directional arrow key would we use to navigate down the manual page?
**Answer**: `down`
### What flag would we use to display the output in a "human-readable" way?
```
-h, --human-readable
              with -l and -s, print sizes like 1K 234M 2G etc.
```
**Answer**: `-h`
## Filesystem Interaction Continued
### How would you create the file named `newnote`?
**Answer**: `touch newnote`
### On the deployable machine, what is the file type of `unknown1` in `tryhackme`'s home directory?
```
tryhackme@linux2:~$ file unknown1 
unknown1: ASCII text
```
**Answer**: `ASCII text`
### How would we move the file `myfile` to the directory `myfolder`?
**Answer**: `mv myfile myfolder`
### What are the contents of this file?
```
tryhackme@linux2:~$ cat myfile 
THM{FILESYSTEM}
```
**Flag**: `THM{FILESYSTEM}`
## Permissions 101
### On the deployable machine, who is the owner of `important`?
```
tryhackme@linux2:~$ ls -l important 
-rw-r--r-- 1 user2 user2 14 May  5 10:30 important
```
**Answer**: `user2`
### What would the command be to switch to the user `user2`?
**Answer**: `su user2`
### Output the contents of `important`, what is the flag?
```
tryhackme@linux2:~$ su user2
Password: user2
user2@linux2:/home/tryhackme$ cat important 
THM{SU_USER2}
```
**Flag**: `THM{SU_USER2}`
## Common Directories
### What is the directory path that would we expect logs to be stored in?
**Answer**: `/var/logs`
### What root directory is similar to how RAM on a computer works?
**Answer**: `/tmp`
### Name the home directory of the `root` user 
**Answer**: `/root`