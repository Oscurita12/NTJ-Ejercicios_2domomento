""" Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “admin” y la contraseña es “admin123*”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
"""
from calendar import c


def Login(user,passw):
    Usuario="admin"
    Contrasena="admin123*"
    
    
    if (Usuario==user and Contrasena==passw):
        return 1


cualquiera=True
intentos=0
while (cualquiera):
    intentos+=1
    usuario=input("Digite su usuario: ")
    contrasena=input("Digite su contraseña: ")
    loqueustedquiera=Login(usuario,contrasena)
    if(loqueustedquiera==1):
        print(f'El usuario es correcto, los intentos fueron: {intentos}')
        cualquiera=False
    
