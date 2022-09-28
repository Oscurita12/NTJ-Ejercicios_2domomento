"""
Escriba un programa que pida el ancho y largo de un rectángulo y permita calcular:
-Área
-Perímetro
-Graficar el rectángulo

Ejemplo: Ancho=5 Altura=3

* * * * *
* * * * *
* * * * *
"""

def Figuras():

    alto=int(input("Digite el lado de la figura: "))
    ancho=int(input("Digite el ancho de la figura: "))
    area=alto*ancho
    perimetro=(alto*2)+(ancho*2)

    print(f'El area del rectangulo es {area}')
    print(f'El perimetro del rectangulo es {perimetro}')

    for i in range(1,alto+1): #ciclo for de los renglones
        for j in range(1,ancho+1):# ciclo for de las columnas
            print("*",end = "")
        print(" ")

Figuras()