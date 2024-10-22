import sys
from PyQt5.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        MainWidget = QWidget()
        Layout = QFormLayout()
        MainWidget.setLayout(Layout)
        self.setCentralWidget(MainWidget)
        self.userLineEdit = QLineEdit()
        self.passLineEdit = QLineEdit()
        self.passLineEdit.setEchoMode(QLineEdit.Password)
        self.submitButton = QPushButton("Submit")
        self.cancelButton = QPushButton("Cancel")
        
        Layout.addRow(QLabel("Username"),self.userLineEdit)
        Layout.addRow(QLabel("Password"),self.passLineEdit)
        Layout.addRow(self.submitButton,self.cancelButton)
        
        self.resize(300,100)
        
      
    
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()