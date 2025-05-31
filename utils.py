from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os

# Parámetros del algoritmo
TAMANIO_SAL = 16
TAMANIO_IV = 16
ITERACIONES_KDF = 100_000

def derivar_clave(clave: str, sal: bytes) -> bytes:
    """
    Deriva una clave de 256 bits a partir de una contraseña utilizando PBKDF2.

    :param clave: Contraseña ingresada por el usuario
    :param sal: Sal aleatoria para fortalecer la derivación
    :return: Clave derivada de 32 bytes
    """
    return PBKDF2(clave, sal, dkLen=32, count=ITERACIONES_KDF)

def cifrar_archivo(ruta_entrada: str, ruta_salida: str, clave: str):
    """
    Cifra el contenido de un archivo usando AES-256 en modo CBC.

    :param ruta_entrada: Ruta del archivo original
    :param ruta_salida: Ruta donde se guardará el archivo cifrado
    :param clave: Contraseña utilizada para derivar la clave AES
    """
    sal = get_random_bytes(TAMANIO_SAL)
    iv = get_random_bytes(TAMANIO_IV)
    clave_256 = derivar_clave(clave, sal)

    with open(ruta_entrada, "rb") as f:
        datos = f.read()

    # Relleno los ultimos 16bits - un error que no encontraba y me tiro esta solucion
    padding = AES.block_size - len(datos) % AES.block_size
    datos += bytes([padding]) * padding

    cipher = AES.new(clave_256, AES.MODE_CBC, iv)
    datos_cifrados = cipher.encrypt(datos)

    with open(ruta_salida, "wb") as f:
        f.write(sal + iv + datos_cifrados)

def descifrar_archivo(ruta_entrada: str, ruta_salida: str, clave: str):
    """
    Descifra un archivo previamente cifrado con AES-256 en modo CBC.

    :param ruta_entrada: Ruta del archivo cifrado
    :param ruta_salida: Ruta donde se guardará el archivo descifrado
    :param clave: Contraseña usada originalmente para cifrar
    """
    with open(ruta_entrada, "rb") as f:
        contenido = f.read()

    sal = contenido[:TAMANIO_SAL]
    iv = contenido[TAMANIO_SAL:TAMANIO_SAL+TAMANIO_IV]
    datos_cifrados = contenido[TAMANIO_SAL+TAMANIO_IV:]

    clave_256 = derivar_clave(clave, sal)
    cipher = AES.new(clave_256, AES.MODE_CBC, iv)
    datos = cipher.decrypt(datos_cifrados)

    # Quitar padding
    padding = datos[-1]
    datos = datos[:-padding]

    with open(ruta_salida, "wb") as f:
        f.write(datos)
