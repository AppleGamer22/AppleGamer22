from textwrap import wrap
from pwn import xor

ciphertext_hex = "ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c"
known_cleartext = "actf{"
hint = "flag "
cipher_ascii = bytes(int(letter, 16) for letter in wrap(ciphertext_hex, 2))
for i in range(len(cipher_ascii)):
	key = xor(cipher_ascii[i:i + len(known_cleartext)], known_cleartext.encode())
	for ii in range(i, len(cipher_ascii)):
		sub = xor(cipher_ascii[ii:ii + len(known_cleartext)], key)
		message_text = str(xor(cipher_ascii, key))[2:-1]
		if known_cleartext in message_text and hint in message_text:
			print(i)
			print(f"key: {key}")
			print(f"message: {message_text}")
			break

