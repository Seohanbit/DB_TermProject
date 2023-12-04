#!/usr/bin/env python
# coding: utf-8

# 수강신청 페이지

# In[1]:


from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTabWidget, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()

        # 장바구니 아이템을 저장할 리스트
        self.cart_items = []

        # 다른 탭과 공유할 아이템 리스트
        self.shared_items = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('수강신청 페이지')
        self.setGeometry(300, 300, 800, 600)

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
        combo_department.addItem('전체 학과')
        combo_department.addItem('소프트웨어학과')
        combo_department.addItem('컴퓨터공학과')

        # 이수 구분 선택 드롭다운 메뉴 추가
        combo_major = QComboBox()
        combo_major.addItem('전체 이수 구분')
        combo_major.addItem('전공')
        combo_major.addItem('일반')

        # 학년 선택 드롭다운 메뉴 추가
        combo_grade = QComboBox()
        combo_grade.addItem('전체 학년')
        for i in range(1, 5):
            combo_grade.addItem(f'{i}학년')

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
        professor_layout = QVBoxLayout(professor_tab)

        # 교수 입력 라인 에디트 추가
        line_edit_professor = QLineEdit()

        # 조회 버튼 추가
        btn_search_professor = QPushButton('조회')
        btn_search_professor.clicked.connect(self.show_professor_results)

        # 메뉴들을 가로로 배치하기 위한 레이아웃
        menu_layout_professor = QHBoxLayout()
        menu_layout_professor.addWidget(QLabel('교수 입력:'))
        menu_layout_professor.addWidget(line_edit_professor)
        menu_layout_professor.addWidget(btn_search_professor)
        menu_layout_professor.setAlignment(Qt.AlignTop)  # 메뉴들을 위로 정렬

        professor_layout.addLayout(menu_layout_professor)

        self.list_professor_results = QListWidget()
        professor_layout.addWidget(self.list_professor_results)

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
        
    def show_cart_results(self):
        # This is a placeholder function, you should replace it with the actual logic to fetch and display results.

        self.list_cart_results.clear()
        for result in results:
            item = QListWidgetItem(result)
            self.list_cart_results.addItem(item)

    

    def show_registration_results(self):
        # This is a placeholder function, you should replace it with the actual logic to fetch and display results.

        self.list_registration_results.clear()
        for result in results:
            item = QListWidgetItem(result)
            self.list_registration_results.addItem(item)

    def show_department_results(self):
        # This is a placeholder function, you should replace it with the actual logic to fetch and display results.
        results = ["결과 1", "결과 2", "결과 3"]

        self.list_department_results.clear()
        for result in results:
            item = QListWidgetItem(result)
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

    def show_professor_results(self):
        # This is a placeholder function, you should replace it with the actual logic to fetch and display results.
        results = ["결과 A", "결과 B", "결과 C"]

        self.list_professor_results.clear()
        for result in results:
            item = QListWidgetItem(result)
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
            cart_item_widget = QListWidgetItem(cart_item)
            self.list_cart_results.addItem(cart_item_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    registration_page = RegistrationPage()
    registration_page.show()

    sys.exit(app.exec_())

