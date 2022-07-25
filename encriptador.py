from sqlalchemy import null


def encriptar(texto):
    print(f'El texto a encriptar es: ${texto}')
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return(textoFinal)

def desencriptar(texto):
    print('El texto a desencriptar es: ' + texto)
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textoFinal += chr(ascii)
    return(textoFinal)



def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()


respuestaEoD = input ('Presione "E" para encriptar un arcivo, o "D" para desencriptar: ')
rutaArchivo = input ('Ingrese la ruta del archivo: ')
 
if respuestaEoD == 'E' or respuestaEoD == 'e':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)