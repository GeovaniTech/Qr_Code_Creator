import qrcode
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from View.PY.InterfaceQrCode import Ui_QrCodeCreator


class QrCodeCreator(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_QrCodeCreator()
        self.ui.setupUi(self)

        self.ui.line_link.textChanged.connect(self.UpdateQrCodeInterface)
        self.ui.btn_save.clicked.connect(self.QrCodeCreator)

    def QrCodeCreator(self):

        link = self.ui.line_link.text()

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=0
        )

        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='transparent')
        img.save('YourQrCode.png')

    def UpdateQrCodeInterface(self):
        pixmapBlack = QPixmap(r'View/RC/Qr Code - Black.png')
        pixmapGray = QPixmap(r'View/RC/Qr Code - Gray.png')

        if self.ui.line_link.text() != "":
            self.ui.lbl_qrcode_link.setPixmap(pixmapBlack)
        else:
            self.ui.lbl_qrcode_link.setPixmap(pixmapGray)


if __name__ == '__main__':

    # Configurando Aplicação
    app = QApplication(sys.argv)
    window = QrCodeCreator()
    window.show()
    sys.exit(app.exec_())