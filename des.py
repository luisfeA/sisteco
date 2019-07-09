from Crypto.Cipher import DES
from Crypto.Hash import SHA256
# Como usamos DES, los bloques son de 8 caracteres.
# Rellenamos con espacios (que habra que eliminar al descifrar).


print("######## DES normal ##########")
print("Ingrese texto a cifrar: ")
texto = input()
largo = len(texto)
#print("Largo: ",largo)
resto = 0
if largo%8 != 0:
    resto = 8-largo%8
    for i in range(resto):
        texto = texto + " "

#print(texto)
newLargo = len(texto)
#print("Largo nuevo: ",newLargo)
# creamos el cifrador con DES
cipher = DES.new('12345678')
c_texto = cipher.encrypt(texto)
# ciframos texto
print("El cliente envia: ", c_texto)

# desciframos mensajes y quitamos espacios
decipher = DES.new('12345678')
if resto == 0:
    d_texto = decipher.decrypt(c_texto)[:]
else:
    d_texto = decipher.decrypt(c_texto)[:-resto]

#decode del texto descifrado
new_texto = d_texto.decode('UTF-8')
print("El servidor descifra:", new_texto)
#print("Largo des: ",len(d_texto))



##### Triple DES #########
print("######## Triple DES ##########")

#Se crean las dos llaves para el triple DES
key1 = "12345678"
key2 = "87654321"

#Se inicializa el objeto HASH
hash = SHA256.new()

#Se ingresa el texto a cifrar
print("Ingrese texto a cifrar: ")
texto = input()
largo = len(texto)

#print("Largo: ",largo)
#En caso de que el texto no sea multiplo de 8, se le agregan espacios para que lo sea
resto = 0
if largo%8 != 0:
    resto = 8-largo%8
    for i in range(resto):
        texto = texto + " "


#print(texto)
newLargo = len(texto)
#print("Largo nuevo: ",newLargo)

#Se instancias los cifradores y descifradores para cada llave
cipher1 = DES.new(key1)
cipher2 = DES.new(key2)
decipher1 = DES.new(key1)
decipher2 = DES.new(key2)

#Se cifra el texto 3 veces
c1_texto = cipher1.encrypt(texto)
c2_texto = cipher2.encrypt(c1_texto)
c3_texto = cipher1.encrypt(c2_texto)

#Se crea un valor HASH en base al texto original
hash.update(texto.encode('UTF-8'))
c3_texto = c3_texto + hash.digest()
print("Cliente envia +  hash: ", c3_texto)

#Se inicializa el objeto HASH
hash2 = SHA256.new()

#Se extrae el HASH enviado por el cliente
hashTexto = c3_texto[len(c3_texto)-32:]
#Se extrae el mensaje cifrado enviado por el cliente
c3_texto = c3_texto[:len(c3_texto)-32]

#Se descifra el mensaje
d1_texto = decipher1.decrypt(c3_texto)
d2_texto = decipher2.decrypt(d1_texto)
d3_texto = decipher1.decrypt(d2_texto)

#Se obtiene un valor HASH del mensaje descifrado
hash2.update(d3_texto)

print("Hash cifrado: ",hashTexto)
print("Hash descifrado: ",hash2.digest())

if hashTexto == hash2.digest():
    print("Mensaje no modificado")
else:
    print("Mensaje modificado")

finalTexto = d3_texto.decode('UTF-8')
print("El servidor descifra: ",finalTexto)
