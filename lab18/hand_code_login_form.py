import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# all stuf related to showing UI:
		self.setup_ui()

		# connect signals and slots (next lab)

		self.show();

	def setup_ui(self):
		self.setWindowTitle('Login Form')
		self.setGeometry(100, 100, 600, 300)

		# create buttons
		self.btn_cancel = qtw.QPushButton('Cancel')
		self.btn_login = qtw.QPushButton('Login')

		# create user input widgets:
		user_name_input = qtw.QLineEdit(self)
		password_input = qtw.QLineEdit(self)
		password_input.setEchoMode(qtw.QLineEdit.Password)

		buttons_layout = qtw.QHBoxLayout()
		buttons_layout.addWidget(self.btn_login)
		buttons_layout.addWidget(self.btn_cancel)
		print(buttons_layout.spacing())
		buttons_layout.setSpacing(100)


		# create a Form Layout and layout widgets in it
		form_layout = qtw.QFormLayout()
		form_layout.addRow('User name: ', user_name_input)
		form_layout.addRow('Password: ', password_input)
		form_layout.addRow('', buttons_layout)


		# apply the form_layout to our widget
		# this will attach our form widget's into main window
		self.setLayout(form_layout)



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);
	icon_path = '../icons/vector60-5826-01.jpg'
	app.setWindowIcon(qtg.QIcon(icon_path))

	window = MainWindow()

	# window.setWindowTitle('alalbajdajd')

	sys.exit(app.exec_())
