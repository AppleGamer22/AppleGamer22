# TryHackMe [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2) Day 7
## Open `pcap1.pcap` in Wireshark. What is the IP address that initiates an ICMP/ping?
1. open pcap
2. filter `icmp`
3. find sender of 1st ping
**Answer**: `10.11.3.2`

## If we only wanted to see HTTP GET requests in our `pcap1.pcap` file, what filter would we use?
**Answer**: ``

## Now apply this filter to `pcap1.pcap` in Wireshark, what is the name of the article that the IP address **10.10.67.199** visited?
**Answer**: ``

## Let's begin analysing `pcap2.pcap`. Look at the captured FTP traffic; what password was leaked during the login process?
1. Filter by ftp
2. look for user input that looks like a bad password

**Answer**: `plaintext_password_fiasco`

## Continuing with our analysis of `pcap2.pcap`, what is the name of the protocol that is encrypted?
**Answer**: ``

## What is on Elf McSkidy's (`pcap3.pcap`) wishlist that will be used to replace Elf McEager?
**Answer**: ``