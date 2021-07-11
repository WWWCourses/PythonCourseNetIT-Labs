import sys
from PyQt5 import QtWidgets as qtw
from ui.Ui_login_form import Ui_Form

class MainWindow(qtw.QWidget,Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)


app = qtw.QApplication(sys.argv)


window = MainWindow()

# form.btn_close.clicked.connect( window.close )

window.show()

sys.exit( app.exec() )
