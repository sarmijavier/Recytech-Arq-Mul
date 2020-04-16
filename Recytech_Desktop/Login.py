# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os


class Ui_Dialog(object):
    def openWindow(self):
        from Register import Ui_Dialog
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 464)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 50, 191, 61))
        self.label.setObjectName("label")
        self.log_in = QtWidgets.QPushButton(Dialog)
        self.log_in.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.log_in.setObjectName("log_in")
        self.register_2 = QtWidgets.QPushButton(Dialog)
        self.register_2.setGeometry(QtCore.QRect(300, 300, 75, 23))
        self.register_2.setObjectName("register_2")
        self.email_address = QtWidgets.QLineEdit(Dialog)
        self.email_address.setGeometry(QtCore.QRect(270, 140, 151, 20))
        self.email_address.setObjectName("email_address")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(270, 190, 151, 20))
        self.password.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(106, 140, 141, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 190, 111, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "BIENVENIDO A  RECYTECH DESKTOP"))
        self.log_in.setText(_translate("Dialog", "Log in"))
        self.register_2.setText(_translate("Dialog", "Register"))
        self.label_2.setText(_translate("Dialog", "CORREO ELECTRONICO"))
        self.label_3.setText(_translate("Dialog", "CONTRASEÑA"))

        self.register_2.clicked.connect(self.openWindow)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())