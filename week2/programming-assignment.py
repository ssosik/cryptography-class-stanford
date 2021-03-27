from Crypto.Cipher import AES
from pdb import set_trace

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

cbc_key1 = bytes.fromhex('140b41b22a29beb4061bda66b6747e14')
cbc_ct1 = bytes.fromhex("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
iv = cbc_ct1[:16]
c1 = cbc_ct1[16:32]

cipher = AES.new(cbc_key1, AES.MODE_ECB)
print(bytes([_a ^ _b for _a, _b in zip(cipher.decrypt(c1), iv)]))
print([bytes([_a ^ _b for _a, _b in zip(cipher.decrypt(c), iv)]) for c in chunks(cbc_ct1[16:],16)])
set_trace()

