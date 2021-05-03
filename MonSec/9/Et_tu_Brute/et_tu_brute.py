from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

key = "ac2ca7cf871bb49aac6d05990f37"

with open("flag.enc", "rb") as flag_file:
	ciphertext = flag_file.read()
	for i in range(0, 16):
		for ii in range(0, 16):
			for iii in range(0, 16):
				for iv in range(0, 16):
					hex_suffix = hex(i)[2:] + hex(ii)[2:] + hex(iii)[2:] + hex(iv)[2:]
					cipher = AES.new(unhexlify(key + hex_suffix), AES.MODE_ECB)
					cleartext = str(cipher.decrypt(ciphertext))
					if "MONSEC" in cleartext:
						print(cleartext)