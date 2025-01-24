# importando el modulo de usuario

from usuario.usuario import Usuario

class Acciones:

   def registrar_usuario(self):
      
      print("\n Hola necesitas registrate para poder ver tus notas !!!:")
      nombre = input("Digita tu nombre: ")
      apellidos = input("Digita tus apellidos: ")
      email = input("Pon aquí tu correo electrónico: ")
      password = input("Ingresa tu contraseña: ")

      registro = Usuario(nombre, apellidos, email, password)

      resultado = registro.registrar()

      insertado = resultado[0]
      usuario = resultado[1]
      
      try:
       if insertado >= 1:
         
        print(f"Felicidades el usuario {usuario.nombre} ha sido registrado exitosamente con el correo {usuario.email} !!!")

      except Exception as e:

        print("Lo siento el usuario no pudo ser creado se produjo un error")
        print(type(e).__name__)

      


