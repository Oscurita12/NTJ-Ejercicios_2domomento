""" Crea una función  que reciba una lista con valores numéricos y devuelva el valor máximo y el mínimo ingresados
"""

def ponerNumero():
    
    numeros=[]
    for i in range(0,4,1):
        numero=int(input("Digite un número: "))
        numeros.insert(i,numero)
    """ print(numeros) """
    numeroMax=max(numeros)
    numeroMin=min(numeros)

    print(f'El número máximo es: {numeroMax} y el número mínimo es: {numeroMin}')


ponerNumero()

