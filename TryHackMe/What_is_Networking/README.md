# TryHackMe [What is Networking?](https://tryhackme.com/room/whatisnetworking)
## What is Networking?
### What is the key term for devices that are connected together?
**Answer**: `Network`
## What is the Internet?
### Who invented the World Wide Web?
* According to the information provided in the reading material:
> The first iteration of the Internet was within the ARPANET project in the late 1960s. This project was funded by the United States Defence Department and was the first documented network in action. However, it wasn't until 1989 when the Internet as we know it was invented by Tim Berners-Lee by the creation of the **W**orld **W**ide **W**eb (**WWW**). It wasn't until this point that the Internet wasn't used as a repository for storing and sharing information (like it is today).

**Answer**: ` Tim Berners-Lee`
## Identifying Devices on a Network
### What does the term "IP" stand for?
* According to the information provided in the reading material:
> Briefly, an **IP** address (or **I**nternet **P**rotocol) address can be used as a way of identifying a host on a network for a period of time, where that IP address can then be associated with another device without the IP address changing.

**Answer**: `Internet Protocol`
### What is each section of an IP address called?
* According to the information provided in the reading material:
An IP address is a set of numbers that are divided into four octets. The value of each octet will summarize to be the IP address of the device on the network.

**Answer**: `Octets`
### How many sections (in digits) does an IP address have? 
**Answer**: `4`
### What does the term "MAC" stand for?
* According to the information provided in the reading material:
> Devices on a network will all have a physical network interface, which is a microchip board found on the device's motherboard. This network interface is assigned a unique address at the factory it was built at, called a **MAC** (**M**edia **A**ccess **C**ontrol) address.

**Answer**: `Media Access Control`
### Deploy the interactive lab using the "View Site" button and spoof your MAC address to access the site.  What is the flag?
**Flag**: `THM{YOU_GOT_ON_TRYHACKME}`
## Ping (ICMP)
### What protocol does ping use?
* According to the information provided in the reading material:
> Ping uses **ICMP** (**I**nternet **C**ontrol **M**essage **P**rotocol) packets to determine the performance of a connection between devices, for example, if the connection exists or is reliable.

**Answer**: `ICMP`
### What is the syntax to ping `10.10.10.10`?
**Answer**: `ping 10.10.10.10`
### What flag do you get when you ping 8.8.8.8?
```bash
user@thm:~$ ping -c 4 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=7.16 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=8.83 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=8.29 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=8.31 ms
--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 8.132/9.428/10.957/1.057 ms
Flag: THM{I_PINGED_THE_SERVER}
```
**Flag**: `THM{I_PINGED_THE_SERVER}`