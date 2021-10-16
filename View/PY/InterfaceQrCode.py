# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfaceQrCode.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QrCodeCreator(object):
    def setupUi(self, QrCodeCreator):
        QrCodeCreator.setObjectName("QrCodeCreator")
        QrCodeCreator.resize(842, 555)
        QrCodeCreator.setMinimumSize(QtCore.QSize(842, 555))
        QrCodeCreator.setMaximumSize(QtCore.QSize(842, 555))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imagens/Qr-Code-Creator.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QrCodeCreator.setWindowIcon(icon)
        QrCodeCreator.setStyleSheet("background-color: white;")
        self.Centro = QtWidgets.QWidget(QrCodeCreator)
        self.Centro.setObjectName("Centro")
        self.btn_save = QtWidgets.QPushButton(self.Centro)
        self.btn_save.setGeometry(QtCore.QRect(440, 430, 311, 41))
        self.btn_save.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgb(6, 205, 227);\n"
"border-radius: 8px;\n"
"font: 75 13pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: rgb(7, 224, 244);\n"
"border-radius: 8px;\n"
"font: 75 13pt \"Montserrat\";\n"
"}")
        self.btn_save.setObjectName("btn_save")
        self.line_link = QtWidgets.QLineEdit(self.Centro)
        self.line_link.setGeometry(QtCore.QRect(440, 350, 311, 51))
        self.line_link.setStyleSheet("background-color: rgba(0, 0 , 0, 0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #07D7F0;\n"
"color: rgb(0,0,0);\n"
"padding-bottom: 8px;\n"
"border-radius: 0px;\n"
"font: 12pt \"Montserrat\";")
        self.line_link.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_link.setDragEnabled(False)
        self.line_link.setClearButtonEnabled(True)
        self.line_link.setObjectName("line_link")
        self.lbl_qrcode_link = QtWidgets.QLabel(self.Centro)
        self.lbl_qrcode_link.setGeometry(QtCore.QRect(478, 90, 241, 221))
        self.lbl_qrcode_link.setText("")
        self.lbl_qrcode_link.setPixmap(QtGui.QPixmap(":/Imagens/Qr Code - Gray.png"))
        self.lbl_qrcode_link.setScaledContents(True)
        self.lbl_qrcode_link.setObjectName("lbl_qrcode_link")
        self.frame = QtWidgets.QFrame(self.Centro)
        self.frame.setGeometry(QtCore.QRect(0, 0, 351, 561))
        self.frame.setStyleSheet("background-color: rgb(7, 215, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_nome_app = QtWidgets.QLabel(self.frame)
        self.lbl_nome_app.setGeometry(QtCore.QRect(22, 40, 311, 41))
        self.lbl_nome_app.setStyleSheet("color: white;\n"
"font: 28pt \"Montserrat\";")
        self.lbl_nome_app.setObjectName("lbl_nome_app")
        self.lbl_criador = QtWidgets.QLabel(self.frame)
        self.lbl_criador.setGeometry(QtCore.QRect(24, 80, 191, 31))
        self.lbl_criador.setStyleSheet("color: white;\n"
"font: 12pt \"Montserrat\";")
        self.lbl_criador.setObjectName("lbl_criador")
        self.lbl_conectividade = QtWidgets.QLabel(self.frame)
        self.lbl_conectividade.setGeometry(QtCore.QRect(29, 200, 291, 231))
        self.lbl_conectividade.setText("")
        self.lbl_conectividade.setPixmap(QtGui.QPixmap(":/Imagens/undraw_connected_world_wuay.svg"))
        self.lbl_conectividade.setScaledContents(True)
        self.lbl_conectividade.setObjectName("lbl_conectividade")
        QrCodeCreator.setCentralWidget(self.Centro)

        self.retranslateUi(QrCodeCreator)
        QtCore.QMetaObject.connectSlotsByName(QrCodeCreator)

    def retranslateUi(self, QrCodeCreator):
        _translate = QtCore.QCoreApplication.translate
        QrCodeCreator.setWindowTitle(_translate("QrCodeCreator", "Qr Code Creator"))
        self.btn_save.setText(_translate("QrCodeCreator", "Save"))
        self.line_link.setPlaceholderText(_translate("QrCodeCreator", "Link"))
        self.lbl_nome_app.setText(_translate("QrCodeCreator", "Qr Code Creator"))
        self.lbl_criador.setText(_translate("QrCodeCreator", "by Geovani Debastiani"))
import arquivo_rc