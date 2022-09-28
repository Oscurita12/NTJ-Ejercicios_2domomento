"""
El banco de hierro de la isla de Braavos necesita de sus servicios para programar un software que permita:

Almacenar información de un cliente (nombre,apellido,cedula)
Almacenar información de la cuenta (numeroCuenta, saldo)
Se debe permitir consultar saldo en cualquier momento
Se debe permitir ingresar o retirar dinero  cuando se desee
"""

from math import prod
from time import process_time


opcion = 1
codigo=0
nombre=""
precio=0
personas=[]
cuentas=[]
while(opcion!=0):
    print("Digitar 1 para Almacenar información de un cliente (nombre,apellido,cedula): ")
    print("Digitar 2 Almacenar información de la cuenta (numeroCuenta, saldo): ")
    print(" Digitar 3 para permitir consultar saldo en cualquier momento: ")
    print("Digitar 4 para permitir ingresar o retirar dinero  cuando se desee: ")
    print(" Digitar 0 para SALIR ")
    opcion=int(input("Digita una opcion "))
    if(opcion==0):
        break
    elif(opcion==1):
        cedula=int(input("Digite la cedula de la persona "))
        nombre=input("Digite el nombre de la personas ")
        apellido=input("Digita el apellido de la persona ")
        persona={'cedula':cedula,'nombre':nombre,'apellido':apellido}
        personas.append(persona)
    elif(opcion==2):
        numeroCuenta=int(input("Digite el número de la cuenta"))
        saldo=int(input("Digite el saldo de la cuenta"))
        cuenta={'numeroCuenta':numeroCuenta, 'saldo':saldo}
        cuentas.append(cuenta)
    elif(opcion==3):
        buscarCodigo=int(input("digite el numero de la cuenta que desea buscar: "))
        for indice,cuenta in enumerate(cuentas):
            if(buscarCodigo==(cuenta['numeroCuenta'])):
                saldo=cuenta['saldo']
                print(f'El saldo de la cuenta {buscarCodigo} es: {saldo}')
            else:
                print("El numero de cuenta no se encuentra ")
    elif(opcion==4):
        eleccion=int(input("Digite 1 para ingresar, digite 2 para sacar: "))
        if(eleccion==1):

            buscarCodigo=int(input("digite la cuenta que desea buscar: "))
            for indice,cuenta in enumerate(cuentas):
                if(buscarCodigo==(cuenta['numeroCuenta'])):
                    nuevosaldo=int(input("Digite cuanto quiere ingresar: "))

                    saldo=cuenta['saldo']
                    calculo=saldo+nuevosaldo
                    cuenta['saldo']=calculo
                    print(f'El nuevo saldo de la cuenta {buscarCodigo} es: {calculo}')
                else:
                    print("El numero de cuenta no se encuentra ")
        elif(eleccion==2):
            buscarCodigo=int(input("digite la cuenta que desea buscar: "))
            for indice,cuenta in enumerate(cuentas):
                if(buscarCodigo==(cuenta['numeroCuenta'])):
                    nuevosaldo=int(input("Digite cuanto quiere retirar: "))

                    saldo=cuenta['saldo']
                    calculo=saldo-nuevosaldo
                    cuenta['saldo']=calculo
                    print(f'El nuevo saldo de la cuenta {buscarCodigo} es: {calculo}')
                else:
                    print("El numero de cuenta no se encuentra ")
        else:
            print("Elección no válida")
    else:
        print("Digite un numero valido")
