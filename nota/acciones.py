from nota.nota import Nota

class AccionesNotas:

    def crearNotas(self, usuario):
        print(f"De acuerdo {usuario[1]} vamos a tus notas!!!")
        titulo = input("Ingresa el titulo de tu nota: ")
        descripcion = input("Ingresa una descripcion: ")

        crearNota = Nota(usuario[0], titulo, descripcion)

        nota = crearNota.insertarNota()

        verificado = nota[0]
        
        if verificado >= 1:
            print(f"Enhorabuena {usuario[0]} haz creado una nota")
        else: 
            print(f"Lo siento {usuario[0]} no fue posible crear tu nota, intentalo de nuevo....")

