from pylab import *
import matplotlib.pyplot as plt
from time import time
import random




# SBOX
S_BOX = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

# Matriz de expansion para obtener 48 bits y realizar operacion XOR
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]



# permutacion inicial de los datos
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9,  1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# permutacion inicial en la generacion de subclaves
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Permutacion de compresion para obtener la clave ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]


# Permutacion hecha despues de cada sustitucion de sBox para cada ronda
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Permutacion final despues de las 16 rondas
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

# Desplazamiento circular a la izquierda a los sub-bloques
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


###################################################################################################
#Entrada: String
#Salida:  Arreglo de bits
#Funcion: Transformar uns string a un arreglo de String
###################################################################################################
def string_to_bit_array(text):
    array = list()
    for char in text:
        binval = binvalue(char, 8)#Get the char value on one byte
        array.extend([int(x) for x in list(binval)]) #Add the bits to the final list
    return array


###################################################################################################
#Entrada: Arreglo de bit
#Salida:  String
#Funcion: Transformar uns arreglo de bit a String
###################################################################################################
def bit_array_to_string(array): #Recreate the string from the bit array
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in  nsplit(array,8)]])
    return res


###################################################################################################
#Entrada: Valores binarios y tamaño de cantidad de bit
#Salida:  Valor binario en forma de string
#Funcion: Crea un string con los valores binarios, en caso de que el largo de la cadena de binarios
#         es menor al tamaño que se especifica se rellena con ceros.
###################################################################################################
def binvalue(val, bitsize): #Return the binary value as a string of the given size
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise Exception("binary value larger than the expected size")
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

###################################################################################################
#Entrada: Lista y tamano de las sublistas
#Salida:  Los subarreglos
#Funcion: Cortar una lista segun el tamano que se especifica
###################################################################################################
def nsplit(s, n):#Split a list into sublists of size "n"
    return [s[k:k+n] for k in range(0, len(s), n)]

ENCRYPT=1
DECRYPT=0


