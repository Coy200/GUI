import tkinter as tk  # Importación de tkinter
import serial
import time

# Inicialización de la ventana principal
ventana = tk.Tk()
ventana.title("Comunicación con ESP32")  # Título de la ventana

# Configuración del puerto por defecto
PUERTO = "COM5"
arduino = serial.Serial(port=PUERTO, baudrate=115200, timeout=.1)

# Etiqueta para mostrar mensajes de conexión
etiqueta_aviso = tk.Label(ventana, text="", fg="red")

def CONECTAR():
    global PUERTO
    print("Función conectar")
    PUERTO = EntryCOM.get()
    
    try:
        arduino.port = PUERTO
        arduino.open()  # Abre el puerto
        print(f"Conectado a {PUERTO}")
        etiqueta_aviso.config(text="Conectado correctamente a " + PUERTO, fg="green")
    except Exception as e:
        print(f"Error al conectar: {e}")
        etiqueta_aviso.config(text="¡Conexión incorrecta! Verifica el puerto.", fg="red")

def SEND():
    global PUERTO
    print("Función ENVIO DE DATOS")
    x = SpinDATA.get()
    
    # Enviar el número al ESP32
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)  # Espera para asegurar que los datos se envíen correctamente
    
    # Leer la respuesta del ESP32
    data = arduino.readline().decode('utf-8').strip()  # Eliminar espacios en blanco y saltos de línea
    LabelRECIVE.config(text="Resultado recibido: " + data)  # Mostrar el resultado en la etiqueta

def CERRAR():
    print("Cerrar")
    arduino.close()  # Cerrar el puerto serial
    ventana.destroy()  # Cerrar la ventana

# Instancia de los objetos de la interfaz gráfica
LabelCOM_NAME = tk.Label(ventana, text="Escribe el nombre del puerto; ejem: COM2")
EntryCOM = tk.Entry(ventana)
BotonCONECT = tk.Button(ventana, text="CONECTAR", command=CONECTAR)  # Sin paréntesis
SpinDATA = tk.Spinbox(ventana, from_=0, to=500)  # Selector numérico para enviar datos
BotonSEND = tk.Button(ventana, text="ENVIAR", command=SEND)  # Sin paréntesis
LabelRECIVE = tk.Label(ventana, text="Resultado recibido:")
BotonCerrar = tk.Button(ventana, text="SALIR", command=CERRAR)

# Incrustación en VENTANA con formato adecuado
LabelCOM_NAME.pack(padx=10, pady=5)
EntryCOM.pack(padx=10, pady=5)
BotonCONECT.pack(padx=10, pady=5)
SpinDATA.pack(padx=10, pady=5)
BotonSEND.pack(padx=10, pady=5)
LabelRECIVE.pack(padx=10, pady=5)
etiqueta_aviso.pack(padx=10, pady=5)  # Añadir la etiqueta de aviso
BotonCerrar.pack(padx=10, pady=5)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()