from typing import TypedDict, List
from textwrap import wrap
from pwn import xor

class XORSolution(TypedDict):
	key: List[int]
	cleartext: str


def decode_xor(ciphertext_hex: str, known_cleartext: str, hint: str) -> List[XORSolution]:
	output = []
	cipher_ascii = bytes(int(letter, 16) for letter in wrap(ciphertext_hex, 2))
	for i in range(len(cipher_ascii)):
		key = list(xor(cipher_ascii[i:i + len(known_cleartext)], known_cleartext.encode()))
		for ii in range(len(key)):
			rotated_key = key[-ii:] + key[:-ii]
			cleartext = str(xor(cipher_ascii, rotated_key))[2:-1]
			if known_cleartext in cleartext and hint in cleartext:
				output.append({"key": rotated_key, "cleartext": cleartext})
	return output

ciphertext_hex1 = "ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c"
known_cleartext1 = "actf{"
hint1 = "flag"

for solution in decode_xor(ciphertext_hex1, known_cleartext1, hint1):
	print(f"key: {solution['key']})")
	print(f"message: {solution['cleartext']}")

for solution in decode_xor(ciphertext_hex1[2:], known_cleartext1, hint1):
	print(f"key: {solution['key']})")
	print(f"message: {solution['cleartext']}")