class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()


    ###################################################################################################
    # Entrada: Dos listas y un valor numerico
    # Salida:  Dos listas desplazadas
    # Funcion: Realiza el desplazamiento a las dos listas segun el valor n dado
    ###################################################################################################
    def shift(self, g, d, n):
        return g[n:] + g[:n], d[n:] + d[:n]

    ###################################################################################################
    # Entrada: Vacio
    # Salida:  Vacio
    # Funcion: Rellena el texto para que sea multiplo de 8 y se guarda en el atributo text
    ###################################################################################################
    def addPadding(self):
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

    ###################################################################################################
    # Entrada: String que representa el texto
    # Salida:  String que representa el texto pero sin relleno
    # Funcion: Quita el relleno que se le agrego con anterioridad
    ###################################################################################################
    def removePadding(self, data):
        pad_len = ord(data[-1])
        return data[:-pad_len]

    ###################################################################################################
    # Entrada: Arreglo que representa el bloque y una matriz que representa la tabla de permutaciones
    # Salida:  Arreglo con los bits permutados
    # Funcion: Realizar la permutacion del bloque usando la tabla correspondiente
    ###################################################################################################
    def permut(self, block, table):
        return [block[x - 1] for x in table]

    ###################################################################################################
    # Entrada: Arreglo que representa el bloque y una matriz que representa la tabla de permutaciones
    # Salida:  Arreglo con los bits permutados
    # Funcion: Realizar la permutacion del bloque usando la tabla correspondiente
    ###################################################################################################
    def expand(self, block,
               table):  # Hace los mismo que el metodo para permutar, solo que se usa otro nombre para no entrar en confusion
        return [block[x - 1] for x in table]

    ###################################################################################################
    # Entrada: Lista t1 y Lista t2
    # Salida:  Lista resultante al aplicar xor
    # Funcion: Realiza un or exclisivo a las listas qque ingresan como parametros
    ###################################################################################################
    def xor(self, t1, t2):
        return [x ^ y for x, y in zip(t1, t2)]

    ###################################################################################################
    # Entrada: arreglo que representa El lado derecho del bloque expandido
    # Salida:  Lista con los bits permutados
    # Funcion: Transformar uns string a una lista de bits
    ###################################################################################################
    def substitute(self, d_e):  # Subtituye los bytes usando para ello SBOX
        subblocks = nsplit(d_e, 6)  # separa el arreglo de bits en sublistas de 6 bits
        result = list()
        for i in range(len(subblocks)):  # Por cada subbloque
            block = subblocks[i]
            row = int(str(block[0]) + str(block[5]), 2)  # Se obtiene la fila con el primer y ultimo bit
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)  # La columnas son los 2,3,4 y 5 bits
            val = S_BOX[i][row][column]  # Toma el valor de sBox apropiado para la ronda i.
            bin = binvalue(val, 4)  # Convierte el valor en binario
            result += [int(x) for x in bin]  # y se agrega a la lista resul
        return result

    ###################################################################################################
    # Entrada: Vacio
    # Salida:  Vacio
    # Funcion: Metodo que Genera una lista con todas las llaves usadas en la rondas, se guarda en el atributo de la clase
    ###################################################################################################
    def generatekeys(self):
        self.keys = []
        key = string_to_bit_array(self.password)
        key = self.permut(key, CP_1)  # Se aplica la permutacion inicial a la llave
        g, d = nsplit(key, 28)  # Se separa la llave en (g->LEFT),(d->RIGHT)
        for i in range(16):  # Comienzas las 16 rondas
            g, d = self.shift(g, d, SHIFT[i])  # Aplica el desplazamiento asociado a cada ronda
            tmp = g + d  # Se juntan nuevamente las partes
            self.keys.append(self.permut(tmp,
                                         CP_2))  # Se aplica la permutacion para obtner los Ki y se guardan el atributo de la clase

    ###################################################################################################
    # Entrada: Llave, texto a cifrar, accion Permut made after each SBox substitution for each round(Encriptar o Desencriptar) y padding
    # Salida:  Mensaje cifrado o descifrado
    # Funcion: Realiza el proceso de cifrado o descifrado segun la accion que se especifique
    ###################################################################################################
    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise Exception("La llave debe ser de longitud 8 bit")
        elif len(key) > 8:
            key = key[:8]  # Si la llave es mayor a 8 se corta en los 8 primeros bits

        self.password = key
        self.text = text

        if padding and action == ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:  #Si no se especifica el padding en TRUE solo se pueden procesar textos de largo multiplos de 8
            raise Exception("Tamano del dato debe ser multiĺo de 8")

        self.generatekeys()  # Aqui se generan todas las llaves
        text_blocks = nsplit(self.text, 8)  # Corta el texto en bloques de 8 bytes (64 bits)
        result = list()
        for block in text_blocks:  # For que recorre todos los bloques del texto
            block = string_to_bit_array(block)  # Convierte el string en un arreglo de bits
            block = self.permut(block, PI)  # Se aplica la permutacion inicial
            g, d = nsplit(block, 32)  # g(LEFT), d(RIGHT)
            tmp = None
            for i in range(16):  # Aqui se realizan las 16 rondas
                d_e = self.expand(d, E)  # Se expande d (32 bits) para que coincida con el tamaño de Ki(48bits)
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d_e)  # Si es para encriptar se usa Ki
                else:
                    tmp = self.xor(self.keys[15 - i], d_e)  # Si es para desencriptar se usa la ultima llave
                tmp = self.substitute(tmp)  # Metodo que aplica los SBOXes
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            result += self.permut(d + g, PI_1)  # Hace la ultima permutación y agrega ese resultado en la variable result
        final_res = bit_array_to_string(result)
        if padding and action == DECRYPT:
            return self.removePadding(final_res)  # Se remueve el padding si se esta descifrando y si padding = True
        else:
            return final_res  # Retorna el string final para el cifrado y descifrado

    ###################################################################################################
    # Metodo run para realizar test de avalancha
    #
    #
    ###################################################################################################
    def run_test(self, key, text, n, action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise Exception("La llave debe ser de longitud 8 bit")
        elif len(key) > 8:
            key = key[:8]  # Si la llave es mayor a 8 se corta en los 8 primeros bits

        self.password = key
        self.text = text

        if padding and action == ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:  #Si no se especifica el padding solo se pueden porcesar textos de largo multiplos de 8
            raise Exception("Tamano del dato debe ser multiĺo de 8")

        self.generatekeys()  # Aqui se generan todas las llaves
        text_blocks = nsplit(self.text, 8)  # Corta el texto en bloques de 8 bytes (64 bits)
        result = list()
        for block in text_blocks:  # For que recorre todos los bloques del texto
            block = string_to_bit_array(block)  # Convierte el string en un arreglo de bits

            if block[n] == 0: #Se cambia un bit en la posicion n para comprobar el efecto avalancha
                block[n] = 1
            else:
                block[n] = 0

            #Comienza aca el efecto avalancha
            block = self.permut(block, PI)  # Se aplica la permutacion inicial
            g, d = nsplit(block, 32)  # g(LEFT), d(RIGHT)
            tmp = None
            for i in range(16):  # Aqui se realizan las 16 rondas
                d_e = self.expand(d, E)  # Se expande d (32 bits) para que coincida con el tamaño de Ki(48bits)
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d_e)  # Si es para encriptar se usa Ki
                else:
                    tmp = self.xor(self.keys[15 - i], d_e)  # Si es para desencriptar se usa la ultima llave
                tmp = self.substitute(tmp)  # Metodo que aplica los SBOXes
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            result += self.permut(d + g, PI_1)  # Hace la ultima permutación y agrega ese resultado en la variable result
            #Termina el proceso que produce el efecto avalancha
        final_res = bit_array_to_string(result)
        if padding and action == DECRYPT:
            return self.removePadding(final_res)  # Se remueve el padding si se esta descifrando y si padding = True
        else:
            return final_res  # Retorna el string final para el cifrado y descifrado


    ###################################################################################################
    # Entrada: Llave inicial, texto a cifrar y el relleno que por defecto es falso
    # Salida:  Retorna el texto cifrado
    # Funcion: Llama el metodo run, que realiza el proceso de cifrado/descifrado
    ###################################################################################################
    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)

    ###################################################################################################
    # Entrada: Llave inicial, texto cifrado y el relleno que por defecto es falso
    # Salida:  Retorna el texto descifrado
    # Funcion: Llama el metodo run, que realiza el proceso de cifrado/descifrado
    ###################################################################################################
    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)

    ###################################################################################################
    # Entrada: El numero de mensajes, Llave inicial, texto a cifrado
    # Salida:  Retorna el tiempo que se demora en cifrar y descifrar cierta cantidad de mensajes
    # Funcion: Crea un tiempo de partida y un tiempo final y retorna la resta de ambos para determinar el tiempo total
    ###################################################################################################
    def n_message_test(self,n, text, key):
        t1 = time()
        for i in range(n):
            cifrado = self.encrypt(key,text,True) #Cifrado
            self.decrypt(key,cifrado,True)        #Descifrado
        t2 = time()
        return t2-t1

    ###################################################################################################
    # Entrada: El tamano del mensajes, Llave inicial, texto a cifrado y descifrar
    # Salida:  Retorna el tiempo que se demora en cifrar y descifrar un mensaje con cierto tamano
    # Funcion: Crea un tiempo de partida y un tiempo final y retorna la resta de ambos para determinar el tiempo total
    ###################################################################################################
    def size_message_test(self,n,key):
        text="a"
        for i in range(n):
            text+="a"
        t1 = time()
        cifrado = self.encrypt(key, text, True)
        self.decrypt(key, cifrado, True)
        t2 = time()
        return t2-t1

    ###################################################################################################
    # Entrada: La Llave inicial, texto a cifrado y descifrar y la posicion del bit a cambiar
    # Salida:  Retorna la probabilidad de error al cambiar un solo bit
    # Funcion: Llamma a la funcion run_test que es para determinar que tanto cambian los bit al realizar el proceso de cifrado cuando se le cambia un bit en la entrada
    ###################################################################################################
    def efecto_avalancha(self,key,text,n):
        cifrado = self.encrypt(key,text,True)
        cifrado2 = self.run_test(key,text,n,ENCRYPT,True)

        bin1 = string_to_bit_array(cifrado)
        bin2 = string_to_bit_array(cifrado2)

        errores = 0
        for i in range(len(bin1)):
            if bin1[i] != bin2[i]:
                errores+=1
        prob = errores/len(bin1)
        return prob




