import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from utils import cifrar_archivo, descifrar_archivo

def seleccionar_y_cifrar():
    ruta_archivo = filedialog.askopenfilename(title="Selecciona un archivo para cifrar")
    if not ruta_archivo:
        return

    while True:
        clave = simpledialog.askstring("Clave", "Introduce una clave (mínimo 32 caracteres):", show='*')
        if clave and len(clave) >= 32:
            break
        messagebox.showerror("Error", "La clave debe tener al menos 32 caracteres.")

    directorio, nombre = os.path.split(ruta_archivo)
    ruta_salida = os.path.join(directorio, nombre + ".enc")

    try:
        cifrar_archivo(ruta_archivo, ruta_salida, clave)
        messagebox.showinfo("Éxito", f"Archivo cifrado correctamente:\n{ruta_salida}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al cifrar el archivo:\n{str(e)}")


def seleccionar_y_descifrar():
    ruta_archivo = filedialog.askopenfilename(title="Selecciona un archivo para descifrar", filetypes=[("Archivos cifrados", "*.enc")])
    if not ruta_archivo:
        return

    while True:
        clave = simpledialog.askstring("Clave", "Introduce la clave original:", show='*')
        if clave and len(clave) >= 32:
            break
        messagebox.showerror("Error", "La clave debe tener al menos 32 caracteres.")

    directorio, nombre = os.path.split(ruta_archivo)
    nombre_original = nombre_original = "Desencriptado_" + (nombre[:-4] if nombre.endswith(".enc") else nombre) 
    ruta_salida = os.path.join(directorio, nombre_original)

    try:
        descifrar_archivo(ruta_archivo, ruta_salida, clave)
        messagebox.showinfo("Éxito", f"Archivo descifrado correctamente:\n{ruta_salida}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al descifrar el archivo:\n{str(e)}")


def main():
    root = tk.Tk()
    root.title("Cifrador/Descifrador AES-256")
    root.geometry("400x200")
    root.resizable(False, False)
    root.configure(bg="#1e1e1e")  # fondo oscuro

    # Cargar íconos (asegurate de tener estos PNGs en la carpeta)
    icon_cifrar = tk.PhotoImage(file="lock_closed.png")
    icon_descifrar = tk.PhotoImage(file="lock_open.png")

    # Crear botones oscuros
    btnCifrado = tk.Button(
        root,
        text="  Cifrar archivo",
        image=icon_cifrar,
        compound="left",
        font=("Segoe UI", 11, "bold"),
        bg="#333333",
        fg="white",
        activebackground="#555555",
        activeforeground="white",
        padx=10,
        pady=10,
        command=seleccionar_y_cifrar
    )
    btnCifrado.pack(expand=True, fill='x', padx=20, pady=10)

    btnDescrifrado = tk.Button(
        root,
        text="  Descifrar archivo",
        image=icon_descifrar,
        compound="left",
        font=("Segoe UI", 11, "bold"),
        bg="#333333",
        fg="white",
        activebackground="#555555",
        activeforeground="white",
        padx=10,
        pady=10,
        command=seleccionar_y_descifrar
    )
    btnDescrifrado.pack(expand=True, fill='x', padx=20, pady=5)

    # Mantener referencia a las imágenes para que no se borren
    btnCifrado.image = icon_cifrar
    btnDescrifrado.image = icon_descifrar

    root.mainloop()

if __name__ == "__main__":
    main()
