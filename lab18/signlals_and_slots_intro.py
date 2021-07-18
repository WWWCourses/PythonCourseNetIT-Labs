import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Test')
		self.setup_ui()

		# connect slots:
		self.btn_close.clicked.connect( self.close )

		# ------------ various ways to print content of input into console ----------- #
		# print(self.input.text())
		# self.input.textChanged.connect(self.inputChangeHandle)
		self.input.textChanged.connect(print)

		# call the method with slides demo code
		self.test()

		self.show();

	def inputChangeHandle(self, content):
		# print(self.input.text()) # no need as we have the text as argument
		print(content)

	def test(self):
		self.input.editingFinished.connect(lambda: print('Edit Done'))
		self.btn_submit.clicked.connect(self.input.editingFinished)

	def setup_ui(self):
		self.btn_submit = qtw.QPushButton('Submit')
		self.btn_close = qtw.QPushButton('Close')

		self.input = qtw.QLineEdit()
		self.output = qtw.QLabel('________')

		btn_layout = qtw.QGridLayout()
		btn_layout.addWidget(self.btn_submit, 0,0)
		btn_layout.addWidget(self.btn_close, 0,1)

		main_layout=  qtw.QVBoxLayout(self)
		main_layout.addWidget(self.input)

		main_layout.addLayout(btn_layout)
		main_layout.addWidget(self.output)


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	# start event loop
	sys.exit(app.exec_())
