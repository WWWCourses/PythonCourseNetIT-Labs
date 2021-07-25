import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Demo for using StyleSheets')

		# ------------------------------ create widgets ------------------------------ #
		label1 = qtw.QLabel('Label 1')
		label2 = qtw.QLabel('Label 2')
		label3 = qtw.QLabel('Label 3')

		button1 = qtw.QPushButton('Button1')
		button2 = qtw.QPushButton('Button2')

		text_edit = qtw.QTextEdit()

		# -------------------------- add widgets to layouts -------------------------- #
		labels_layout = qtw.QHBoxLayout()
		labels_layout.addWidget(label1)
		labels_layout.addWidget(label2)
		labels_layout.addWidget(label3)

		main_layout = qtw.QVBoxLayout(self)
		main_layout.addLayout(labels_layout)
		main_layout.addWidget(button1)
		main_layout.addWidget(button2)
		main_layout.addWidget(text_edit)

		# ------------------------------ Styling Widgets ----------------------------- #
		# set style on specific widget.
		# note, that this will overwrite the style from file
		label1_style = f"""
			color: white;
			background-color: red;
			border: 1px solid black;
			border-radius: 10px;
		"""
		label1.setStyleSheet(label1_style)

		# load style from file:
		style_file = './main.css'
		with open(style_file, 'r') as fh:
			style_sheet = fh.read()

		# set style on all widgets:
		self.setStyleSheet(style_sheet)


		# ----------------------------- Show Main Widget ----------------------------- #
		self.setLayout(main_layout)
		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
