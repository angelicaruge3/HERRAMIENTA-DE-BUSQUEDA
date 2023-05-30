import json
import mysql.connector

#Diccionario con datos
base_datos = {
    "host" : "localhost",
    "user" : "root",
    "password" : "",
    "database" : "looking_for_adventures",
    "port" : 3306
}
#imprimir 
print(base_datos)
#escribir
archivo = open("bd.json", "w")
#Guardar json
json.dump(base_datos,archivo)
#Cerrar archivo
archivo.close()
#Leer json
#escribir
archivo = open("bd.json", "r")
#leer json
contenido = json.load(archivo)
print(contenido)
#Cerrar archivo
archivo.close()
#Conexion bd

#Establecer conexion con la base de datos
conexion = mysql.connector.connect(
    host = contenido["host"],
    user = contenido["user"],
    password = contenido["password"],
    database = contenido["database"],
    port = contenido["port"]
)
#Crear un cursor para generar consultas
cursor = conexion.cursor()
#Generar consultas en sql
sql = "SELECT * FROM datos WHERE id = 1"
#Comando
cursor.execute(sql)
#Almacernar los datos
sensores = cursor.fetchall()
#Recorrer los resultadoe e imprimirlos
for datos in sensores:
    print(f"libros: {datos}")
#Cerrar el cursor y la conecxion a bd
cursor.close()
conexion.close()