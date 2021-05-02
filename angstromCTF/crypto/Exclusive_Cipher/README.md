# Exclusive Cipher
Clam decided to return to classic cryptography and revisit the XOR cipher! Here's some hex encoded ciphertext:
```
ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c
```
The key is 5 bytes long, and the flag is somewhere in the message.
## Solution:
In XOR Cipher, it is known that `possible_key = ciphertext ^ known_cleartext`. The python script attached:
1. slices the ciphertext to all possible 5 characters-long (assuming 2 hexadecimal digits are equivalent to 1 ASCII characters) sections,
2. computes `possible_key = ciphertext ^ known_cleartext`, for a known substring of `actf{`
3. expands the key to the ASCII length of the message,
4. recomputes the XOR to possibly decode the message
5. prints the possible message as ASCII.
```
hex-encoded ciphertext: ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c
known cleartext (of key length): actf{
hint (such as 'flag'): flag
key: [237, 72, 133, 93, 102] ('íH]f')
message: Congratulations on decrypting the message! The flag is actf{who_needs_aes_when_you_have_xor}. Good luck on the other crypto!
```
**Flag**: `actf{who_needs_aes_when_you_have_xor}`