import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

"""TASK
	Reimplement the login form using MySQL

	Tip: you can look at the demo code in "login_form_with_MySQL_demo.py"
		and check the link in presentation
"""

class MainWindow(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# all stuf related to showing UI:
		self.setup_ui()

		self.btn_login.clicked.connect(self.login)

		self.show();

	def setup_ui(self):
		self.setWindowTitle('Login Form')
		self.setGeometry(100, 100, 600, 300)

		# create buttons
		self.btn_cancel = qtw.QPushButton('Cancel')
		self.btn_login = qtw.QPushButton('Login')

		# create user input widgets:
		self.user_name_input = qtw.QLineEdit(self)
		self.password_input = qtw.QLineEdit(self)
		self.password_input.setEchoMode(qtw.QLineEdit.Password)

		buttons_layout = qtw.QHBoxLayout()
		buttons_layout.addWidget(self.btn_login)
		buttons_layout.addWidget(self.btn_cancel)
		print(buttons_layout.spacing())
		buttons_layout.setSpacing(100)


		# create a Form Layout and layout widgets in it
		form_layout = qtw.QFormLayout()
		form_layout.addRow('User name: ', self.user_name_input)
		form_layout.addRow('Password: ', self.password_input)
		form_layout.addRow('', buttons_layout)


		# apply the form_layout to our widget
		# this will attach our form widget's into main window
		self.setLayout(form_layout)

	def login(self):
		user_name = self.user_name_input.text()
		password = self.password_input.text()
		print(user_name, password)

		if(user_name == 'Maria' and password == 'maria123'):
			# show a message box
			qtw.QMessageBox.information(self, 'Login info', 'Welcome Maria!')
			self.close()
		else:
			qtw.QMessageBox.warning(self, 'Login error', 'Incorrect username or password')


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);
	icon_path = '../icons/vector60-5826-01.jpg'
	app.setWindowIcon(qtg.QIcon(icon_path))

	window = MainWindow()

	# window.setWindowTitle('alalbajdajd')

	sys.exit(app.exec_())
