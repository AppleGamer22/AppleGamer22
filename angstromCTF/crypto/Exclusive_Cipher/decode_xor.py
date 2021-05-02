from typing import List
from doctest import testmod
from textwrap import wrap


def xor(s: List[int], t: List[int]) -> List[int]:
	"""
	:param s: list of non-negative integers
	:param t: list of non-negative integers
	:return: XOR of the ith number of both lists
	"""
	return [a ^ b for a, b in zip(s, t)]


def expand_key(short_key: List[int], size: int) -> List[int]:
	"""
	:param short_key: list of non-negative integers
	:param size: positive integer
	:return: short_key * (size // len(short_key)) + short_key[:size - len(key_expanded)]

	>>> expand_key([1, 2, 3, 4, 5], 9)
	[1, 2, 3, 4, 5, 1, 2, 3, 4]
	"""
	assert size > len(short_key)
	key_expanded = short_key * (size // len(short_key))
	for ii in range(size - len(key_expanded)):
		key_expanded.append(short_key[ii])
	return key_expanded


ciphertext_text = input("hex-encoded ciphertext: ")
known_cleartext = input("known cleartext (with length of key): ")
hint = input("hint (such as 'flag'): ")

cipher_ascii = [int(letter, 16) for letter in wrap(ciphertext_text, 2)]
known_cleartext_ascii = [ord(letter) for letter in known_cleartext]

for i in range(len(cipher_ascii) - len(known_cleartext)):
	key = xor(cipher_ascii[i:i + len(known_cleartext)], known_cleartext_ascii)
	expanded_key = expand_key(key, len(cipher_ascii))
	message_ascii = xor(cipher_ascii, expanded_key)
	message_text = "".join(map(chr, message_ascii))
	if known_cleartext in message_text and hint in message_text:
		print(f"key: {key} ('{(''.join(map(chr, key)))}')")
		print(f"message: {message_text}")
		print()


if __name__ == "__main__":
	testmod()

