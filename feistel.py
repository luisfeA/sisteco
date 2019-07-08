from numpy import array,dot,append

def xor(A1,A2):
    i=0
    aux=[]
    while i<len(A1):
        if (A1[i] != A2[i]):
            aux.append(1)
        else:
            aux.append(0)
        i+=1
    return array(aux)


def F(R,key):
    #print(R)
    #print(key)
    #print(array(list(format(dot(R,key[0:len(key)//2]),'08b'))).astype('int'))
    return (R*key[len(R):(2*len(R))]*(array(list(format(dot(R,key[0:len(R)]),'08b'))).astype('int')))


def feistel(entrada, key):
    L=entrada[0:(len(entrada)//2)]
    R=entrada[(len(entrada)//2):]
    nR=F(R,key)
    return append(R,xor(L,nR))


def invertir(entrada):
    return append(entrada[(len(entrada)//2):],entrada[0:(len(entrada)//2)])

def shftKey(entrada):
    largo=len(entrada)
    l=append((entrada[3*(largo//4):]),entrada[0:(largo//4)] )
    r=append((entrada[(largo//4):(largo//2)]+1)%2,entrada[(largo//2):3*(largo//4)] )
    return xor(entrada,append(l,r))

#array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

def ciclar(entrada,key,ciclos):
    x=entrada
    k=key
    i=0
    while(i<ciclos):
        key=shftKey(key)
        entrada=feistel(entrada,key)
        i+=1
        print("encriptado "+str(i), entrada)
    print("original     ",x)
    print("llave        ",k)