if __name__ == '__main__':
    key = "secret_k"
    text = "Hello woHello wo kjkljlkjk"
    d = des()
    r = d.encrypt(key, text, True)
    r2 = d.decrypt("secret_k", r, True)
    print("Ciphered: %r" % r)
    print("Deciphered: ", r2)
########################################################################################################################
#Cieminzan las pruebas de rendimiento y de efecto avalncha
########################################################################################################################
    '''
    n_mensajes = [10,100,500,1000,1500,2000,2500]
    tiempo1 = []
    tiempo11 = []
    tiempo12 = []
    for mensaje in n_mensajes:
        tiempo1.append(d.n_message_test(mensaje,"12345678", key))
    print("Tiempo1: ", tiempo1)

    for mensaje in n_mensajes:
        tiempo11.append(d.n_message_test(mensaje, "1234567812345678", key))
    print("Tiempo11: ", tiempo11)

    for mensaje in n_mensajes:
        tiempo12.append(d.n_message_test(mensaje, "123456781234567812345678", key))
    print("Tiempo12: ", tiempo12)

    s_mensaje = [80,800,4000,8000,12000,16000,20000]
    tiempo2 = []
    for mensaje in s_mensaje:
        tiempo2.append(d.size_message_test(mensaje,key))

    prob_avalancha = []
    print("Teimpo2: ", tiempo2)

    for i in range(8):
        n = int(random.random()*63)
        prob_avalancha.append(d.efecto_avalancha(key,"12345678",n))


    print("Probabilidad",prob_avalancha)
    '''


