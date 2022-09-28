"""
Construir un programa para ir de compras a un supermercado que permita la construcción del siguiente menú:

Digitar 1 para recibir código, nombre y precio de un producto
Digitar 2 para mostrar los productos
Digitar 3 para buscar y editar producto por código
Digitar 4 para buscar y eliminar producto por código 
"""

from math import prod
from time import process_time


opcion = 1
codigo=0
nombre=""
precio=0
compras=[]

while(opcion!=0):
    print("Digitar 1 para recibir {código, nombre, precio} de un producto ")
    print("Digitar 2 para mostrar todos los productos registrados ")
    print(" Digitar 3 para permitir buscar por código un producto y editar el precio de este ")
    print("Digitar 4 para permitir buscar por código un producto y eliminar el producto ")
    print(" Digitar 0 para SALIR ")
    opcion=int(input("Digita una opcion "))
    if(opcion==0):
        break
    elif(opcion==1):
        codigo=int(input("Digite el codigo del producto "))
        nombre=input("Digite el nombre del prducto ")
        precio=int(input("Digita el precio para el producto "))
        producto={'codigo':codigo,'nombre':nombre,'precio':precio}
        compras.append(producto)
    elif(opcion==2):
        print(compras)
    elif(opcion==3):
        buscarCodigo=int(input("digite el codigo que desea buscar: "))
        for indice,producto in enumerate(compras):
            if(buscarCodigo==(producto['codigo'])):
                modificarPrecio=int(input("Digite el nuevo precio"))
                producto['precio']=modificarPrecio
            else:
                print("El codigo ingresado no a sido registrado ")
    elif(opcion==4):
        buscarCodigo=int(input("digite el codigo que desea buscar: "))
        for indice,producto in enumerate(compras):
          if(buscarCodigo==(producto['codigo'])):
                compras.pop(indice)
                print("Se elimino el producto ")
                break
        else:
             print("No se a encontrado el registro")
    else:
        print("Digite un numero valido")

