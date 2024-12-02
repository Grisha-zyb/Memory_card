from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from random import choice, shuffle
from time import sleep

app = QApplication([])

from card_window import *
from main_window import *

class Question:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

count_ask = 0
count_right = 0
q1 = Question('Вікно', 'Window', 'Widget', 'Wendows', 'Would')
q2 = Question("Комп'ютер", 'Computer', 'Competition', 'Could', 'Tablet')
q3 = Question('Миша', 'Mouse', 'Hamster', 'Misha', 'Milk')
q4 = Question('Стіна', 'Wall', 'Fence', 'Door', 'Walpaper')

questions = [q1, q2, q3, q4]
radio_buttons = [rbtn1, rbtn2, rbtn3, rbtn4]

def new_question():
    global cur_quest
    cur_quest = choice(questions)
    lbl_question.setText(cur_quest.question)
    lbl_correct.setText(cur_quest.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_quest.wrong_ans1)
    radio_buttons[1].setText(cur_quest.wrong_ans2)
    radio_buttons[2].setText(cur_quest.wrong_ans3)
    radio_buttons[3].setText(cur_quest.answer)
new_question()

def check():
    global count_ask, count_right
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lbl_correct.text():
                count_right += 1
                lbl_result.setText("Правильно!")
            else:
                lbl_result.setText("Не правильно!")
            count_ask += 1
            answer.setChecked(False)
            break
    RadioGroup.setExclusive(True)

def switch_screen():
    if btn_ok.text() == "Відповісти":
        check()
        RadioGroupBox.hide()
        ans_GroupBox.show()
        btn_ok.setText("Наступне запитання")
    else:
        ans_GroupBox.hide()
        RadioGroupBox.show()
        new_question()
        btn_ok.setText("Відповісти")

btn_ok.clicked.connect(switch_screen)

def rest():
    window.hide()
    n = box_min.value() * 60
    sleep(n)
    window.show()

btn_sleep.clicked.connect(rest)

def to_menu():
    window.hide()
    main_window.show()

btn_menu.clicked.connect(to_menu)

def to_quests():
    main_window.hide()
    window.show()

back_btn.clicked.connect(to_quests)

def clear():
    edit_que.clear()
    edit_ans_corr.clear()
    edit_ans_incor1.clear()
    edit_ans_incor2.clear()
    edit_ans_incor3.clear()

btn_clr.clicked.connect(clear)

def add_quest():
    q = Question(edit_que.text(), edit_ans_corr.text(), edit_ans_incor1.text(), edit_ans_incor2.text(), edit_ans_incor3.text())
    questions.append(q)
    clear()

btn_add.clicked.connect(add_quest)

window.show()
app.exec_()
