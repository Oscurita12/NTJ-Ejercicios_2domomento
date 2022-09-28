x = int(input("Digite un número: "))
numero = lambda num: num%2

if(numero(x) !=0):
    print(f'El numero es impar {x}')
else:
    print(f'El numero es par {x}')