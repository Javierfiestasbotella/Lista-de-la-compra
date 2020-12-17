import os
import io
from datetime import datetime
from colorama import init, Fore, Back, Style
from datetime import date

nombre=input("dime su nombre para referirme a usted: ")
lista=[]
articulo=""
while articulo!="stop":
  articulo=input("añade articulo a la lista: ")
  lista.append(articulo)
lista.pop()
print ("la lista de su compra es la siguiente: ")
archivo_dia=date.today()
for i in lista:
  print(i)
listacompra=open(str(archivo_dia),"w")
listacompra.write("\n la lista de hoy "+str(archivo_dia)+" y echa por " +nombre+": ")
envio=input("¿quiere guardar la lista de la compra? ")
if envio=="si":
  listacompra=open(str(archivo_dia),"a")
  for productos in lista:
    listacompra.write("\n"+productos)
else:
  print("de acuerdo la borro de la memoria")
  os.remove(str(archivo_dia))
