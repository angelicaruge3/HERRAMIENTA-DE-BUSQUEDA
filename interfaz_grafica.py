import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextBrowser

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Herramienta de búsqueda de libros")

        # Crear el contenido principal de la ventana
        etiqueta = QLabel("¡Bienvenido a la herramienta de búsqueda de libros!")
        self.caja_busqueda = QLineEdit()
        boton_buscar = QPushButton("Buscar")
        self.resultados_busqueda = QTextBrowser()

        # Conectar el botón de búsqueda con la función correspondiente
        boton_buscar.clicked.connect(self.realizar_busqueda)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(etiqueta)
        layout_principal.addWidget(self.caja_busqueda)
        layout_principal.addWidget(boton_buscar)
        layout_principal.addWidget(self.resultados_busqueda)

        # Crear un widget contenedor y establecer el diseño principal
        widget_principal = QWidget()
        widget_principal.setLayout(layout_principal)

        # Establecer el widget principal como el widget central de la ventana
        self.setCentralWidget(widget_principal)

        # Conectar a la base de datos MySQL
        self.conexion = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password= "",
            database= "looking_for_adventures",
            port= 3306
        )

    def realizar_busqueda(self):
        # Obtener el término de búsqueda ingresado por el usuario
        termino_busqueda = self.caja_busqueda.text()

        # Realizar la búsqueda en la base de datos
        cursor = self.conexion.cursor()
        consulta = "SELECT * FROM libros WHERE titulo LIKE %s"
        cursor.execute(consulta, ('%' + termino_busqueda + '%',))
        resultados = cursor.fetchall()

        # Mostrar los resultados en la ventana
        self.resultados_busqueda.clear()
        if resultados:
            for resultado in resultados:
                self.resultados_busqueda.append(f"año_publicacion: {resultado[1]}")
                self.resultados_busqueda.append(f"genero: {resultado[2]}")
                self.resultados_busqueda.append(f"sinopsis: {resultado[3]}")
                self.resultados_busqueda.append(f"id_autor: {resultado[4]}")
        else:
            self.resultados_busqueda.append("No se encontraron resultados.")

def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
