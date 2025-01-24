# Importar la conexion de la base de datos

from conexion.DB import *

conexion = database
cursorprincipal = cursor

# ahora debemos usar el modulo haslib que es un paquete para cifrar claves para el usuario

import hashlib

# ahora necesitamos el modulo de fechas

from datetime import datetime

ObtenerFecha = datetime.now()
fechaFormateada = ObtenerFecha.strftime("%Y-%m-%d")

class Usuario:



    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    
    def registrar(self):

        # cifrar contraseña con haslib

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios (id, nombre, apellido, email, password, fechaCreacion) VALUES (null,%s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fechaFormateada)

        try:
         cursorprincipal.execute(sql, usuario)
         conexion.commit()

         resultado = [cursorprincipal.rowcount, self]
        except Error as e:
         print(f"Error al insertar usuario: {e}")  # Mostrar el error exacto
         resultado = [0, self]

        return resultado
    

    def indentificar(self):
       
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
       
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        params = (self.email, cifrado.hexdigest())

        try:
         cursorprincipal.execute(sql, params)

         resultado = cursorprincipal.fetchone()

        except:
           
         resultado = None

        return resultado
           


           


        
    


        

        