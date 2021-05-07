# Hack The Box [Easy Phish](https://app.hackthebox.eu/challenges/79)
### References
* Septian, T. W. (2020, April 21). twseptian. Twseptian. https://twseptian.github.io/hackthebox%20challenge/htb-challenge-osint-easy-phisy/
## Description
> Customers of secure-startup.com have been receiving some very convincing phishing emails, can you figure out why?
## Challenge
```
$ dig TXT secure-startup.com _dmarc.secure-startup.com
;; Warning: Client COOKIE mismatch

; <<>> DiG 9.16.15 <<>> TXT secure-startup.com _dmarc.secure-startup.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 17162
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1220
; COOKIE: d5ba993438bb8b3e86a1aee860953e7131ec2b106310ac39 (bad)
;; QUESTION SECTION:
;secure-startup.com.            IN      TXT

;; ANSWER SECTION:
secure-startup.com.     1789    IN      TXT     "v=spf1 a mx ?all - HTB{RIP_SPF_Always_2nd"

;; Query time: 10 msec
;; SERVER: 192.168.1.1#53(192.168.1.1)
;; WHEN: Fri May 07 23:19:57 AEST 2021
;; MSG SIZE  rcvd: 129

;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 4858
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1220
; COOKIE: f50e876d94c38e2209831f2360953e7d7396ef687da7d30c (good)
;; QUESTION SECTION:
;_dmarc.secure-startup.com.     IN      TXT

;; ANSWER SECTION:
_dmarc.secure-startup.com. 1800 IN      TXT     "v=DMARC1;p=none;_F1ddl3_2_DMARC}"

;; Query time: 30 msec
;; SERVER: 192.168.1.1#53(192.168.1.1)
;; WHEN: Fri May 07 23:19:57 AEST 2021
;; MSG SIZE  rcvd: 127
```

*Flag**: `HTB{RIP_SPF_Always_2nd_F1ddl3_2_DMARC}`