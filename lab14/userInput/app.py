import sys

from PyQt5.QtWidgets import QApplication,QWidget
from Ui_userInput import Ui_MainWindow

def clickHandler(line):
    print('Your name: ' + line.text())

""" TASK:
	Instantiate Ui_MainWindow and using the "../demos/read_text.py" as example try to make it work here
"""

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App Works')
window.setGeometry(100, 100, 500, 500)

window.show()
sys.exit(app.exec_())