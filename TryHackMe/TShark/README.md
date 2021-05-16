# TryHackMe [TShark](https://www.tryhackme.com/room/tshark)
### References
* DarkSec. (2021). TryHackMe TShark Official Walkthrough [YouTube Video]. In YouTube. https://youtu.be/tbXIFRS4u7I
## Reading PCAP Files
### How many packets are in the `dns.cap` file?
* TShark's `-r` flag enable reading a PCAP file.
* `wc`'s `-l` flag counts the lines of a given input.
```bash
$ tshark -r dns.cap | wc -l
38
```

**Answer**: `38`
### How many A records are in the capture (including responses)?
* TShark's `-Y "dns.qry.type == 1"` is used to filter DNS A records.
```bash
$ tshark -r dns.cap -Y "dns.qry.type == 1" | wc -l
6
```

**Answer**: `6`
### Which A record was present the most?
* TShark's `-T fields` is used to specify the output's format.
* TShark's `-e dns.qry.name` is specify which field to output.
```bash
$ tshark -r dns.cap -Y "dns.qry.type == 1" -T fields -e dns.qry.name
www.netbsd.org
www.netbsd.org
GRIMM.utelsystems.local
GRIMM.utelsystems.local
GRIMM.utelsystems.local
GRIMM.utelsystems.local
```

**Answer**: `GRIMM.utelsystems.local`
## DNS Exfil
### How many packets are in this capture?
```bash
$ tshark -r task3.pcap | wc -l
125
```
**Answer**: `125`
### How many DNS queries are in this PCAP (excluding responses)?
```bash
$ tshark -r task3.pcap -Y "dns.flags.response == 0" | wc -l
56
```
**Answer**: `56`
### What is the DNS transaction ID of the suspicious queries (in hex)?
```bash
$ tshark -r task3.pcap -Y "dns.flags.response == 0" -T fields -e dns.id
0x0000beef
```
**Answer**: `0x0000beef`
### What is the string extracted from the DNS queries?
```bash
$ tshark -r task3.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name | cut -c1 | tr "\n" " " | sed 's/ //g'
MZWGCZ33ORUDC427NFZV65BQOVTWQX3XNF2GQMDVG5PXI43IGRZGWIL5
```
**Answer**: `MZWGCZ33ORUDC427NFZV65BQOVTWQX3XNF2GQMDVG5PXI43IGRZGWIL5`
### What is the flag?
```bash
$ echo 'MZWGCZ33ORUDC427NFZV65BQOVTWQX3XNF2GQMDVG5PXI43IGRZGWIL5' | base32 -d
flag{th1s_is_t0ugh_with0u7_tsh4rk!}
```
**Flag**: `flag{th1s_is_t0ugh_with0u7_tsh4rk!}`