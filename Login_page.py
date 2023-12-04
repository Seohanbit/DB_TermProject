#!/usr/bin/env python
# coding: utf-8

# 로그인 페이지

# In[2]:


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

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

        # 여기에서는 사용자가 입력한 아이디와 패스워드를 간단히 비교합니다.
        # 실제로는 데이터베이스에서 검증하는 과정이 필요합니다.
        if entered_id == '사용자아이디' and entered_pw == '패스워드':
            QMessageBox.information(self, '로그인 성공', '로그인에 성공했습니다.')
        else:
            QMessageBox.warning(self, '로그인 실패', '아이디 또는 패스워드가 잘못되었습니다.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())


# In[ ]:





# In[ ]:





# In[ ]:




