import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from ui.Ui_login_form import Ui_Form

class MainWindow(qtw.QWidget, Ui_Form):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		# ------------------------------ your code here ------------------------------ #
		self.setupUi(self)
		self.close()

	# TODO: discuss why not working
	def close(self):
		self.btn_close.clicked.connect( self.close )

app = qtw.QApplication(sys.argv)

window = MainWindow()

# form = Ui_Form()

window.show()

sys.exit( app.exec() )
