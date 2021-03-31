from pdb import set_trace
from itertools import product

def F(k, x):
    t = int(k[0])
    for i in range(1,5):
        if x[i-1] == "1":
            t = t ^ int(k[i])
        print(t)
    return t

def Fp(k, _x):
    if len(k) != 5:
        raise Exception("K needs to be 5 bits")
    if len(_x) != 4:
        raise Exception("X needs to be 4 bits")
    x = int(_x,2)
    t = int(k[0], 2)
    for i in range(1,5):
        if _x[i-1] == "1":
            #print("K {} X {} {}".format(k,_x,x))
            t = t ^ int(k[i],2)
    return format(t, '04b')

def doit(x, e):
    for k in product([format(i,'04b') for i in range(0,16)], repeat=5):
        o = Fp(k, x)
        #print("k:{} := o:{}".format(k,o))
        if e == o:
            print("E:{} O:{} + K:{}".format(e, o, k))

#Fp("01101", "0011")
#doit("0110", "0011")
doit("0101", "1010")
#doit("1110", "0110")
set_trace()
