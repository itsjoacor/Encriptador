from utils import cifrar_archivo, descifrar_archivo
import argparse

def main():
    parser = argparse.ArgumentParser(description="Cifrar o descifrar un archivo usando AES-256.")
    parser.add_argument("modo", choices=["cifrar", "descifrar"], help="Modo de operación")
    parser.add_argument("archivo_entrada", help="Ruta al archivo de entrada")
    parser.add_argument("archivo_salida", help="Ruta al archivo de salida")
    parser.add_argument("clave", help="Clave secreta (mínimo 32 caracteres para AES-256)")

    args = parser.parse_args()

    if args.modo == "cifrar":
        cifrar_archivo(args.archivo_entrada, args.archivo_salida, args.clave)
        print("Archivo cifrado exitosamente.")
    elif args.modo == "descifrar":
        descifrar_archivo(args.archivo_entrada, args.archivo_salida, args.clave)
        print("Archivo descifrado exitosamente.")

if __name__ == "__main__":
    main()
