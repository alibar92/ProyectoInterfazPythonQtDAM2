# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frutas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(421, 794)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowOpacity(100.0)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(100, 100, 100, 100)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.orden = QtWidgets.QCheckBox(self.centralwidget)
        self.orden.setObjectName("orden")
        self.gridLayout_3.addWidget(self.orden, 6, 2, 1, 1)
        self.infoNutricional = QtWidgets.QCheckBox(self.centralwidget)
        self.infoNutricional.setObjectName("infoNutricional")
        self.gridLayout_3.addWidget(self.infoNutricional, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.eleccionFruta = QtWidgets.QLabel(self.centralwidget)
        self.eleccionFruta.setObjectName("eleccionFruta")
        self.gridLayout_3.addWidget(self.eleccionFruta, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.eleccionCheckBox = QtWidgets.QLabel(self.centralwidget)
        self.eleccionCheckBox.setObjectName("eleccionCheckBox")
        self.gridLayout_3.addWidget(self.eleccionCheckBox, 3, 0, 1, 5)
        self.listaFrutas = QtWidgets.QComboBox(self.centralwidget)
        self.listaFrutas.setObjectName("listaFrutas")
        self.gridLayout_3.addWidget(self.listaFrutas, 0, 2, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 4, 0, 1, 1)
        self.familia = QtWidgets.QCheckBox(self.centralwidget)
        self.familia.setObjectName("familia")
        self.gridLayout_3.addWidget(self.familia, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.layoutFamily = QtWidgets.QGridLayout()
        self.layoutFamily.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layoutFamily.setObjectName("layoutFamily")
        self.familiaValue = QtWidgets.QLabel(self.centralwidget)
        self.familiaValue.setText("")
        self.familiaValue.setObjectName("familiaValue")
        self.layoutFamily.addWidget(self.familiaValue, 0, 1, 1, 1)
        self.familiaLabel = QtWidgets.QLabel(self.centralwidget)
        self.familiaLabel.setText("")
        self.familiaLabel.setObjectName("familiaLabel")
        self.layoutFamily.addWidget(self.familiaLabel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.layoutFamily)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.layoutOrder = QtWidgets.QGridLayout()
        self.layoutOrder.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layoutOrder.setObjectName("layoutOrder")
        self.ordenValue = QtWidgets.QLabel(self.centralwidget)
        self.ordenValue.setText("")
        self.ordenValue.setObjectName("ordenValue")
        self.layoutOrder.addWidget(self.ordenValue, 0, 1, 1, 1)
        self.ordenLabel = QtWidgets.QLabel(self.centralwidget)
        self.ordenLabel.setText("")
        self.ordenLabel.setObjectName("ordenLabel")
        self.layoutOrder.addWidget(self.ordenLabel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.layoutOrder)
        self.layoutNutritions = QtWidgets.QGridLayout()
        self.layoutNutritions.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layoutNutritions.setObjectName("layoutNutritions")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutNutritions.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutNutritions.addItem(spacerItem7, 7, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutNutritions.addItem(spacerItem8, 6, 2, 1, 1)
        self.salirButton = QtWidgets.QPushButton(self.centralwidget)
        self.salirButton.setObjectName("salirButton")
        self.layoutNutritions.addWidget(self.salirButton, 7, 2, 1, 1)
        self.hidratoLabel = QtWidgets.QLabel(self.centralwidget)
        self.hidratoLabel.setText("")
        self.hidratoLabel.setObjectName("hidratoLabel")
        self.layoutNutritions.addWidget(self.hidratoLabel, 1, 0, 1, 1)
        self.azucaresLabel = QtWidgets.QLabel(self.centralwidget)
        self.azucaresLabel.setText("")
        self.azucaresLabel.setObjectName("azucaresLabel")
        self.layoutNutritions.addWidget(self.azucaresLabel, 2, 0, 1, 1)
        self.proteinasLabel = QtWidgets.QLabel(self.centralwidget)
        self.proteinasLabel.setText("")
        self.proteinasLabel.setObjectName("proteinasLabel")
        self.layoutNutritions.addWidget(self.proteinasLabel, 3, 0, 1, 1)
        self.grasasLabel = QtWidgets.QLabel(self.centralwidget)
        self.grasasLabel.setText("")
        self.grasasLabel.setObjectName("grasasLabel")
        self.layoutNutritions.addWidget(self.grasasLabel, 4, 0, 1, 1)
        self.caloriasLabel = QtWidgets.QLabel(self.centralwidget)
        self.caloriasLabel.setText("")
        self.caloriasLabel.setObjectName("caloriasLabel")
        self.layoutNutritions.addWidget(self.caloriasLabel, 5, 0, 1, 1)
        self.hidratosValue = QtWidgets.QLabel(self.centralwidget)
        self.hidratosValue.setText("")
        self.hidratosValue.setObjectName("hidratosValue")
        self.layoutNutritions.addWidget(self.hidratosValue, 1, 1, 1, 1)
        self.azucaresValue = QtWidgets.QLabel(self.centralwidget)
        self.azucaresValue.setText("")
        self.azucaresValue.setObjectName("azucaresValue")
        self.layoutNutritions.addWidget(self.azucaresValue, 2, 1, 1, 1)
        self.proteinasValue = QtWidgets.QLabel(self.centralwidget)
        self.proteinasValue.setText("")
        self.proteinasValue.setObjectName("proteinasValue")
        self.layoutNutritions.addWidget(self.proteinasValue, 3, 1, 1, 1)
        self.grasasValue = QtWidgets.QLabel(self.centralwidget)
        self.grasasValue.setText("")
        self.grasasValue.setObjectName("grasasValue")
        self.layoutNutritions.addWidget(self.grasasValue, 4, 1, 1, 1)
        self.caloriasValue = QtWidgets.QLabel(self.centralwidget)
        self.caloriasValue.setText("")
        self.caloriasValue.setObjectName("caloriasValue")
        self.layoutNutritions.addWidget(self.caloriasValue, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.layoutNutritions)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName("menubar")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        self.menuAcerca_de_2 = QtWidgets.QMenu(self.menuAcerca_de)
        self.menuAcerca_de_2.setObjectName("menuAcerca_de_2")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTabla = QtWidgets.QAction(MainWindow)
        self.actionTabla.setObjectName("actionTabla")
        self.actionAutor = QtWidgets.QAction(MainWindow)
        self.actionAutor.setObjectName("actionAutor")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionGuardarComoPDF = QtWidgets.QAction(MainWindow)
        self.actionGuardarComoPDF.setObjectName("actionGuardarComoPDF")
        self.menuAcerca_de_2.addAction(self.actionTabla)
        self.menuAcerca_de_2.addAction(self.actionAutor)
        self.menuAcerca_de.addAction(self.menuAcerca_de_2.menuAction())
        self.menuAyuda.addAction(self.actionGuardarComoPDF)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionSalir)
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(MainWindow)
        self.salirButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.listaFrutas, self.familia)
        MainWindow.setTabOrder(self.familia, self.orden)
        MainWindow.setTabOrder(self.orden, self.infoNutricional)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.orden.setText(_translate("MainWindow", "Orden"))
        self.infoNutricional.setText(_translate("MainWindow", "Info nutricional"))
        self.eleccionFruta.setText(_translate("MainWindow", "Elige una Fruta:"))
        self.eleccionCheckBox.setText(_translate("MainWindow", "Selecciona los datos a mostrar:"))
        self.familia.setText(_translate("MainWindow", "Familia"))
        self.salirButton.setText(_translate("MainWindow", "Salir"))
        self.menuAcerca_de.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuAcerca_de_2.setTitle(_translate("MainWindow", "Acerca de.. "))
        self.menuAyuda.setTitle(_translate("MainWindow", "Archivo"))
        self.actionTabla.setText(_translate("MainWindow", "Tabla"))
        self.actionAutor.setText(_translate("MainWindow", "Autor"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionGuardarComoPDF.setText(_translate("MainWindow", "Guardar como PDF"))
