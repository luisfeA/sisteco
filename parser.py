import numpy as np



def encriptar(bitsize):
    entrada=input("ingrese frase: ")
    lista=[]

    padding=len(entrada)%4
    entrada=entrada+(" "*padding)

    i=0
    while(i<len(entrada)):
        a=format(ord(entrada[i]),'08b')
        b=format(ord(entrada[i+1]),'08b')
        c=format(ord(entrada[i+2]),'08b')
        d=format(ord(entrada[i+3]),'08b')
        x='0b'+a+b+c+d
        lista.append(x)
        i+=4
    print(lista)