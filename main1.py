import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(50,50,300,300)
        self.Label1 = QLabel()
        self.Label1.setText("Hello World")
        self.setCentralWidget(self.Label1)
        self.Button=QPushButton("Push Me",self)
        self.Button.clicked.connect(self.ButtonMethod)
        self.Button.setFixedSize(100,20)
        
    def ButtonMethod(self):
        self.Label1.setText("Hi!")
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    main.show_Maximized()
    app.exec()