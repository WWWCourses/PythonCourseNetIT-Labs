import sys

from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App Works')
window.setGeometry(200, 0, 500, 200)


window.show()
sys.exit(app.exec_())
