from pdb import set_trace

def F(k, x):
    t = int(k[0])
    for i in range(1,5):
        if x[i-1] == "1":
            t = t ^ int(k[i])
        print(t)
    return t

def Fp(k, x):
    ret = ""
    t = int(k[0])
    for i in range(1,5):
        if x[i-1] == "1":
            t = t ^ int(k[i])
        ret += "{}".format(t)
    return ret

def doit(x, e):
    for i in range(0,32):
        k = format(i, '{fill}{width}b'.format(width=5, fill=0))
        o = Fp(k, x)
        print("k:{} := o:{}".format(k,o))
        if e == o:
            print(k)

#doit("0110", "0011")
#doit("0101", "1010")
doit("1110", "0110")
set_trace()
