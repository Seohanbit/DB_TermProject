#!/usr/bin/env python
# coding: utf-8

# 수강신청 페이지

# In[ ]:


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTabWidget, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QMessageBox
import mysql.connector

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()

        # 장바구니 아이템을 저장할 리스트
        self.cart_items = []

        # 다른 탭과 공유할 아이템 리스트
        self.shared_items = []

        # 콤보박스를 클래스 멤버로 정의
        self.combo_department = QComboBox()
        self.combo_major = QComboBox()
        self.combo_grade = QComboBox()

        self.list_professor_results = QListWidget()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('수강신청 페이지')
        self.setGeometry(300, 300, 1200, 750)

        tab_widget = QTabWidget()

        # 탭 페이지 1 - 장바구니
        cart_tab = QWidget()
        cart_layout = QVBoxLayout(cart_tab)
        cart_layout.addWidget(QLabel('내 장바구니'))

        self.list_cart_results = QListWidget()
        cart_layout.addWidget(self.list_cart_results)

        # 탭 페이지 2 - 수강신청
        registration_tab = QWidget()
        registration_layout = QVBoxLayout(registration_tab)

        self.list_registration_results = QListWidget()
        registration_layout.addWidget(self.list_registration_results)

        # 탭 페이지 3 - 학과별 강의조회
        department_tab = QWidget()
        department_layout = QVBoxLayout(department_tab)

        # 학과 선택 드롭다운 메뉴 추가
        combo_department = QComboBox()
        combo_department.addItem('All Department')
        combo_department.addItem('software')
        combo_department.addItem('computer')
        combo_department.addItem('Sociology')
        combo_department.addItem('Mathematics')
        combo_department.addItem('Physics')
        combo_department.addItem('Music')
        combo_department.addItem('Marketing')
        

        # 이수 구분 선택 드롭다운 메뉴 추가
        combo_major = QComboBox()
        combo_major.addItem('all Division')
        combo_major.addItem('specialty')
        combo_major.addItem('all')

        # 학년 선택 드롭다운 메뉴 추가
        combo_grade = QComboBox()
        combo_grade.addItem('all grade')
        for i in range(1, 5):
            combo_grade.addItem(f'{i}')

        # 조회 버튼 추가
        btn_search_department = QPushButton('조회')
        btn_search_department.clicked.connect(self.show_department_results)

        # 메뉴들을 가로로 배치하기 위한 레이아웃
        menu_layout_department = QHBoxLayout()
        menu_layout_department.addWidget(combo_department)
        menu_layout_department.addWidget(combo_major)
        menu_layout_department.addWidget(combo_grade)
        menu_layout_department.addWidget(btn_search_department)
        menu_layout_department.setAlignment(Qt.AlignTop)  # 메뉴들을 위로 정렬
        

        department_layout.addLayout(menu_layout_department)

        self.list_department_results = QListWidget()
        department_layout.addWidget(self.list_department_results)

        # 장바구니 탭에 하위 탭 추가
        cart_layout.addWidget(registration_tab)
        cart_layout.addWidget(department_tab)

        # 탭 페이지 4 - 교수별 강의조회
        professor_tab = QWidget()
        self.professor_layout = QVBoxLayout(professor_tab)

        # If not, create and set them up
        self.line_edit_professor = QLineEdit()

        # 조회 버튼 추가
        self.btn_search_professor = QPushButton('조회')
        self.btn_search_professor.clicked.connect(lambda: self.show_professor_results_for_professor(self.line_edit_professor.text()))

        # 메뉴들을 가로로 배치하기 위한 레이아웃
        menu_layout_professor = QHBoxLayout()
        menu_layout_professor.addWidget(QLabel('교수 입력:'))
        menu_layout_professor.addWidget(self.line_edit_professor)
        menu_layout_professor.addWidget(self.btn_search_professor)
        menu_layout_professor.setAlignment(Qt.AlignTop)  # 메뉴들을 위로 정렬

        # 기존의 레이아웃을 유지하면서 새로운 레이아웃 요소를 추가
        self.professor_layout.addLayout(menu_layout_professor)
        self.list_professor_results = QListWidget()
        self.professor_layout.addWidget(self.list_professor_results)


        btn_add_to_cart = QPushButton('담기')
        btn_add_to_cart.setFixedSize(40, 20)


        # 탭 위젯에 탭 추가
        tab_widget.addTab(cart_tab, '장바구니')
        tab_widget.addTab(registration_tab, '수강신청')
        tab_widget.addTab(department_tab, '학과별 강의조회')
        tab_widget.addTab(professor_tab, '교수별 강의조회')

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)

        self.setLayout(main_layout)

    

    def show_registration_results(self):
        # 수강신청 탭의 리스트 갱신
        self.list_registration_results.clear()
        for item_text in self.shared_items:  # 장바구니와 공유되는 아이템 리스트 사용
            item = QListWidgetItem(item_text)
            self.list_registration_results.addItem(item)

            btn_delete_registration_item = QPushButton('삭제')
            btn_delete_registration_item.clicked.connect(lambda _, item=item: self.delete_cart_item_for_registration_item(item))
            btn_delete_registration_item.setFixedSize(80, 30)

            btn_apply_registration = QPushButton('신청')
            btn_apply_registration.clicked.connect(lambda _, item=item: self.apply_registration(item, btn_apply_registration))
            btn_apply_registration.setFixedSize(80, 30)

            # 'Delete' 버튼을 오른쪽으로 정렬하기 위한 수동 정렬
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(QLabel(''))  # 공간 추가
            layout.addWidget(btn_delete_registration_item)
            layout.addWidget(btn_apply_registration)
            item.setSizeHint(widget.sizeHint())
            item.setFlags(item.flags() | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.list_registration_results.setItemWidget(item, widget)

    def apply_registration(self, item, button):
        # 수강신청 버튼이 클릭되었을 때 실행되는 함수
        item_text = item.text()
        print(f"강의를 수강신청합니다: {item_text}")

        # 수강신청 리스트 갱신
        self.show_registration_results()

        # "신청" 버튼을 비활성화
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, QColor('gray'))
        button.setPalette(palette)

        button.setEnabled(False)


    def show_department_results(self):
    # MySQL 연결 설정
        mydb = mysql.connector.connect(
            host="192.168.148.4",
            user="seohanbit",
            password="gksqlc0627!",
            database="TermProject",
            port=4567
        )

        try:
            conn = mydb
            cursor = conn.cursor()

            # 데이터베이스에서 데이터를 가져와서 리스트에 표시
            query = "SELECT * FROM class"
            cursor.execute(query)
            results = cursor.fetchall()

            # 포맷 지정을 위한 너비
            column_widths = [15, 5, 30, 15, 5, 15, 15, 10, 10, 10, 15]

            # 헤더를 추가하기 위한 코드
            headers = ["Class ID", "Group", "Name", "Day", "Grade", "Current Students", "Max Students", "Major", "Division", "Prof ID", "Room"]
            
            # 헤더의 구분선을 생성
            header_line = "+".join("-" * (width + 2) for width in column_widths)
            
            # 헤더와 구분선을 조합
            header_text = f"{header_line}\n| {' | '.join(f'{header:<{width}}' for header, width in zip(headers, column_widths))} |\n{header_line}"
            header_item = QListWidgetItem(header_text)
            self.list_department_results.addItem(header_item)

            # 실제 데이터 출력
            for result in results:
                # 각 열을 특정 너비로 정렬하도록 포맷팅
                item_text = "|".join(f" {value:<{width}} " for value, width in zip(result, column_widths))

                # 데이터와 구분선을 조합
                item_text = f"{header_line}\n| {item_text} |\n{header_line}"
                
                item = QListWidgetItem(item_text)
                self.list_department_results.addItem(item)

                # '담기' 버튼 생성 및 연결
                btn_add_to_cart = QPushButton('담기')
                btn_add_to_cart.clicked.connect(lambda _, item=item: self.add_to_cart(item))

                # '담기' 버튼 크기 조절 (예: 80x30 픽셀)
                btn_add_to_cart.setFixedSize(80, 30)

                # '담기' 버튼을 오른쪽으로 정렬하기 위한 수동 정렬
                widget = QWidget()
                layout = QHBoxLayout(widget)
                layout.addWidget(QLabel(''))  # 공간 추가
                layout.addWidget(btn_add_to_cart)
                item.setSizeHint(widget.sizeHint())
                item.setFlags(item.flags() | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                self.list_department_results.setItemWidget(item, widget)

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "MySQL Error", f"MySQL Error: {err}")

        finally:
            # MySQL 연결 종료
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()


    def show_professor_results_for_professor(self, professor_name):
        # MySQL 연결 설정
        mydb = mysql.connector.connect(
            host="192.168.148.4",
            user="seohanbit",
            password="gksqlc0627!",
            database="TermProject",
            port=4567
        )

        try:
            conn = mydb
            cursor = conn.cursor()

            # 교수명에 해당하는 강의 데이터 가져오기
            query = "SELECT * FROM class WHERE prof_id = %s"
            cursor.execute(query, (professor_name,))
            results = cursor.fetchall()

             # 포맷 지정을 위한 너비
            column_widths = [15, 5, 30, 15, 5, 15, 15, 10, 10, 10, 15]

            # 헤더를 추가하기 위한 코드
            headers = ["Class ID", "Group", "Name", "Day", "Grade", "Current Students", "Max Students", "Major", "Division", "Prof ID", "Room"]
            
            # 헤더의 구분선을 생성
            header_line = "+".join("-" * (width + 2) for width in column_widths)
            
            # 헤더와 구분선을 조합
            header_text = f"{header_line}\n| {' | '.join(f'{header:<{width}}' for header, width in zip(headers, column_widths))} |\n{header_line}"
            header_item = QListWidgetItem(header_text)
            self.list_professor_results.addItem(header_item)

            # 실제 데이터 출력
            for result in results:
                # 각 열을 특정 너비로 정렬하도록 포맷팅
                item_text = "|".join(f" {value:<{width}} " for value, width in zip(result, column_widths))

                # 데이터와 구분선을 조합
                item_text = f"{header_line}\n| {item_text} |\n{header_line}"
                
                item = QListWidgetItem(item_text)
                self.list_professor_results.addItem(item)

                # '담기' 버튼 생성 및 연결
                btn_add_to_cart = QPushButton('담기')
                btn_add_to_cart.clicked.connect(lambda _, item=item: self.add_to_cart(item))

                # '담기' 버튼 크기 조절 (예: 80x30 픽셀)
                btn_add_to_cart.setFixedSize(80, 30)

                # '담기' 버튼을 오른쪽으로 정렬하기 위한 수동 정렬
                widget = QWidget()
                layout = QHBoxLayout(widget)
                layout.addWidget(QLabel(''))  # 공간 추가
                layout.addWidget(btn_add_to_cart)
                item.setSizeHint(widget.sizeHint())
                item.setFlags(item.flags() | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                self.list_professor_results.setItemWidget(item, widget)

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "MySQL Error", f"MySQL Error: {err}")

        finally:
            # MySQL 연결 종료
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()
        print(results)


    def add_to_cart(self, item):
        # '담기' 버튼이 클릭되었을 때 실행되는 함수
        item_text = item.text()
        print(f"상품을 장바구니에 추가합니다: {item_text}")

        # 장바구니 아이템 리스트에 추가
        self.cart_items.append(item_text)
    
        # 공유 아이템 리스트에도 추가
        self.shared_items.append(item_text)

        # 장바구니 리스트를 다시 표시
        self.show_cart_results()

        # 수강신청 탭의 리스트 갱신
        self.show_registration_results()

    def show_cart_results(self):
        # 장바구니 아이템 리스트를 출력
        self.list_cart_results.clear()
        for cart_item in self.cart_items:
            item = QListWidgetItem(cart_item)
            self.list_cart_results.addItem(item)
    
            btn_delete_cart_item = QPushButton('삭제')
            btn_delete_cart_item.clicked.connect(lambda _, item=item: self.delete_cart_item_for_item(item))
            btn_delete_cart_item.setFixedSize(80, 30)
    
            # 'Delete' 버튼을 오른쪽으로 정렬하기 위한 수동 정렬
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(QLabel(''))  # 공간 추가
            layout.addWidget(btn_delete_cart_item)
            item.setSizeHint(widget.sizeHint())
            item.setFlags(item.flags() | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.list_cart_results.setItemWidget(item, widget)

    def delete_cart_item(self):
        # 선택된 장바구니 아이템 삭제
        selected_items = self.list_cart_results.selectedItems()
        for item in selected_items:
            item_text = item.text()
            print(f"장바구니에서 아이템을 삭제합니다: {item_text}")
            self.cart_items.remove(item_text)
            self.shared_items.remove(item_text)
    
        # 장바구니 리스트 다시 표시
        self.show_cart_results()
    
    def delete_cart_item_for_item(self, item):
        # Delete 버튼 클릭 시 해당 아이템 삭제
        item_text = item.text()
        print(f"장바구니에서 아이템을 삭제합니다: {item_text}")
        self.cart_items.remove(item_text)
    
        # 장바구니 리스트 다시 표시
        self.show_cart_results()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    registration_page = RegistrationPage()
    registration_page.show()

    sys.exit(app.exec_())

