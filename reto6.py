"""
Construir un programa para calcular un programa CALCULADORA que permita calcular
SUMA
RESTA
MULTIPLICACIÓN
DIVISIÓN
"""

def opera1(operador, a, b):
    if operador == 'suma':
        return a + b
    elif operador == 'resta':
        return a - b
    elif operador == 'multiplica':
        return a * b
    elif operador == 'divide':
        return a / b
    else:
        return None
    

a=int(input("Ingrese un número: "))
b=int(input("Ingrese otro número: "))

operacionresultado=input('Seleccione una opcion: suma, resta, multiplica o divide: ')

resultado=opera1(operacionresultado,a,b)
print(f'El resultado de la operacion es {resultado}')


    