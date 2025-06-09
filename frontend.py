import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from utils import cifrar_archivo, descifrar_archivo

def seleccionar_y_cifrar():
    # Seleccionar archivo
    ruta_archivo = filedialog.askopenfilename(title="Selecciona un archivo para cifrar")
    if not ruta_archivo:
        return

    # Pedir clave
    clave = simpledialog.askstring("Clave", "Introduce una clave (mínimo 32 caracteres):", show='*')
    if not clave or len(clave) < 32:
        messagebox.showerror("Error", "La clave debe tener al menos 32 caracteres.")
        return

    # Ruta del archivo cifrado (mismo directorio, con extensión .enc)
    directorio, nombre = os.path.split(ruta_archivo)
    ruta_salida = os.path.join(directorio, nombre + ".enc")

    try:
        cifrar_archivo(ruta_archivo, ruta_salida, clave)
        messagebox.showinfo("Éxito", f"Archivo cifrado correctamente:\n{ruta_salida}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al cifrar el archivo:\n{str(e)}")


def seleccionar_y_descifrar():
    # Seleccionar archivo .enc
    ruta_archivo = filedialog.askopenfilename(title="Selecciona un archivo para descifrar", filetypes=[("Archivos cifrados", "*.enc")])
    if not ruta_archivo:
        return

    # Pedir clave
    clave = simpledialog.askstring("Clave", "Introduce la clave original:", show='*')
    if not clave:
        messagebox.showerror("Error", "Debes introducir una clave.")
        return

    # Ruta del archivo descifrado (mismo directorio, sin extensión .enc)
    directorio, nombre = os.path.split(ruta_archivo)
    
    if nombre.endswith(".enc"):
        nombre_original = nombre[:-4]
    else:
        nombre_original = nombre + ".decrypted" 
    
    ruta_salida = os.path.join(directorio, nombre_original)

    try:
        descifrar_archivo(ruta_archivo, ruta_salida, clave)
        messagebox.showinfo("Éxito", f"Archivo descifrado correctamente:\n{ruta_salida}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al descifrar el archivo:\n{str(e)}")


def main():
    root = tk.Tk()
    root.title("Cifrador/Descifrador AES-256")
    root.geometry("350x150") 
    root.resizable(False, False)

    btnCifrado = tk.Button(root, text="Seleccionar archivo para CIFRAR", command=seleccionar_y_cifrar, padx=10, pady=10)
    btnCifrado.pack(expand=True, fill='x', padx=20, pady=5)

    btnDescrifrado = tk.Button(root, text="Seleccionar archivo para DESCIFRAR", command=seleccionar_y_descifrar, padx=10, pady=10)
    btnDescrifrado.pack(expand=True, fill='x', padx=20, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()