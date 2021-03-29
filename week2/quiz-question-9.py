from pdb import set_trace

def F(k, x):
    t = int(k[0])
    for i in range(1,5):
        if x[i-1] == "1":
            t = t ^ int(k[i])
        print(t)
    return t

def Fp(_k, _x):
    if len(_k) != 5:
        raise Exception("K needs to be 5 bits")
    if len(_x) != 4:
        raise Exception("X needs to be 4 bits")
    k = int(_k,2)
    x = int(_x,2)
    t = int(_k[0])
    for i in range(1,5):
        if _x[i-1] == "1":
            print("K {} {} X {} {}".format(_k,k,_x,x))
            t = t ^ int(_k[i])
    return format(t, '04b')

def doit(x, e):
    for i in range(0,32):
        k = format(i, '{fill}{width}b'.format(width=5, fill=0))
        o = Fp(k, x)
        print("k:{} := o:{}".format(k,o))
        if e == o:
            print(k)

#Fp("01101", "0011")
#doit("0110", "0011")
doit("0101", "1010")
#doit("1110", "0110")
set_trace()
