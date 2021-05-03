from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

one = {
	"c": 0xd906aac5b10009dc45b685aef03a10978f550d6b0ab2eb4e8c796c57866435c8,
	"k": 0xa1ed15f60534137dbf621e0892e52e40
}
two = {
	"c": 0x838c79f90ec64855108b92669e6a97c97d40a0032915565ca870de9e32cd3f70,
	"k": 0x964e03d43489c923184f7087f6a519f5,
	"iv": 0x36ebd72c44c684dede483259e2c00166
}

cipher1 = AES.new(long_to_bytes(one["k"]), AES.MODE_ECB)
flag1 = cipher1.decrypt(long_to_bytes(one["c"])).replace(b"\x0e", b"")

cipher2 = AES.new(long_to_bytes(two["k"]), AES.MODE_CBC, long_to_bytes(two["iv"]))
flag2 = cipher2.decrypt(long_to_bytes(two["c"])).replace(b"\r", b"")
flag = str(flag1 + flag2)
print(flag)