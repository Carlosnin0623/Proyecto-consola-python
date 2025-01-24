# importando el modulo de usuario

from usuario.usuario import Usuario

from nota.acciones import AccionesNotas

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


   def identificar(self):
     print("Nececitamos verificar tu identidad para trabajar con las notas: ")
     print("Favor introducir los siguientes datos: ")
     email = input("Introduce tu correo electrónico: ")
     password = input("Instroduce tu contraseña: ")

     login = Usuario("","", email, password)

     verificado = login.indentificar()

     if verificado != None:
       print("Genial, el usuario ha sido verificado!!!, podemos continuar... ")
       self.opciones(verificado)
     else:
       print("Lo siento, el usuario no ha podido ser verificado, prueba otra vez!!!")

     

   def opciones(self, usuario):
     print("Saludos, !! Ahora camos a trabajar con las notas: ")
     print(
       """

         (crear) Crear una nota
         (mostrar) Ver mis notas
         (borrar) Borrar nota

       """)
     
     opcion = input("Que deseas hacer?: ")

     if opcion == 'crear':
        resultado = AccionesNotas()
        resultado.crearNotas(usuario)


     

      


