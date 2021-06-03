# TryHackMe [Networking](https://www.tryhackme.com/room/bpnetworking)
### References
* Aryal, A. (2020, October 13). TryHackMe – Networking (Write-up). Deepak Aryal. https://avhiaryal54.wordpress.com/2020/10/13/tryhackme-networking-write-up/
## Kinda like a street address, just cooler.
IP Address Class | Octet Range
--|--
A | from 1 to 127
B | from 128 to 191
C | from 192 to 223
D | from 224 to 239
D | from 240 to 255

Private IP Address Class | Space
--|--
A | from `10.0.0.0`
B | from `172.16.0.0` to `172.31.255.255`
C | from `192.168.0.0` to `192.168.255.255`

### How many categories of IPv4 addresses are there?
**Answer**: `5`
### Which type is for research?
**Answer**: `E`
### How many private address ranges are there?
**Answer**: `3`
### Which private range is typically used by businesses?
**Answer**: `A`
### There are two common default private ranges for home routers, what is the first one?
**Answer**: `192.168.0.0`
### How about the second common private home range?
**Answer**: `192.168.1.0`
### How many addresses make up a typical class C range (specifically a `/24`)?
**Answer**: `256`
### Of these addresses two are reserved, what is the first addresses typically reserved as?
**Answer**: `Network`
### The very last address in a range is typically reserved as what address type?
**Answer**: `Broadcast`
### A third predominant address type is typically reserved for the router, what is the name of this address type?
**Answer**: `Gateway`
### Which address is reserved for testing on individual computers?
**Answer**: `127.0.0.1`
### A particularly unique address is reserved for unroutable packets, what is that address?
**Answer**: `0.0.0.0`
## Binary to Decimal
### `1001 0010`
**Answer**: `146`
### `0111 0111`
**Answer**: `119`
### `1111 1111`
**Answer**: `255`
### `1100 0101`
**Answer**: `197`
### `1111 0110`
**Answer**: `246`
### `0001 0011`
**Answer**: `19`
### `1000 0001`
**Answer**: `129`
### `0011 0001`
**Answer**: `49`
### `0111 1000`
**Answer**: `120`
### `1111 0000`
**Answer**: `240`
### `0011 1011`
**Answer**: `59`
### `0000 0111`
**Answer**: `7`
## Decimal to Binary
### 238
**Answer**: `11101110`
### 34
**Answer**: `00100010`
### 123
### 50
**Answer**: `00110010`
### 255
**Answer**: `11111111`
### 200
**Answer**: `11001000`
### 10
**Answer**: `00001010`
### 138
**Answer**: `10001010`
### 1
**Answer**: `00000001`
### 13
**Answer**: `00001101`
### 250
**Answer**: `11111010`
### 114
**Answer**: `01110010`
## Address Class Identification
IP Address Class | Octet Range
--|--
A | from 1 to 127
B | from 128 to 191
C | from 192 to 223
D | from 224 to 239
D | from 240 to 255

### `10.240.1.1`
**Answer**: `A`
### `150.10.15.0`
**Answer**: `B`
### `192.14.2.0`
**Answer**: `C`
### `148.17.9.1`
**Answer**: `B`
### `193.42.1.1`
**Answer**: `C`
### `126.8.156.0`
**Answer**: `A`
### `220.200.23.1`
**Answer**: `C`
### `230.230.45.58`
**Answer**: `D`
### `177.100.18.4`
**Answer**: `B`
### `119.18.45.0`
**Answer**: `A`
### `117.89.56.45`
**Answer**: `A`
### `215.45.45.0`
**Answer**: `C`