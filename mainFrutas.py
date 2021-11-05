import os
import sys
import requests, json
from PyQt5.QtWidgets import(
    QApplication, QMainWindow, QWidget, QMessageBox
)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
from PyQt5.uic import loadUi
from frutas import Ui_MainWindow
from reportlab.pdfgen import canvas


class Frutas(QMainWindow, Ui_MainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        try:
        #llamo a la API que devuelve un file json con todas las frutas como respuesta
            self.resp = requests.get('https://www.fruityvice.com/api/fruit/all').json()
        except:
            self.mensajeError()

        self.setupUi(self)
        #lectura del archivo qss de estilo
        self.setStyleSheet(open("estilos.qss", "r").read())
        self.setWindowTitle("Tabla Nutricional de Frutas")
        self.cargarFrutas()
        #creo una variable para guardar la info de la fruta elegida
        self.objetoFruta = {}
        #deshabilito los checkboxes
        self.familia.setEnabled(False)
        self.orden.setEnabled(False)
        self.infoNutricional.setEnabled(False)
        #conecto los checkBox con sus metodos para mostrar o menos las info
        self.familia.stateChanged.connect(self.mostrarFamilia)
        self.orden.stateChanged.connect(self.mostrarOrden)
        self.infoNutricional.stateChanged.connect(self.mostrarInfoNutricional)
        #llamo al metodo para conectar los señales recibido en el menu con su acciones  
        self.connexionSenalesRanuras()

    def mensajeError(self):
        mensaje=QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setInformativeText("Ha habido un problema con la conexión, inténtalo de nuevo más tarde")
        mensaje.setWindowTitle("Error")
        mensaje.exec_()

    def connexionSenalesRanuras(self):
        #accion para guardar los datos en un PDF
        self.actionGuardarComoPDF.triggered.connect(self.guardarPDF)
        #acción salir llama al cierre de la app
        self.actionSalir.triggered.connect(self.close)
        #acciones acercaDeTabla y acercaDeAutor
        self.actionTabla.triggered.connect(self.acercaDeTabla)
        self.actionAutor.triggered.connect(self.acercaDeAutor)

    def mostrarFamilia(self, state):
        #si el checkbox esta chequeado, setteo el texto de la label y muestro el valor de familia 
        if (QtCore.Qt.Checked == state):
            self.familiaLabel.setText("Familia")
            self.familiaValue.setText(self.objetoFruta["family"])
        #sino setteo todas las labels a null para no mostrar nada
        else: 
            self.familiaLabel.setText("")
            self.familiaValue.setText("")

    def mostrarOrden(self, state):
        if (QtCore.Qt.Checked == state):
            self.ordenLabel.setText("Orden")
            self.ordenValue.setText(self.objetoFruta["order"])
        else:
            self.ordenLabel.setText("")
            self.ordenValue.setText("")
    
    def mostrarInfoNutricional(self, state):
        if (QtCore.Qt.Checked == state):
            self.hidratoLabel.setText("Hidratos")
            self.hidratosValue.setText(str(self.objetoFruta["nutritions"]["carbohydrates"]) + " g")
            self.azucaresLabel.setText("Azúcares")
            self.azucaresValue.setText(str(self.objetoFruta["nutritions"]["sugar"]) + " g")
            self.proteinasLabel.setText("Proteínas")
            self.proteinasValue.setText(str(self.objetoFruta["nutritions"]["protein"]) + " g")
            self.grasasLabel.setText("Grasas")
            self.grasasValue.setText(str(self.objetoFruta["nutritions"]["fat"]) + " g")
            self.caloriasLabel.setText("Calorias")
            self.caloriasValue.setText(str(self.objetoFruta["nutritions"]["calories"]) + " Kcal")
        else:
            self.hidratoLabel.setText("")
            self.hidratosValue.setText("")
            self.azucaresLabel.setText("")
            self.azucaresValue.setText("")
            self.proteinasLabel.setText("")
            self.proteinasValue.setText("")
            self.grasasLabel.setText("")
            self.grasasValue.setText("")
            self.caloriasLabel.setText("")
            self.caloriasValue.setText("")

    #metodo para cargar las frutas desde la API
    def cargarFrutas(self):
        frutas=["--Select--"] #lista de frutas
        for i in self.resp: #se recorre la respuesta de la API
            #me quedo con el nombre de cada fruta y lo anyado a la lista
            frutas.append(i["name"])
        #anyado los nombres en el combobox "listaFrutas"
        self.listaFrutas.addItems(frutas)
        #metodo que indentifica que se ha cambiato el texto en el combo
        #a su vez nos manda el valor seleccionado
        self.listaFrutas.currentTextChanged.connect(self.getFruta)

    #metodo para mostrar los resultados en la interfaz 
    def mostrarInfoFruta(self, nombreFruta):
        #necesito para hacer una busqueda en la lista de frutas (obj Json) con el nombreFruta recibido
        for i in self.resp:
            #esta es la busqueda nombrada en el metodo anterior
            if i["name"] == nombreFruta:
                #y aqui guardo la fruta que he buscado a traves del nombre para tener todos sus datos
                self.objetoFruta = i
        #cada vez que selecciono una fruta se actualizan los valores de las labels
        self.mostrarFamilia(self)
        self.mostrarOrden(self)
        self.mostrarInfoNutricional(self)
        #para quitar los checks y volver a poder chequear lo que queremos mostrar
        self.infoNutricional.setChecked(False)
        self.familia.setChecked(False)
        self.orden.setChecked(False)
        #habilito los checkboxes 
        self.familia.setEnabled(True)
        self.orden.setEnabled(True)
        self.infoNutricional.setEnabled(True)
        #si el elemento de la lista es el 0 (), es decir "--select--"
        if self.listaFrutas.currentIndex() == 0:
            #deshabilito los checkboxes 
            self.familia.setEnabled(False)
            self.orden.setEnabled(False)
            self.infoNutricional.setEnabled(False)

    #metodo para coger la fruta seleccionada
    #el parametro nombreFruta es el que nos ha mandado el metodo anterior (currentTextChanged) 
    def getFruta(self, nombreFruta):
        #este nombre se lo pasamos a nuestro metodo mostrarInfoFruta para coger todos los datos de la fruta a traves de una busqueda
        self.mostrarInfoFruta(nombreFruta)

    #metodo para guardar los datos de cada fruta en un PDF
    def guardarPDF(self):
        #nombre de la ficha cogiendo el name de la fruta elegida
        c = canvas.Canvas("Ficha_" + self.objetoFruta["name"] + ".pdf")
        #datos que escribo en el pdf
        c.drawString(100,750,"Ficha con la información nutricional de la fruta elegida:")
        c.drawString(100,700,("Nombre: " + self.objetoFruta["name"]))
        c.drawString(100,680,("Familia: "+ self.objetoFruta["family"]))
        c.drawString(100,660,("Orden: "+ self.objetoFruta["order"]))
        c.drawString(100,640,("Hidratos: "+ str(self.objetoFruta["nutritions"]["carbohydrates"])+" g"))
        c.drawString(100,620,("Azúcares: "+ str(self.objetoFruta["nutritions"]["sugar"])+" g"))
        c.drawString(100,600,("Proteinas: "+ str(self.objetoFruta["nutritions"]["protein"])+" g"))
        c.drawString(100,580,("Grasas: "+ str(self.objetoFruta["nutritions"]["fat"])+" g"))
        c.drawString(100,560,("Calorias: "+ str(self.objetoFruta["nutritions"]["calories"])+" Kcal"))
        c.save()
    

    #metodo para que se abra una ventana de info
    def acercaDeTabla(self):
        mensaje=QMessageBox()
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setInformativeText("<p>Tabla nutricional construida con:</p><p>- PyQt</p><p>- Qt Designer</p><p>- Python</p>")
        mensaje.setWindowTitle("Acerca de la tabla")
        mensaje.exec_()

    def acercaDeAutor(self):
        mensaje=QMessageBox()
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setInformativeText("<p>Autor: Alice Bartolozzi</p><p>- Nutricionista y desarrolladora")
        mensaje.setWindowTitle("Acerca del autor")
        mensaje.exec_()



if __name__=="__main__":
    app=QApplication(sys.argv)
    gui=Frutas()
    gui.show()
    sys.exit(app.exec())