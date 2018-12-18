from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
import dict


class Window(QWidget):
    def __init__(self, wlist):
        super().__init__()

        self.wlist = wlist
        self.title = "Lets see!"
        self.top = 100
        self.left = 300
        self.w = 680
        self.h = 500
        self.initWin()

    def initWin(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.w, self.h)
        self.setStyleSheet("QWidget {background: '#123456';}")

        self.tField = QLineEdit(self)
        self.tField.setGeometry(50, 50, 400, 50)
        self.tField.setStyleSheet("QLineEdit {background: '#FFFFFF';}")
        font = QtGui.QFont("Times", 15)
        self.tField.setFont(font)

        sButton = QPushButton("Search", self)
        sButton.setGeometry(470, 60, 50, 30)
        sButton.setStyleSheet("QPushButton {background: '#00FFFF';}")
        sButton.clicked.connect(self.searchClick)

        self.console = QLineEdit(self)
        self.console.setGeometry(50,200,350,100)
        self.console.setStyleSheet("QLineEdit {background: '#FFFFFF';}")
        self.console.setFont(font)

        self.initCompleter(self.tField)

    def initCompleter(self, tField):
        completer = QCompleter(self.wlist, self.tField)
        self.tField.setCompleter(completer)

    def searchClick(self):
        print(self.tField.text())

        t, found = dict.searching(self.tField.text().strip("\n"))
        if (found):
            output = "Found in %f Seconds" %t
            self.console.setText(output)
        else:
            self.console.setText("Not Found")


wlist = dict.Load()
App = QApplication(sys.argv)
win = Window(wlist)
win.show()

sys.exit(App.exec_())
