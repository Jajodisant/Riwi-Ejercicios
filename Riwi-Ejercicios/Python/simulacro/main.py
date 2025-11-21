


role = input("ingrese el tipo de Rol: ")
username = input("ingresar el nombre de usuario")
passwordUser = input("Ingrese la contraseña de usuario: ")

try:

    if role == "admin":
        print("mostrar al admin")

    elif role == "user":
        print("mostrar al usuario")
    else:
        print("perfil no existe")
except:
    print("ingreso de información erronea")