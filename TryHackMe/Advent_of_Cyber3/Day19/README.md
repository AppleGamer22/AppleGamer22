# TryHackMe [Advent of Cyber 3](https://tryhackme.com/room/adventofcyber3) Day 19
### References
* Cybersecurity Meg. (2021). TryHackMe: Advent of Cyber Day #19 - Task 24 Phishing Walkthrough! [YouTube Video]. In YouTube. https://youtu.be/0XKkSYVftPA

## Who was the email sent to?
**Answer**: `elfmcphearson@tbfc.com`
## Who sent the email?
**Answer**: `customerservice@t8fc.info`
## If this email was replied to, what email address will receive the email response?
**Answer**: `fisher@tempmailz.grinch`
##  What is the misspelled word?
**Answer**: `stright`
## What is the link to the credential harvesting website?
**Answer**: `https://89xgwsnmo5.grinch/out/fishing/`
## View the email source code. There is an unusual email header. What is the header and its value?
**Answer**: `X-GrinchPhish: >;^)`
## What is the name of the attachment?
**Answer**: `password-reset-instructions.pdf`
## What is the flag in the PDF file?
* Convert the Base64 string to a PDF document:
```bash
$ cat attachment-base64.txt | base64 -d > password-reset-instructions.pdf
```

**Flag**: `THM{A0C_Thr33_Ph1sh1ng_An4lys!s}`
