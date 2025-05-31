import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from utils import cifrar_archivo

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

def main():
    root = tk.Tk()
    root.title("Cifrador AES-256")
    root.geometry("300x150")
    root.resizable(False, False)

    btn = tk.Button(root, text="Seleccionar archivo para cifrar", command=seleccionar_y_cifrar, padx=10, pady=10)
    btn.pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
