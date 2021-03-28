from Crypto.Cipher import AES
from pdb import set_trace

# XOR'ing bytes: https://nitratine.net/blog/post/xor-python-byte-strings/
# pycrypto: https://www.dlitz.net/software/pycrypto/api/current/
# Hex to bytes: https://www.coursera.org/learn/crypto/discussions/weeks/2/threads/y3hgXmO7Eeuhwwo1pM_uuQ

def chunker(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

cbc_key = bytes.fromhex('140b41b22a29beb4061bda66b6747e14')
cbc_ct1 = bytes.fromhex("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
cbc_ct2 = bytes.fromhex("5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253")

def cbc_decrypt(key, ct):
    cipher = AES.new(key, AES.MODE_ECB)

    out = b""
    for i, c in enumerate(chunker(ct,16)):
        if i > 0:
            out += bytes([_a ^ _b for _a, _b in zip(cipher.decrypt(c), iv)])
        iv = c

    return out[:-out[-1]]

print(cbc_decrypt(cbc_key, cbc_ct1))
print(cbc_decrypt(cbc_key, cbc_ct2))

ctr_key = bytes.fromhex("36f18357be4dbd77f050515c73fcf9f2")
ctr_ct1 = bytes.fromhex("69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329")
#ctr_ct1 = bytes.fromhex("770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451")

def ctr_decrypt(key, iv, ct):
    cipher = AES.new(key, AES.MODE_CTR)

    nonce = iv[:8]
    ctr = iv[8:]
    out = b""
    for i, c in enumerate(chunker(ct,16)):
        out += bytes([_a ^ _b for _a, _b in zip(cipher.decrypt(c), nonce + ctr)])
        #set_trace()
        print(ctr)
        ##iv += 1
        ctr = (int.from_bytes(ctr, "big") + 1).to_bytes(8, "big")
    
    return out

iv = ctr_ct1[:16]
print(ctr_decrypt(ctr_key, iv, ctr_ct1[16:]))
