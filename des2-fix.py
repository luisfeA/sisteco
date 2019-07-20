from pylab import *
import matplotlib.pyplot as plt
from time import time
import random
import sys


ENCRYPT = 1
DECRYPT = 0


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
      57, 49, 41, 33, 25, 17, 9, 1,
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
# Entrada: String
# Salida:  Arreglo de bits
# Funcion: Transformar uns string a un arreglo de String
###################################################################################################
def string_to_bit_array(text):
    array = list()
    for char in text:
        binval = binvalue(char, 8)  # Get the char value on one byte
        array.extend([int(x) for x in list(binval)])  # Add the bits to the final list
    return array


###################################################################################################
# Entrada: Arreglo de bit
# Salida:  String
# Funcion: Transformar uns arreglo de bit a String
###################################################################################################
def bit_array_to_string(array):  # Recreate the string from the bit array
    res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in nsplit(array, 8)]])
    return res


###################################################################################################
# Entrada: Valores binarios y tamaño de cantidad de bit
# Salida:  Valor binario en forma de string
# Funcion: Crea un string con los valores binarios, en caso de que el largo de la cadena de binarios
#         es menor al tamaño que se especifica se rellena con ceros.
###################################################################################################
def binvalue(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise Exception("binary value larger than the expected size")
    while len(binval) < bitsize:
        binval = "0" + binval  # Add as many 0 as needed to get the wanted size
    return binval


###################################################################################################
# Entrada: Lista y tamano de las sublistas
# Salida:  Los subarreglos
# Funcion: Cortar una lista segun el tamano que se especifica
###################################################################################################
def nsplit(s, n):
    return [s[k:k + n] for k in range(0, len(s), n)]


###################################################################################################
# Entrada: Dos listas y un valor numerico
# Salida:  Dos listas desplazadas
# Funcion: Realiza el desplazamiento a las dos listas segun el valor n dado
###################################################################################################
def shift(g, d, n):
    return g[n:] + g[:n], d[n:] + d[:n]


###################################################################################################
# Entrada: Vacio
# Salida:  Vacio
# Funcion: Rellena el texto para que sea multiplo de 8 y se guarda en el atributo text
###################################################################################################
def addPadding(text):
    pad_len = 8 - (len(text) % 8)
    text += pad_len * chr(pad_len)
    return text


###################################################################################################
# Entrada: String que representa el texto
# Salida:  String que representa el texto pero sin relleno
# Funcion: Quita el relleno que se le agrego con anterioridad
###################################################################################################
def removePadding(data):
    pad_len = ord(data[-1])
    return data[:-pad_len]


###################################################################################################
# Entrada: Arreglo que representa el bloque y una matriz que representa la tabla de permutaciones
# Salida:  Arreglo con los bits permutados
# Funcion: Realizar la permutacion del bloque usando la tabla correspondiente
###################################################################################################
def permut(block, table):
    return [block[x - 1] for x in table]


###################################################################################################
# Entrada: Lista t1 y Lista t2
# Salida:  Lista resultante al aplicar xor
# Funcion: Realiza un or exclisivo a las listas qque ingresan como parametros
###################################################################################################
def xor(t1, t2):
    return [x ^ y for x, y in zip(t1, t2)]


###################################################################################################
# Entrada: arreglo que representa El lado derecho del bloque expandido
# Salida:  Lista con los bits permutados
# Funcion: Transformar uns string a una lista de bits
###################################################################################################
def substitute(d_e):  # Subtituye los bytes usando para ello SBOX
    subblocks = nsplit(d_e, 6)  # separa el arreglo de bits en sublistas de 6 bits
    result = list()
    for i in range(len(subblocks)):  # Por cada subbloque
        block = subblocks[i]
        row = int(str(block[0]) + str(block[5]), 2)  # Se obtiene la fila con el primer y ultimo bit
        column = int(''.join([str(x) for x in block[1:][:-1]]), 2)  # La columnas son los 2,3,4 y 5 bits
        val = S_BOX[i][row][column]  # Toma el valor de sBox apropiado para la ronda i.
        bin2 = binvalue(val, 4)  # Convierte el valor en binario
        result += [int(x) for x in bin2]  # y se agrega a la lista result
    return result


###################################################################################################
# Entrada: Vacio
# Salida:  Vacio
# Funcion: Metodo que Genera una lista con todas las llaves usadas en la rondas, se guarda en el atributo de la clase
###################################################################################################
def generatekeys(password):
    keys = []
    key = string_to_bit_array(password)
    key = permut(key, CP_1)  # Se aplica la permutacion inicial a la llave
    g, d = nsplit(key, 28)  # Se separa la llave en (g->LEFT),(d->RIGHT)
    for i in range(16):  # Comienzas las 16 rondas
        g, d = shift(g, d, SHIFT[i])  # Aplica el desplazamiento asociado a cada ronda
        tmp = g + d  # Se juntan nuevamente las partes
        keys.append(permut(tmp, CP_2))  # Se aplica la permutacion para obtner las Ki y se guardan el atributo de la clase
    return keys


###################################################################################################
# Entrada: Llave, texto a cifrar, (Encriptar o Desencriptar) y padding
# Salida:  Mensaje cifrado o descifrado
# Funcion: Realiza el proceso de cifrado o descifrado segun la accion que se especifique
###################################################################################################
def run(key, text, action=ENCRYPT):
    if len(key) < 8:
        raise Exception("La llave debe ser al menos de longitud 8 bit")
    elif len(key) > 8:
        key = key[:8]  # Si la llave es mayor a 8 se corta en los 8 primeros bits

    if action == ENCRYPT:
        text = addPadding(text)
    elif len(text) % 8 != 0:  # Si no se especifica el padding en TRUE solo se pueden procesar textos de largo multiplos de 8
        raise Exception("Tamanno del dato debe ser multipĺo de 8")

    keys = generatekeys(key)  # Aqui se generan todas las llaves
    text_blocks = nsplit(text, 8)  # Corta el texto en bloques de 8 bytes (64 bits)
    result = list()
    for bloque in text_blocks:  # For que recorre todos los bloques del texto
        bloque = string_to_bit_array(bloque)  # Convierte el string en un arreglo de bits
        bloque = permut(bloque, PI)  # Se aplica la permutacion inicial
        g, d = nsplit(bloque, 32)  # g(LEFT), d(RIGHT)
        tmp = None
        for i in range(16):  # Aqui se realizan las 16 rondas
            d_e = permut(d, E)  # Se expande d (32 bits) para que coincida con el tamaño de Ki(48bits)
            if action == ENCRYPT:
                tmp = xor(keys[i], d_e)  # Si es para encriptar se usa Ki
            else:
                tmp = xor(keys[15 - i], d_e)  # Si es para desencriptar se usa la ultima llave
            tmp = substitute(tmp)  # Metodo que aplica los SBOXes
            tmp = permut(tmp, P)
            tmp = xor(g, tmp)
            g = d
            d = tmp
        result += permut(d + g, PI_1)  # Hace la ultima permutación y agrega ese resultado en la variable result
    final_res = bit_array_to_string(result)
    if action == DECRYPT:
        return removePadding(final_res)  # Se remueve el padding si se esta descifrando y si padding = True
    else:
        return final_res  # Retorna el string final para el cifrado y descifrado


###################################################################################################
# Metodo run para realizar test de avalancha
#
#
###################################################################################################
def run_test(key, text, n, action=ENCRYPT):
    if len(key) < 8:
        raise Exception("La llave debe ser de longitud 8 bit")
    elif len(key) > 8:
        key = key[:8]  # Si la llave es mayor a 8 se corta en los 8 primeros bits

    if action == ENCRYPT:
        text = addPadding(text)
    elif len(text) % 8 != 0:  # Si no se especifica el padding solo se pueden porcesar textos de largo multiplos de 8
        raise Exception("Tamano del dato debe ser multiĺo de 8")

    keys = generatekeys(key)  # Aqui se generan todas las llaves
    text_blocks = nsplit(text, 8)  # Corta el texto en bloques de 8 bytes (64 bits)
    result = list()
    for bloque in text_blocks:  # For que recorre todos los bloques del texto
        bloque = string_to_bit_array(bloque)  # Convierte el string en un arreglo de bits

        if bloque[n] == 0:  # Se cambia un bit en la posicion n para comprobar el efecto avalancha
            bloque[n] = 1
        else:
            bloque[n] = 0

        # Comienza aca el efecto avalancha
        bloque = permut(bloque, PI)  # Se aplica la permutacion inicial
        g, d = nsplit(bloque, 32)  # g(LEFT), d(RIGHT)
        tmp = None
        for i in range(16):  # Aqui se realizan las 16 rondas
            d_e = permut(d, E)  # Se expande d (32 bits) para que coincida con el tamaño de Ki(48bits)
            if action == ENCRYPT:
                tmp = xor(keys[i], d_e)  # Si es para encriptar se usa Ki
            else:
                tmp = xor(keys[15 - i], d_e)  # Si es para desencriptar se usa la ultima llave
            tmp = substitute(tmp)  # Metodo que aplica los SBOXes
            tmp = permut(tmp, P)
            tmp = xor(g, tmp)
            g = d
            d = tmp
        result += permut(d + g,PI_1)  # Hace la ultima permutación y agrega ese resultado en la variable result
        # Termina el proceso que produce el efecto avalancha
    final_res = bit_array_to_string(result)
    if action == DECRYPT:
        return removePadding(final_res)  # Se remueve el padding si se esta descifrando y si padding = True
    else:
        return final_res  # Retorna el string final para el cifrado y descifrado


###################################################################################################
# Entrada: Llave inicial, texto a cifrar y el relleno que por defecto es falso
# Salida:  Retorna el texto cifrado
# Funcion: Llama el metodo run, que realiza el proceso de cifrado/descifrado
###################################################################################################
def encrypt(key, text):
    return run(key, text, ENCRYPT)


###################################################################################################
# Entrada: Llave inicial, texto cifrado y el relleno que por defecto es falso
# Salida:  Retorna el texto descifrado
# Funcion: Llama el metodo run, que realiza el proceso de cifrado/descifrado
###################################################################################################
def decrypt(key, text):
    return run(key, text, DECRYPT)


###################################################################################################
# Entrada: La Llave inicial, texto a cifrado y descifrar y la posicion del bit a cambiar
# Salida:  Retorna la probabilidad de error al cambiar un solo bit
# Funcion: Llama a la funcion run_test que es para determinar que tanto cambian los bit al realizar el proceso de cifrado cuando se le cambia un bit en la entrada
###################################################################################################
def efecto_avalancha(key, text, n):
    cifrado = encrypt(key, text)
    cifrado2 = run_test(key, text, n, ENCRYPT)

    bin1 = string_to_bit_array(cifrado)
    bin2 = string_to_bit_array(cifrado2)

    errores = 0
    for i in range(len(bin1)):
        if bin1[i] != bin2[i]:
            errores += 1
    prob = errores / len(bin1)
    return prob




def modo():
    #modo simple de encriptación de una sola palabra
    if len(sys.argv) == 4:
        print("Usando instrucciones de la línea de comandos")
        if sys.argv[1]=="0":
            print("Encriptando...")
        elif sys.argv[1]=="1":
            print("Desencriptando...")
        elif sys.argv[1]=="2":
            print("Test de desempeño")
        elif sys.argv[1]=="3":
            print("Comparación")
        m = sys.argv[1]
        key = sys.argv[2]
        text = sys.argv[3]
    else: #Modo interactivo

        print("     _____ _______     _______ _______ ____   _____ ")
        print("    / ____|  __ \ \   / /  __ \__   __/ __ \ / ____|")
        print("   | |    | |__) \ \_/ /| |__) | | | | |  | | (___  ")
        print("   | |    |  _  / \   / |  ___/  | | | |  | |\___ \ ")
        print("   | |____| | \ \  | |  | |      | | | |__| |____) |")
        print("    \_____|_|  \_\ |_|  |_|      |_|  \____/|_____/ ")
        print("")
        print("Modos disponibles: ")
        print("0=>Encriptar, 1=> Desencriptar, 2=>Test de avalancha (texto), 3=> Comparación")
        while True:
            m = input("Ingrese acción a realizar: ")
            key = input("Ingrese password de 8 caracteres: ")
            text  = input("Ingrese texto: ")
            if m=="1" or m=="2" or m=="3" or m=="4" :
                break

    if m == "0":
        cifrado = encrypt(key, text)
        print("Cifrado: %r" % cifrado)
    elif m == "1":
        plano = decrypt(key, text)
        print("Descifrado: ", plano)
    elif m == "2":
        resultado = efecto_avalancha(key, text, 1) # se usa para revisar el efecto avalancha. Cambia el caracter n-ésimo
        print("Porcentaje idéntico: %r" % (resultado*100))
    elif m == "3":
        cifrado = encrypt(key, text)
        plano = decrypt(key, cifrado)
        print("Cifrado: %r" % cifrado)
        print("Descifrado: ", plano)
    else:
        print("Modo incorrecto")
        # print(">%s<" % m)

    return 1


modo()
print("--Fin--")
