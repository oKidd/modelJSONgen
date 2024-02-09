import json
import os
import tkinter as tk
from tkinter import filedialog


def modificar_json(model_id, nombre_mueble, nombre_material, nombre_archivo, route, textura_json):
    # Abre el archivo main.json
    with open(nombre_archivo, "r") as archivo:
        data = json.load(archivo)
        
    model_id = int(model_id)

    # Lista de colores
    lista_colores = ["white", "light_gray", "gray", "black", "brown", "red", "orange", "yellow", "lime", "green", "cyan", "light_blue", "blue", "purple", "magenta", "pink"]

    # Lista para almacenar las líneas modificadas
    lineas_modificadas = []
    
    if not os.path.exists("exports"):
        os.makedirs("exports")

    for color in lista_colores:
        # Modifica la línea en el archivo JSON
        data["textures"][f"{textura_json}"] = f'block/{color}_{nombre_material}'

        # Crea el nombre del archivo exportado
        nombre_exportado = f"exports/{nombre_mueble}_{color}.json"

        # Crea y guarda el nuevo archivo JSON
        with open(nombre_exportado, "w") as archivo_exportado:
            json.dump(data, archivo_exportado, indent=2)

        print(f"Archivo {nombre_exportado} creado con éxito.")

        # Genera las líneas adicionales y las guarda en la lista
        lineas_modificadas.append({
            "predicate": {
                "custom_model_data": model_id
            },
            "model": f"{route}/{nombre_mueble}_{color}"
        })

        # Incrementa el ID del modelo
        model_id += 1

    # Al final del ciclo, guarda las líneas en un archivo item_frame.json
    with open("item_frame.json", "w") as archivo_item_frame:
        json.dump(lineas_modificadas, archivo_item_frame, indent=2)

    print("Archivo item_frame.json creado con éxito.")




def generar_modelos():
    # Obtener los valores de los campos de texto
    nombre_modelo = entry_nombre_modelo.get()
    numero_modelo = entry_numero_modelo.get()
    nombre_material = entry_nombre_material.get()
    nombre_archivo = entry_nombre_archivo.get()
    ruta_archivo = entry_ruta_archivo.get()
    textura_json = entry_textura_json.get()

    # Validar los campos de texto
    if not nombre_modelo or not numero_modelo or not nombre_material or not nombre_archivo or not ruta_archivo or not textura_json:
        label_mensaje["text"] = "Debe completar todos los campos."
        return

    # Ejecutar el código
    modificar_json(numero_modelo, nombre_modelo, nombre_material, nombre_archivo, ruta_archivo, textura_json)

    # Mostrar mensaje de éxito
    label_mensaje["text"] = "Archivos JSON creados con éxito."


def seleccionar_archivo():
    # Abrir una ventana para seleccionar el archivo JSON original
    archivo = filedialog.askopenfilename(title="Seleccionar archivo JSON", filetypes=[("Archivos JSON", "*.json")])

    # Si se seleccionó un archivo, actualizar el campo de texto
    if archivo:
        entry_nombre_archivo.delete(0, tk.END)
        entry_nombre_archivo.insert(0, archivo)
        


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("JSONgenV3")

# Agregar los widgets
label_nombre_modelo = tk.Label(text="Nombre mueble:")
entry_nombre_modelo = tk.Entry()

label_numero_modelo = tk.Label(text="Id inicial modelo:")
entry_numero_modelo = tk.Entry()

label_nombre_material = tk.Label(text="Nombre material: (sin color)")
entry_nombre_material = tk.Entry()

label_nombre_archivo = tk.Label(text="Archivo modelo: (.json)")
entry_nombre_archivo = tk.Entry()

boton_seleccionar_archivo = tk.Button(text="...", command=seleccionar_archivo)

label_ruta_archivo = tk.Label(text="Ruta modelo: (pack route)")
entry_ruta_archivo = tk.Entry()

label_textura_json = tk.Label(text="Textura JSON: (""nombre"")")
entry_textura_json = tk.Entry()

boton_generar = tk.Button(text="Generar Modelos", command=generar_modelos)

label_mensaje = tk.Label()

# Diseño de la interfaz
label_nombre_modelo.grid(row=0, column=0)
entry_nombre_modelo.grid(row=0, column=1)

label_numero_modelo.grid(row=1, column=0)
entry_numero_modelo.grid(row=1, column=1)

label_nombre_material.grid(row=2, column=0)
entry_nombre_material.grid(row=2, column=1)

label_nombre_archivo.grid(row=3, column=0)
entry_nombre_archivo.grid(row=3, column=1)
boton_seleccionar_archivo.grid(row=3, column=2)

label_ruta_archivo.grid(row=4, column=0)
entry_ruta_archivo.grid(row=4, column=1)

label_textura_json.grid(row=5, column=0)
entry_textura_json.grid(row=5, column=1)

boton_generar.grid(row=7, column=0, columnspan=2, sticky="ew")

label_mensaje.grid(row=6, column=0, columnspan=2, sticky="ew")

# Agregar estilos a la interfaz
ventana.configure(bg="#131313")

label_nombre_modelo.configure(bg="#131313", fg="#fff", font=("Arial", 14))
entry_nombre_modelo.configure(bg="#ffffff", fg="#333333", font=("Arial", 14), bd=1, relief="solid")

label_numero_modelo.configure(bg="#131313", fg="#fff", font=("Arial", 14))
entry_numero_modelo.configure(bg="#ffffff", fg="#333333", font=("Arial", 14), bd=1, relief="solid")

label_nombre_material.configure(bg="#131313", fg="#fff", font=("Arial", 14))
entry_nombre_material.configure(bg="#ffffff", fg="#333333", font=("Arial", 14), bd=1, relief="solid")

label_nombre_archivo.configure(bg="#131313", fg="#fff", font=("Arial", 14))
entry_nombre_archivo.configure(bg="#ffffff", fg="#333333", font=("Arial", 14), bd=1, relief="solid")
boton_seleccionar_archivo.configure(bg="#ffffff", fg="#333333", font=("Arial", 10), bd=0, relief="solid")

label_ruta_archivo.configure(bg="#131313", fg="#fff", font=("Arial", 14))
entry_ruta_archivo.configure(bg="#ffffff", fg="#333333", font=("Arial", 14), bd=1, relief="solid")

label_textura_json.configure(bg="#131313", fg="#fff", font=("Arial", 14))
entry_textura_json.configure(bg="#ffffff", fg="#333333", font=("Arial", 14), bd=1, relief="solid")

boton_generar.configure(bg="#4bb34d", fg="#ffffff", font=("Arial", 14), bd=0)

label_mensaje.configure(bg="#131313", fg="#ff4f4f", font=("Arial", 14))

# Iniciar la ventana principal
ventana.mainloop()
