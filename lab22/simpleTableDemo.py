import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class SimpleTable(qtw.QTableWidget):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent)
		self.rows = kwargs["rows"]
		self.cols = kwargs["cols"]

		self.setRowCount(self.rows);
		self.setColumnCount(self.cols);


		# set column headings
		column_heading = []
		for i in range(1,self.cols+1):
			column_heading.append(f"Heading{i}")

		self.setHorizontalHeaderLabels(column_heading);

		self.setMinimumWidth(self.cols*100);
		self.setMinimumHeight(self.rows*50);

		# set table values
		for row in range(self.rows):
				for col in range(self.cols):
						self.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row+1},{col+1}'))

		# resize cells to content:
		self.resizeColumnsToContents();
		self.resizeRowsToContents();

		# actions
		self.tableAction()

	def tableAction(self):
		self.add_above_action = qtw.QAction("Add row above", self)
		self.add_above_action.triggered.connect(lambda: self.insertRow(self.currentRow()))


	def contextMenuEvent(self, event):
		context_menu = qtw.QMenu(self)
		context_menu.addAction(self.add_above_action)
		context_menu.addAction("Add row bellow")
		context_menu.exec_(event.globalPos())




class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')

		# create table widget:
		table = SimpleTable(self, rows=3, cols=7);

		# create button widgets:
		buttonOK = qtw.QPushButton("OK", self)
		buttonClose = qtw.QPushButton("Click Me", self)
		buttonOK.setObjectName("ok")
		buttonClose.setObjectName("close")

		# create layout:
		layout = qtw.QVBoxLayout(self)
		layout.addWidget(table)
		layout.addWidget(buttonOK)
		layout.addWidget(buttonClose)


		# self.uiCreateTable()
		self.applyStyle()

		self.show();

	def applyStyle(self):
		with open('./table.css','r') as f:
			style = f.read()

		self.setStyleSheet(style)

	def someOtherMethod(self):
		pass


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
