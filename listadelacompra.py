import os
from datetime import date
from colorama import init, Fore, Style

init(autoreset=True)

# Preguntar nombre
nombre = input(Fore.CYAN + "Dime su nombre para referirme a usted: ")

# Crear lista de la compra
lista = []
print(Fore.YELLOW + "Vaya añadiendo artículos a la lista. Cuando quiera terminar, escriba 'stop'.")

articulo = ""
while articulo.lower() != "stop":
    articulo = input(Fore.GREEN + "Añade artículo a la lista: ")
    if articulo.lower() != "stop":
        lista.append(articulo)

# Mostrar la lista
print(Fore.MAGENTA + "\nLa lista de su compra es la siguiente:")
for i in lista:
    print("- " + i)

# Crear archivo con la fecha de hoy
archivo_dia = str(date.today()) + ".txt"
with open(archivo_dia, "w") as listacompra:
    listacompra.write("La lista de hoy (" + str(date.today()) + ") hecha por " + nombre + ":\n")
    for producto in lista:
        listacompra.write("- " + producto + "\n")

# Preguntar si quiere guardar o borrar
envio = input(Fore.CYAN + "\n¿Quiere guardar la lista de la compra? (si/no): ").lower()

if envio == "no":
    os.remove(archivo_dia)
    print(Fore.RED + "De acuerdo, la lista ha sido borrada de la memoria.")
else:
    print(Fore.GREEN + f"La lista se ha guardado como {archivo_dia}.")

# Ofrecer enviar por email o WhatsApp
enviar_opcion = input(Fore.CYAN + "\n¿Quiere enviar la lista por email o WhatsApp? (email/whatsapp/no): ").lower()

if enviar_opcion == "email":
    print(Fore.BLUE + "Para enviar por email, adjunte el archivo '" + archivo_dia + "' en su aplicación de correo.")
elif enviar_opcion == "whatsapp":
    print(Fore.BLUE + "Para enviar por WhatsApp, comparta el archivo '" + archivo_dia + "' como documento desde su móvil.")
else:
    print(Fore.YELLOW + "De acuerdo, no se enviará.")
    
    
import shutil

# Ruta destino en el móvil
destino = "/sdcard/Download/" + archivo_dia

# Mover el archivo a la carpeta de Descargas
try:
    shutil.move(archivo_dia, destino)
    print(f"\nEl archivo se ha movido a la carpeta de Descargas: {destino}")
except Exception as e:
    print(f"\nError al mover el archivo: {e}")