import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Welcome to the Login Portal")
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f2f5;
            }
            QWidget {
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel {
                color: #1a73e8;
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 10px;
                border: 2px solid #e0e0e0;
                border-radius: 5px;
                background-color: white;
                font-size: 13px;
                min-width: 250px;
            }
            QLineEdit:focus {
                border: 2px solid #1a73e8;
                outline: none;
            }
            QPushButton {
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-size: 13px;
                font-weight: bold;
                min-width: 50px;
            }
            QPushButton#submitBtn {
                background-color: #1a73e8;
                color: white;
            }
            QPushButton#submitBtn:hover {
                background-color: #1557b0;
            }
            QPushButton#cancelBtn {
                background-color: #f0f2f5;
                border: 1px solid #dadce0;
                color: #3c4043;
            }
            QPushButton#cancelBtn:hover {
                background-color: #e8eaed;
            }
            QCheckBox {
                color: #5f6368;
                font-size: 13px;
            }
        """)

        # Create main widget and layout
        main_widget = QWidget()
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Create form layout
        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        # Title label with modern styling
        title_label = QLabel("Secure Your Account")
        title_label.setStyleSheet("""
            font-size: 24px; 
            font-weight: bold; 
            color: #1a73e8; 
            margin-bottom: 20px;
        """)
        title_label.setAlignment(Qt.AlignCenter)

        self.user_line_edit = QLineEdit()
        self.user_line_edit.setPlaceholderText("Enter your username")
        
        self.pass_line_edit = QLineEdit()
        self.pass_line_edit.setPlaceholderText("Enter your password")
        self.pass_line_edit.setEchoMode(QLineEdit.Password)

        #password checkbox
        self.show_password_checkbox = QCheckBox("Show password")
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)

        # mybutton
        button_layout = QHBoxLayout()
        self.submit_button = QPushButton("Login")
        self.submit_button.setObjectName("submitBtn")
        self.submit_button.clicked.connect(self.check_credentials) 
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setObjectName("cancelBtn")
        
       
        form_layout.addRow(QLabel("Username"), self.user_line_edit)
        form_layout.addRow(QLabel("Password"), self.pass_line_edit)
        
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.cancel_button)

        layout.addWidget(title_label)
        layout.addLayout(form_layout)
        layout.addWidget(self.show_password_checkbox)
        layout.addLayout(button_layout)
        
        
        layout.setContentsMargins(20, 30, 20, 20)
        layout.setSpacing(15)
        
        
        self.setFixedSize(400, 350)
        
        
        
    def toggle_password_visibility(self, state):
        if state == Qt.Checked:
            self.pass_line_edit.setEchoMode(QLineEdit.Normal)
        else:
            self.pass_line_edit.setEchoMode(QLineEdit.Password)

    def check_credentials(self):
        username = self.user_line_edit.text()
        password = self.pass_line_edit.text()
        
        if username == "admin" and password == "admin":
            QMessageBox.information(self, "Login Successful", f"Welcome back, {username}!")
        else:
            QMessageBox.critical(self, "Login Failed", "Wrong credentials, please try again.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
