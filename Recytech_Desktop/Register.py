# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from sys import path

path.append('./')
from contact_models import Contact

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 463)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 60, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 120, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 160, 111, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 200, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 240, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(140, 280, 111, 31))
        self.label_6.setObjectName("label_6")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(240, 120, 221, 20))
        self.name.setObjectName("name")
        self.last_name = QtWidgets.QLineEdit(Dialog)
        self.last_name.setGeometry(QtCore.QRect(240, 160, 221, 20))
        self.last_name.setObjectName("last_name")
        self.phone_number = QtWidgets.QLineEdit(Dialog)
        self.phone_number.setGeometry(QtCore.QRect(240, 200, 221, 20))
        self.phone_number.setObjectName("phone_number")
        self.email_address = QtWidgets.QLineEdit(Dialog)
        self.email_address.setGeometry(QtCore.QRect(240, 240, 221, 20))
        self.email_address.setObjectName("email_address")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(240, 280, 221, 20))
        self.password.setObjectName("password")
        self.registrar = QtWidgets.QPushButton(Dialog)
        self.registrar.setGeometry(QtCore.QRect(280, 380, 75, 23))
        self.registrar.setObjectName("registrar")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(140, 320, 111, 31))
        self.label_7.setObjectName("label_7")
        self.generator = QtWidgets.QRadioButton(Dialog)
        self.generator.setGeometry(QtCore.QRect(280, 320, 82, 17))
        self.generator.setObjectName("generator")
        self.collector = QtWidgets.QRadioButton(Dialog)
        self.collector.setGeometry(QtCore.QRect(390, 320, 101, 17))
        self.collector.setObjectName("collector")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "REGISTRAR"))
        self.label_2.setText(_translate("Dialog", "NOMBRES:"))
        self.label_3.setText(_translate("Dialog", "APELLIDOS:"))
        self.label_4.setText(_translate("Dialog", "CELULAR:"))
        self.label_5.setText(_translate("Dialog", "CORREO:"))
        self.label_6.setText(_translate("Dialog", "CONTRASEÑA"))
        self.registrar.setText(_translate("Dialog", "Registrar"))
        self.label_7.setText(_translate("Dialog", "SELECCIONE SU ROL"))
        self.generator.setText(_translate("Dialog", "GENERADOR"))
        self.collector.setText(_translate("Dialog", "RECOLECTOR"))


        self.registrar.clicked.connect(self.saveUser)
    

    def saveUser(self):
        if self.generator.isChecked():
            objeto = Contact()
            objeto.GuardarGenerador(self.name.text(),self.last_name.text(),self.phone_number.text(),self.email_address.text(),self.password.text())
            self.name.setText("")
            self.last_name.setText("")
            self.phone_number.setText("")
            self.email_address.setText("")
            self.password.setText("")
        elif self.collector.isChecked():
            objeto = Contact()
            objeto.GuardarRecolector(self.name.text(),self.last_name.text(),self.phone_number.text(),self.email_address.text(),self.password.text())
            self.name.setText("")
            self.last_name.setText("")
            self.phone_number.setText("")
            self.email_address.setText("")
            self.password.setText("")
