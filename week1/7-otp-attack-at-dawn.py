import sys
import pdb
import binascii

message = "attack at dawn"
newMessage = "attack at dusk"
ciphertext = "6c73d5240a948c86981bc294814d"

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def encrypt(key, msg):
    c = strxor(key, msg)
    #print
    #print c.encode('hex')
    #print binascii.hexlify(c)
    #return binascii.hexlify(c)
    return c

for (a,b,c) in zip(binascii.unhexlify(ciphertext), message, newMessage):
    print(a,b,c)

for (a,b,c) in zip(binascii.unhexlify(ciphertext), message, newMessage):
    print(a-(ord(b)-ord(c)))

for (a,b,c) in zip(binascii.unhexlify(ciphertext), message, newMessage):
    print(chr(a-(ord(b)-ord(c))))

it = "".join([chr(a-(ord(b)-ord(c))) for (a,b,c) in zip(binascii.unhexlify(ciphertext), message, newMessage)])

[hex(a-(ord(b)-ord(c))) for (a,b,c) in zip(binascii.unhexlify(ciphertext), message, newMessage)]
"".join([format(a-(ord(b)-ord(c)),'x') for (a,b,c) in zip(binascii.unhexlify(ciphertext), message, newMessage)])

pdb.set_trace()
print("done")


