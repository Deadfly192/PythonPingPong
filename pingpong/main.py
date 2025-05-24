from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QSlider
import json
import os

def start():
    btn_start_2p.hide()
    win.hide()
    import pingpong
    app.quit()



app = QApplication([])
win = QWidget()
win.setWindowTitle('Ping pong launcher')
win.resize(1000, 700)

app.setStyleSheet("""
    QPushButton {
        font: 75 10pt "Microsoft YaHei UI";
        font-weight: bold;
        background-color: #e6e6e6;
        border-style: solid;
        border-width: 2px;
        border-radius: 10px;
        border-color: white;
        min-width: 10em;
        padding: 6px;
    }
    QPushButton:pressed {
        background-color: rgb(220, 220, 220);
        border-style: inset;
    }
    QLabel {
        font: 195 30pt "Comic Sans MS";
    }
    QLineEdit {
        font: 75 10pt "Microsoft YaHei UI";
    }
""")

def gamespeed():
    if slider_gamespeed.value() == 10:
        lb_gamespeed_value.setText(f'Cкорость игры: {str(slider_gamespeed.value())} (рекомендуемая)')
    else:
        lb_gamespeed_value.setText(f'Cкорость игры: {str(slider_gamespeed.value())}')
    save['game_speed'] = slider_gamespeed.value()
    print(save)
    save_json()
        
def ballsize():
    if slider_ballsize.value() == 40:
        lb_ballsize_value.setText(f'Размер мяча: {str(slider_ballsize.value())} (рекомендуемый)')
    else:
        lb_ballsize_value.setText(f'Размер мяча: {str(slider_ballsize.value())}')
    save['ball_size'] = slider_ballsize.value()
    save_json()

save = {}
with open('data/data.json', 'r', encoding='utf-8') as file:
    save = json.load(file)
def save_json():
    with open('data/data.json', 'w', encoding='utf-8') as file:
        json.dump(save, file, indent=4)


btn_start_2p = QPushButton('Начать игру на двоих')
lb_gamespeed_value = QLabel('Скорость игры: 10 (рекомендуемая)')
slider_gamespeed = QSlider(Qt.Orientation.Horizontal)
slider_gamespeed.setRange(1, 20)
slider_gamespeed.setValue(10)
lb_ballsize_value = QLabel('Размер мяча: 40 (рекомендуемый)')
slider_ballsize = QSlider(Qt.Orientation.Horizontal)
slider_ballsize.setRange(20, 80)
slider_ballsize.setValue(40)


Vlayout1 = QVBoxLayout()
MainHlayout = QHBoxLayout()

Vlayout1.addWidget(btn_start_2p)
Vlayout1.addWidget(lb_gamespeed_value)
Vlayout1.addWidget(slider_gamespeed)
Vlayout1.addWidget(lb_ballsize_value)
Vlayout1.addWidget(slider_ballsize)


MainHlayout.addLayout(Vlayout1)

btn_start_2p.clicked.connect(start)
slider_gamespeed.valueChanged.connect(gamespeed)
slider_ballsize.valueChanged.connect(ballsize)

win.setLayout(MainHlayout)
win.show()
app.exec_()





