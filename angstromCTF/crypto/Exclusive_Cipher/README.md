# [ångstromCTF 2021](https://2021.angstromctf.com/) Exclusive Cipher
### References
* Szymański, Ł. (2021). ångstromCTF 2021: Exclusive Cipher. szymanski.ninja. https://szymanski.ninja/en/ctfwriteups/2021/angstromctf/exclusive-cipher/
## Question
> Clam decided to return to classic cryptography and revisit the XOR cipher! Here's some hex encoded ciphertext:
> ```
> ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d2182> 27e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c
> ```
> The key is 5 bytes long, and the flag is somewhere in the message.
## Analysis
Assuming 2 hexadecimal digits are equivalent to 1 ASCII characters, a possible key can be found by XORing the ciphertext with the known 5-bytes long substring `actf{`.
## [My Solution](https://github.com/AppleGamer22/AppleGamer22/tree/master/angstromCTF/crypto/Exclusive_Cipher/decode_xor2.py)
In an XOR Cipher, it is known that `possible_key = ciphertext ^ known_cleartext`. The python script attached:
1. slices the ciphertext to all possible 5 characters-long (assuming 2 hexadecimal digits are equivalent to 1 ASCII characters) sections,
2. computes `possible_key = ciphertext ^ known_cleartext`, for a known substring of `actf{`,
3. expands the key to the ASCII length of the message,
4. rotates the key to deal with cases where the known clear text is not in an index that is a multiple of the key length.
   * Thanks to [@Levon](https://hashnode.com/@Levon) for this suggestion.
5. recomputes the XOR to possibly decode the message
6. and prints the possible message as ASCII.

### Python Script Output
* A Python script that prints all valid solutions for the full ciphertext and the ciphertext without the first character:
```python
ciphertext_hex1 = "ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c"
known_cleartext1 = "actf{"
hint1 = "flag"

for solution in decode_xor(ciphertext_hex1, known_cleartext1, hint1):
	print(f"key: {solution['key']})")
	print(f"message: {solution['cleartext']}")

for solution in decode_xor(ciphertext_hex1[2:], known_cleartext1, hint1):
	print(f"key: {solution['key']})")
	print(f"message: {solution['cleartext']}")
```
* The output of the screen described immediately above:
```
key: [237, 72, 133, 93, 102])
message: Congratulations on decrypting the message! The flag is actf{who_needs_aes_when_you_have_xor}. Good luck on the other crypto!
key: [72, 133, 93, 102, 237])
message: ongratulations on decrypting the message! The flag is actf{who_needs_aes_when_you_have_xor}. Good luck on the other crypto!
```
**Flag**: `actf{who_needs_aes_when_you_have_xor}`