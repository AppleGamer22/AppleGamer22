# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 23
### References
* Cybrites. (2021). AdventOfCyber Day23 | PowershELlF Magic [YouTube Video]. In YouTube. https://youtu.be/xx4K57lnaTI

## What command was executed as Elf McNealy to add a new user to the machine?
![`Invoke-Nightmare`](Invoke-Nightmare.png)

**Answer**: `Invoke-Nightmare`
## What user executed the PowerShell file to send the `password.txt` file from the administrator's desktop to a remote server?
![`sendit.ps1`](sendit.ps1.png)

**Answer**: `adm1n`
## What was the IP address of the remote server? What was the port used for the remote connection?
**Answer**: `10.10.148.96,4321`
## What was the encryption key used to encrypt the contents of the text file sent to the remote server?
**Answer**: `j3pn50vkw21hhurbqmxjlpmo9doiukyb`
## What application was used to delete the `password.txt` file?
![`sdelete.exe`](sdelete.exe.1.png)

**Answer**: `sdelete.exe`
## What is the date and timestamp the logs show that `password.txt` was deleted?
![`sdelete.exe`](sdelete.exe.2.png)

**Answer**: `11/11/2021 7:29:27 PM`
## What were the contents of the deleted `password.txt` file?
```powershell
$key = (New-Object System.Text.ASCIIEncoding).GetBytes("j3pn50vkw21hhurbqmxjlpmo9doiukyb")

$encrypted = "76492d1116743f0423413b16050a5345MgB8AEcAVwB1AFMATwB1ADgALwA0AGQAKwBSAEYAYQBHAE8ANgBHAG0AcQBnAHcAPQA9AHwAMwBlADAAYwBmADAAYQAzAGEANgBmADkAZQA0ADUAMABiADkANgA4ADcAZgA3ADAAMQA3ADAAOABiADkAZAA2ADgAOQA2ADAANQA3AGEAZAA4AGMANQBjADIAMAA4ADYAYQA0ADMAMABkADkAMwBiADUAYQBhADIANwA5AGMAYQA1ADYAYQAzAGEAYQA2ADUAMABjADAAMwAzADYANABlADYAOAA4ADQAYwAxAGMAYwAxADkANwBiADIANAAzADMAMAAzADgAYQA5ADYANAAzADEANAA2AGUAZgBkAGEAMAA3ADcANQAyADcAZgBlADMAZQA3ADUANwAyADkAZAAwAGUAOQA5ADQAOQA1AGQAYQBkADEANQAxADYANwA2AGIAYQBjADAAMQA0AGEAOQA3ADYAYgBkAGMAOAAxAGMAZgA2ADYAOABjADEAMABmADcAZgAyADcAZgBjADEAYgA3AGYAOAA3AGIANQAyAGUAMwA4ADgAYQAxADkANgA4ADMA"

echo $encrypted | ConvertTo-SecureString -key $key | ForEach-Object {[Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($_))}
```

**Answer**: `Mission Control: letitsnowletitsnowletitsnow`