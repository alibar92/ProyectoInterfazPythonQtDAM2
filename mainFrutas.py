import sys
import requests, json
from PyQt5.QtWidgets import(
    QApplication, QMainWindow, QWidget
)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
from PyQt5.uic import loadUi
from frutas import Ui_MainWindow

class Frutas(QMainWindow, Ui_MainWindow):
    
    #llamo a la API que devuelve un file json con todas las frutas como respuesta
    resp = requests.get('https://www.fruityvice.com/api/fruit/all').json()
        
    def __init__(self,parent=None):
        super().__init__(parent)
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
            #me quedo con el nombre de cada fruta y lo añado a la lista
            frutas.append(i["name"])
        #añado los nombres en el combobox "listaFrutas"
        self.listaFrutas.addItems(frutas)
        #metodo que indentifica que se ha cambiato el texto en el combo
        self.listaFrutas.currentTextChanged.connect(self.getFruta)

    #metodo para mostrar los resultados en la interfaz 
    def mostrarInfoFruta(self, nombreFruta):
        #necesito para hacer una busqueda en la lista de frutas (obj Json) con el nombreFruta recibido
        #me quedo con el nombre de cada fruta
        for i in self.resp:
            if i["name"] == nombreFruta:
                self.objetoFruta = i
        #cada vez que selecciono una fruta se actualizan los valores de las labels
        self.mostrarOrden(self)
        self.mostrarInfoNutricional(self)
        self.mostrarFamilia(self)
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
    def getFruta(self, nombreFruta):
        self.mostrarInfoFruta(nombreFruta)


if __name__=="__main__":
    app=QApplication(sys.argv)
    gui=Frutas()
    gui.show()
    sys.exit(app.exec())