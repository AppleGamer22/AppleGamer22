# TryHackMe [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2) Day 4
### References
* DarkSec. (2020). TryHackMe Advent of Cyber 2: Day 4 [YouTube Video]. In YouTube. https://youtu.be/7GAFQdYCk5s

## Given the URL `http://shibes.xyz/api.php`, what would the entire `wfuzz` command look like to query the `breed` parameter using the word list `big.txt`?
> **Note**: For legal reasons, do not actually run this command as the site in question has not consented to being fuzzed!

**Answer**: `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ`
## Use `gobuster` **(against the target you deployed - not the`shibes.xyz` domain)** to find the API directory. What file is there?

1. Find the path of the API directory:
```bash
$ gobuster dir -u http://<MACHINE_IP> -w $(pwd)/big.txt -x .php
/.htpasswd            (Status: 403) [Size: 277]
/.htaccess.php        (Status: 403) [Size: 277]
/.htpasswd.php        (Status: 403) [Size: 277]
/.htaccess            (Status: 403) [Size: 277]
/LICENSE              (Status: 200) [Size: 1086]
/api                  (Status: 301) [Size: 310] [--> http://<MACHINE_IP>/api/]
```
2. Go to `http://<MACHINE_IP>/api/` and find the `site-log.php` file:
![API directory](api.jpg)

**Answer**: `site-log.php`

## Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?
```bash
$ wfuzz -c -z file,$(pwd)/big.txt -u http://http://<MACHINE_IP>/api/site-log.php?date=FUZZ
``
