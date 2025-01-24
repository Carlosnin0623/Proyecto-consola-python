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


class Nota:




    def __init__(self, usuario_id, titulo,descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion


    def insertarNota(self):
        sql = "INSERT INTO notas (id, usuario_id, titulo, descripcion, fechaCreacion) VALUES (null,%s,%s,%s,%s)"
        nota = (self.usuario_id, self.titulo, self.descripcion, fechaFormateada)
        
        try:
         cursorprincipal.execute(sql, nota)
         conexion.commit()

         resultado = [cursorprincipal.rowcount, self]

        except Error as e:
         print(f"Ha ocurrido un error: {e}")
         resultado = [0, self]

        return resultado
           

