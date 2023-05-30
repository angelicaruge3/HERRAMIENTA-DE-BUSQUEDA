import mysql.connector

conexion = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password ="",
    database = "looking_for_adventures",
    port=3306
)

cursor=conexion.cursor()

sql = "SELECT *FROM libros"

cursor.execute(sql)

sensores = cursor.fetchall()

for datos in sensores:
    print(f"datos looking_for_adventures: {datos}")
    
cursor.close()
conexion.close()