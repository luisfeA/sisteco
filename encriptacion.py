def encriptar(texto):
    abc = "abcdefghijklmnñopqrstuvwxyz"
    abcM = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedarioMinus=list(abc)
    abecedarioMayus=list(abcM)

    key = 0
    archivo = open("decrypt.txt", "w")

    while key < 27:
        output = ""
        for letra in texto:
            if letra in abecedarioMinus:
                output = output + abecedarioMinus[(abecedarioMinus.index(letra)+key) % 27]
            elif letra in abecedarioMayus:
                output = output + abecedarioMayus[(abecedarioMayus.index(letra)+key) % 27]
            else:
                output = output + letra
        archivo.write("key: "+str(key))
        archivo.write("\n")
        archivo.write(output)
        archivo.write("\n")
        archivo.write("-----------------------------------------------------------------------")
        archivo.write("\n")

        key += 1
    archivo.close()


encriptar("weap pa kcxre pakbce gkt lxce weñ")