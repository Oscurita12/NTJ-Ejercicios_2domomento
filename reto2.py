""" El valle de aburra afronta altas temperaturas año tras año, Cree una función que permita calcular la temperatura media de la tierra partir de recibir 20 datos diarios de temperatura. """

def calcularTemperatura():
    dias=[]
    temperatura=0
    for i in range(0,5,1):
        dia=int(input("Digite la temperatura: "))
        dias.insert(i,dia)
    """ for dia in range(0,len(dias),1):
        temperatura=temperatura+dia
    print(f'La media de la temperatra es {(temperatura)/5}') """
    
    mean = sum(dias) / len(dias)
    print(f'La media de la temperatura es: {mean}')
calcularTemperatura()