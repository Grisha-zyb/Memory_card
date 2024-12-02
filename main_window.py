from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QWidget
)

main_window = QWidget()
main_window.resize(400,300)
main_window.setWindowTitle("Створення запитання")

lbl_que_new = QLabel("Введіть запитання:")
lbl_ans_corr = QLabel("Введіть правильну відповідь:")
lbl_ans_incor1 = QLabel("Введіть першу хибну відповідь:")
lbl_ans_incor2 = QLabel("Введіть другу хибну відповідь:")
lbl_ans_incor3 = QLabel("Введіть третю хибну відповідь:")

mk_lbl = QVBoxLayout()
mk_lbl.addWidget(lbl_que_new)
mk_lbl.addWidget(lbl_ans_corr)
mk_lbl.addWidget(lbl_ans_incor1)
mk_lbl.addWidget(lbl_ans_incor2)
mk_lbl.addWidget(lbl_ans_incor3)

edit_que = QLineEdit()
edit_ans_corr = QLineEdit()
edit_ans_incor1 = QLineEdit()
edit_ans_incor2 = QLineEdit()
edit_ans_incor3 = QLineEdit()

mk_edt = QVBoxLayout()
mk_edt.addWidget(edit_que)
mk_edt.addWidget(edit_ans_corr)
mk_edt.addWidget(edit_ans_incor1)
mk_edt.addWidget(edit_ans_incor2)
mk_edt.addWidget(edit_ans_incor3)

h1 = QHBoxLayout()
h1.addLayout(mk_lbl)
h1.addLayout(mk_edt)

btn_add = QPushButton("Додати запитання")
btn_clr = QPushButton("Очистити")

mk_btn = QHBoxLayout()
mk_btn.addWidget(btn_add)
mk_btn.addWidget(btn_clr)

stat_lbl = QLabel("Статистика")
stat_lbl.setStyleSheet("font-size: 20px; font-weight: bold;")
inf_lbl = QLabel()

back_btn = QPushButton("Назад")

mk_main = QVBoxLayout()
mk_main.addLayout(h1)
mk_main.addLayout(mk_btn)
mk_main.addWidget(stat_lbl)
mk_main.addWidget(inf_lbl)
mk_main.addWidget(back_btn)

main_window.setLayout(mk_main)


