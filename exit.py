
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogexit(object):
    def closing(self):
        QtWidgets.qApp.quit()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 50, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pbexit = QtWidgets.QPushButton(Dialog, clicked=lambda: self.closing())
        self.pbexit.setGeometry(QtCore.QRect(270, 90, 93, 31))
        self.pbexit.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(200, 11, 4);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(241, 12, 4);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(200, 11, 4);\n"
"    \n"
"}")
        self.pbexit.setObjectName("pbexit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 55, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("qmark.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pbcancel = QtWidgets.QPushButton(Dialog)
        self.pbcancel.setGeometry(QtCore.QRect(160, 90, 93, 31))
        self.pbcancel.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(245, 188, 0);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    background-color: rgb(255, 247, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   \n"
"    background-color: rgb(255, 199, 0);\n"
"    \n"
"}")
        self.pbcancel.setObjectName("pbcancel")

        self.retranslateUi(Dialog)
        self.pbexit.clicked.connect(Dialog.close)
        self.pbcancel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Do you really want to quit the game?"))
        self.pbexit.setText(_translate("Dialog", "Quit"))
        self.pbcancel.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialogexit()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
