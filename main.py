
#llamar a tu modulo de acciones

from usuario.acciones import Acciones

print("\n ######################## Verificar Notas #################################")

print("¿Que deseas hacer?: ")
opcion = input(
     """
       (crear) Crear un nuevo usuario
       (login) Logueate para ver tus notas
       (salir) Salir del programa
     """ + "\n")
if opcion == "crear":
   resultado =  Acciones()
   resultado.registrar_usuario()
elif opcion == "login":
    True
elif opcion == "salir":
    exit()

