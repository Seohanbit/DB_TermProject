import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import mysql.connector
from Main_page_before_DB import RegistrationPage

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('로그인')
        self.setGeometry(300, 300, 300, 150)

        self.label_id = QLabel('아이디:')
        self.label_pw = QLabel('패스워드:')

        self.edit_id = QLineEdit()
        self.edit_pw = QLineEdit()
        self.edit_pw.setEchoMode(QLineEdit.Password)  # 패스워드 입력 시 '*'로 표시

        self.btn_login = QPushButton('로그인')
        self.btn_login.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.label_id)
        layout.addWidget(self.edit_id)
        layout.addWidget(self.label_pw)
        layout.addWidget(self.edit_pw)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def login(self):
        entered_id = self.edit_id.text()
        entered_pw = self.edit_pw.text()

        # MySQL 서버에 연결
        mydb = mysql.connector.connect(
            host="192.168.148.4",
            user="seohanbit",
            password="gksqlc0627!",
            database="TermProject",
            port=4567
        )

        cursor = mydb.cursor()

        query = f"SELECT * FROM student WHERE Student_id = '{entered_id}' AND Password = '{entered_pw}'"
        cursor.execute(query)

        result = cursor.fetchall()

        cursor.close()
        mydb.close()

        if result:
            QMessageBox.information(self, '로그인 성공', '로그인에 성공했습니다.')
            
            # 로그인 성공 시 메인 페이지를 표시
            self.show_main_page()
        else:
            QMessageBox.warning(self, '로그인 실패', '아이디 또는 패스워드가 잘못되었습니다.')

    def show_main_page(self):
        # 메인 페이지를 표시하는 함수
        self.main_page = RegistrationPage()
        self.main_page.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())
