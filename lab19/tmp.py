import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Main')

		self.layout = qtw.QVBoxLayout(self)

		self.line_edit = qtw.QLineEdit()
		self.btn_ok = qtw.QPushButton('Ok')
		self.layout.addWidget(self.line_edit)
		self.layout.addWidget(self.btn_ok)

		# self.line_edit.textChanged.connect(self.on_click)
		# TODO: make it work
		self.btn_ok.clicked.connect(self.on_click(1))

		self.show();

	# custom slot
	def on_click(self, data, x):
		print(x)

		return lambda x: print(x**2)




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
