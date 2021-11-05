# TryHackMe [`nmap` Live Host Discovery](https://tryhackme.com/room/nmap01)
## Enumerating Targets
### What is the first IP address `nmap` would scan if you provided `10.10.12.13/29` as your target?
```bash
$ nmap -sL -n 10.10.12.13/29
Starting Nmap 7.92 ( https://nmap.org ) at 2021-11-05 05:49 EDT
Nmap scan report for 10.10.12.8
Nmap scan report for 10.10.12.9
Nmap scan report for 10.10.12.10
Nmap scan report for 10.10.12.11
Nmap scan report for 10.10.12.12
Nmap scan report for 10.10.12.13
Nmap scan report for 10.10.12.14
Nmap scan report for 10.10.12.15
Nmap done: 8 IP addresses (0 hosts up) scanned in 0.00 seconds
```

**Answer**: `10.10.12.8`
### How many IP addresses will `nmap` scan if you provide the following range `10.10.0-255.101-125`?
* Disregarding first and last line:
```bash
$ echo "$(nmap -sL -n 10.10.0-255.101-125 | wc -l) - 2" | bc
6400
```

**Answer**: `6400`
## `nmap` Host Discovery Using ICMP
### What is the option required to tell `nmap` to use ICMP Timestamp to discover live hosts?
**Answer**: `-PP`
### What is the option required to tell `nmap` to use ICMP Address Mask to discover live hosts?
**Answer**: `-PM`
### What is the option required to tell `n	map` to use ICMP Echo to discover life hosts?
**Answer**: `-PE`
## `nmap` Host Discovery Using TCP and UDP
### Which TCP ping scan does not require a privileged account?
**Answer**: `TCP SYN Ping`
### Which TCP ping scan requires a privileged account?
**Answer**: `TCP ACK Ping`
### What option do you need to add to `nmap` to run a TCP SYN ping scan on the telnet port?
**Answer**: `-PS23`
