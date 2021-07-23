import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

# from ui.login_form import LoginForm

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My App')

		# ------------------------- create and atach widgets ------------------------- #
		self.label = qtw.QLabel('Initial Text')
		self.btn_change = qtw.QPushButton('change text')

		self.main_layout = qtw.QVBoxLayout()
		self.main_layout.addWidget(self.label)
		self.main_layout.addWidget(self.btn_change)
		self.main_layout.setContentsMargins(50,50,50,50)
		self.setLayout(self.main_layout)

		self.show()

		# ---------------------------------- signals --------------------------------- #
		self.btn_change.clicked.connect(self.onChangeClicked)


	def onChangeClicked(self):
		# show pop up
		# self.popup_form=FormWindow()
		# self.label.setText('changed text')

		self.form_widget = FormWindow(self.label.text())

		# # TODO: finish demo with tightly coupled objects
		# form_data = self.form_widget.edit.text()
		# print(form_data)
		# self.label.setText(form_data)

		# loosly coupled (implemented with custom signals) is better
		self.form_widget.sig_submit.connect(self.label.setText)



class FormWindow(qtw.QWidget):
	# cretate custom signal which will cary a string data type data:
	sig_submit = qtc.pyqtSignal(str);

	def __init__(self , msg):
		super().__init__()
		self.setWindowTitle('My Form')

		# ------------------------- create and atach widgets ------------------------- #
		self.edit = qtw.QLineEdit(msg)
		self.btn_submit = qtw.QPushButton('Submit')

		self.setLayout(qtw.QVBoxLayout())
		self.layout().addWidget(self.edit)
		self.layout().addWidget(self.btn_submit)

		# will be shown by parent
		self.show();

		# ---------------------------------- signals --------------------------------- #
		self.btn_submit.clicked.connect(self.onSubmit)

	@qtc.pyqtSlot(bool)
	def onSubmit(self):

		# send  edit.text() to parent
		self.sig_submit.emit(self.edit.text())
		self.close()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())