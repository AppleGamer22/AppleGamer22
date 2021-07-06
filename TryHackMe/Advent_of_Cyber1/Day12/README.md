# TryHackMe [Advent of Cyber 1](https://tryhackme.com/room/25daysofchristmas) Day 12
### References
* MuirlandOracle. (2020, January 6). MuirlandOracle. MuirlandOracle’s Blog. https://muirlandoracle.co.uk/2020/01/06/tryhackme-christmas-2019-challenge-write-up/
## What is the md5 hashsum of the encrypted `note1` file?
```bash
$ md5sum note1.txt.gpg
24cf615e2a4f42718f2ff36b35614f8f  note1.txt.gpg
```
**Answer**: `24cf615e2a4f42718f2ff36b35614f8f`
## Where was elf Bob told to meet Alice?
* According to the hint:
> gpg key is 25daysofchristmas

```bash
$ gpg -d note1.txt.gpg 
gpg: AES.CFB encrypted data
gpg: encrypted with 1 passphrase
I will meet you outside Santa's Grotto at 5pm!
```

**Answer**: `Santa's Grotto`
## Decrypt `note2` and obtain the flag!
* According to the hint:
> private password is hello

1. Decrypt `note2`
```bash
$ openssl rsautl -decrypt -inkey private.key -in note2_encrypted.txt -out note2_decrypted.txt
Enter pass phrase for private.key: hello
```
2. Read `note2_decrypted.txt`:
```bash
$ cat note2_decrypted.txt 
THM{ed9ccb6802c5d0f905ea747a310bba23}
```

**Flag**: `THM{ed9ccb6802c5d0f905ea747a310bba23}`