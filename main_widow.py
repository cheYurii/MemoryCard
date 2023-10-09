from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSpinBox, QGroupBox, QButtonGroup, 
card_width, card_hight = 600, 500
app = QApplication([])
win_QWidget()
win_card.recize(card_width, card_hight)
win_card.move(300,300)
win_card.setWindowTitle("Memory Card")

btn_sleep = QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(30)
btn_menu = QPushButton("Меню")
btn_next = QPushButton("Відповісти")
RadioGroupBox = QGroupBox("Варіанти відповідей")

RadioGroup = QButtonGroup()

rbtn_ans1 = RadioButton("1")
rbtn_ans2 = RadioButton("2")
rbtn_ans3 = RadioButton("3")
rbtn_ans4 = RadioButton("4")

RadioGroup.addButton(rbtn_ans1)
RadioGroup.addButton(rbtn_ans2)
RadioGroup.addButton(rbtn_ans3)
RadioGroup.addButton(rbtn_ans4)

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn_ans1)
layout_ans2.addWidget(rbtn_ans2)
layout_ans3.addWidget(rbtn_ans3)
layout_ans3.addWidget(rbtn_ans4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

win.card.show()