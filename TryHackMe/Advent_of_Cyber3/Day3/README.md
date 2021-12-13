# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 3
### References
* InsiderPhD. (2021). Try Hack Me: Advent of Cyber 2021 - Day 3 [YouTube Video]. In YouTube. https://youtu.be/8dUylKcDUvU

## Using a common word list for discovering content, enumerate `http://<MACHINE_IP>` to find the location of the administrator dashboard. What is the name of the folder?
```bash
$ gobuster dir -u http://<MACHINE_IP>/ -w /usr/share/dirb/wordlists/small.txt
/admin                (Status: 301) [Size: 312] [--> http://<MACHINE_IP>/admin/]
/assets               (Status: 301) [Size: 313] [--> http://<MACHINE_IP>/assets/]
/javascript           (Status: 301) [Size: 317] [--> http://<MACHINE_IP>/javascript/]
```

**Answer**: `admin`
## In your web browser, try some default credentials on the newly discovered login form for the **`administrator`** user. What is the password?
* In some extreme cases, the password is the same as the username, therefore a username of `administrator` and a password of `administrator` was attempted first.

**Answer**: `administrator`
## Access the admin panel. What is the value of the flag?
**Flag**: `THM{ADM1N_AC3SS}`