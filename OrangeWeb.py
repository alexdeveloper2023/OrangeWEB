import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtGui

class MainWindow(QMainWindow, QWidget):
    def __init__(self):

            
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        self.browser.page().fullScreenRequested.connect(lambda request: request.accept())
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon("OrangeWeb.ico"))

        navbar = QToolBar(self)
        navbar.setMovable(False)
        navbar.toggleViewAction().setVisible(False)

        btn_1 = QAction(QtGui.QIcon("Atras.ico"), "Atras", self)
        btn_2 = QAction(QtGui.QIcon("Refrescar.ico"), "Refrescar", self)
        btn_3 = QAction(QtGui.QIcon("Adelante.ico"), "Adelante", self)
        self.search = QLineEdit(self)
        
        btn_1.triggered.connect(self.browser.back)
        btn_2.triggered.connect(self.browser.reload)
        btn_3.triggered.connect(self.browser.forward)
        self.search.returnPressed.connect(self.btnIrClicked)
        self.browser.urlChanged.connect(self.UpdateUrl)
        navbar.addAction(btn_1)
        navbar.addAction(btn_2)
        navbar.addAction(btn_3)
        navbar.addWidget(self.search)

        self.addToolBar(navbar)
        
    def btnIrClicked(self):
        url = self.search.text()
        self.browser.setUrl(QUrl(url))

    def UpdateUrl(self, q):
        self.search.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('OrangeWeb V1')
window = MainWindow()
app.exec()
