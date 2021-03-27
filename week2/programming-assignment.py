from Crypto.Cipher import AES
from pdb import set_trace

# XOR'ing bytes: https://nitratine.net/blog/post/xor-python-byte-strings/
# pycrypto: https://www.dlitz.net/software/pycrypto/api/current/
# Hex to bytes: https://www.coursera.org/learn/crypto/discussions/weeks/2/threads/y3hgXmO7Eeuhwwo1pM_uuQ

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

cbc_key = bytes.fromhex('140b41b22a29beb4061bda66b6747e14')
#cbc_ct = bytes.fromhex("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
cbc_ct = bytes.fromhex("5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253")

cipher = AES.new(cbc_key, AES.MODE_ECB)

out = b""
for i, c in enumerate(chunks(cbc_ct,16)):
    if i > 0:
        out += bytes([_a ^ _b for _a, _b in zip(cipher.decrypt(c), iv)])
    iv = c

out = out[:-out[-1]]

print(out)
#set_trace()
