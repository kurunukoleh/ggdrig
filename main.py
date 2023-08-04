#імпорт потрібних модулів
from PyQt5.QtWidgets import *
from random import randint

#створення тексту та кнопок
app = QApplication([])
window = QWidget()
window.resize(500 , 500)
text1 = QLabel('Тицни !')
text2 = QLabel('ви скібіді тоілет !!!!')
text3 = QLabel('негри бравл старс')
button = QPushButton('натисни і получи 23331 фіріспінів і 41254215 троянів на свій пк')

#функції відповідяльні за дії кнопки при натисканні
def knopka ():
    a = str(randint(1 , 100))
    text2.setText(a)

def knopka2 ():
    a = str(randint(1 , 100))
    text3.setText(a)

#добавлення різних обєктів на лінію
line = QVBoxLayout()
line.addWidget(text1)
line.addWidget(text2)
line.addWidget(button)
line.addWidget(text3)

#відмалбовування лінії і підєднання функції до кнопки
window.setLayout(line)
button.clicked.connect(knopka)
button.clicked.connect(knopka2)

#показ вікна та оновлення кадрів
window.show()
app.exec()
