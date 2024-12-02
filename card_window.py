from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QSpinBox, QWidget, QButtonGroup, QGroupBox
)

window = QWidget()
window.resize(550, 450)
window.setWindowTitle("Memory card")

btn_menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити")
btn_ok = QPushButton("Відповісти")

box_min = QSpinBox()
box_min.setValue(10)

rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('')
rbtn4 = QRadioButton('')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

lbl_min = QLabel("хвилин")
lbl_question = QLabel("")

line_rbtn1 = QHBoxLayout()
line_rbtn2 = QHBoxLayout()

line_rbtn1.addWidget(rbtn1)
line_rbtn1.addWidget(rbtn2)
line_rbtn2.addWidget(rbtn3)
line_rbtn2.addWidget(rbtn4)

line_main = QVBoxLayout()
line_main.addLayout(line_rbtn1)
line_main.addLayout(line_rbtn2)

RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroupBox.setLayout(line_main)

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
card_layout = QVBoxLayout()

line1.addWidget(btn_menu)
line1.addStretch(2)
line1.addWidget(btn_sleep)
line1.addWidget(box_min)
line1.addWidget(lbl_min)

line2.addWidget(lbl_question, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))

ans_GroupBox = QGroupBox("Результат тексту")
lbl_result = QLabel("")
lbl_correct = QLabel("")
line_ans = QVBoxLayout()
line_ans.addWidget(lbl_result, alignment=Qt.AlignTop)
line_ans.addWidget(lbl_correct, alignment=Qt.AlignCenter, stretch=2)
ans_GroupBox.setLayout(line_ans)
ans_GroupBox.hide()

line3.addWidget(RadioGroupBox)
line3.addWidget(ans_GroupBox)

line4.addStretch(1)
line4.addWidget(btn_ok, stretch=2)
line4.addStretch(1)

card_layout.addLayout(line1, stretch=1)
card_layout.addLayout(line2, stretch=2)
card_layout.addLayout(line3, stretch=8)
card_layout.addLayout(line4)

window.setLayout(card_layout)