import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

	def __init__(self):
		super().__init__()

		self.setWindowTitle('SimpleText Editor')
		self.setGeometry(500, 500, 600, 400)

		# ------------------------------ central widget ------------------------------ #
		self.textedit = qtw.QTextEdit()
		self.setCentralWidget(self.textedit)

		# ------------------------------ menu bar ------------------------------ #
		menubar = self.menuBar()
		# bar = QtWidgets.QMainWindow.menuBar()

		# menubar = self.add
		# add menu items
		file_menu = menubar.addMenu('F&ile')
		edit_menu = menubar.addMenu('&Edit')
		help_menu = menubar.addMenu('&Help')

		# ---------------------------------- toolbar --------------------------------- #
		toolbar = self.addToolBar('File')

		toolbar.setMovable(True)
		toolbar.setFloatable(False)
		toolbar.setAllowedAreas(
			qtc.Qt.TopToolBarArea |
			qtc.Qt.BottomToolBarArea
		)

		# -------------------------------- add Actions ------------------------------- #
		open_action = file_menu.addAction('Open', self.open_file)
		save_action = file_menu.addAction('Save')

		# add separator
		file_menu.addSeparator()
		quit_action = file_menu.addAction('Quit', self.close)

		undo_action = edit_menu.addAction('Undo', self.textedit.undo)

		# create a QAction manually
		redo_action = qtw.QAction('Redo', self)
		redo_action.triggered.connect(self.textedit.redo)

		# Actions, which opens custom dialog
		edit_menu.addAction(redo_action)

		edit_menu.addAction('Set Font…', self.set_font)
		edit_menu.addAction('Settings…', self.show_settings)

		help_action = qtw.QAction(
			self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton),
			'Help',
			self,  # important to pass the parent!
			# add signal
			# triggered=lambda: self.StatusBar().showMessage(
			# 		'Sorry, no help yet!'
			# )

		)
		toolbar.addAction(help_action)

		# ----------------------------------- Dock ----------------------------------- #
		dock = qtw.QDockWidget("Replace")
		self.addDockWidget(qtc.Qt.LeftDockWidgetArea, dock)

		# set dock widget to move and float (but not closeable)
		dock.setFeatures(
			qtw.QDockWidget.DockWidgetMovable |
			qtw.QDockWidget.DockWidgetFloatable
		)

		replace_widget = qtw.QWidget()
		replace_widget.setLayout(qtw.QVBoxLayout())
		dock.setWidget(replace_widget)

		self.search_text_input = qtw.QLineEdit(placeholderText='search')
		self.replace_text_input = qtw.QLineEdit(placeholderText='replace')
		search_and_replace_btn = qtw.QPushButton(
			"Search and Replace",
			clicked=self.search_and_replace
			)
		replace_widget.layout().addWidget(self.search_text_input)
		replace_widget.layout().addWidget(self.replace_text_input)
		replace_widget.layout().addWidget(search_and_replace_btn)
		replace_widget.layout().addStretch()

		# --------------------------------- StatusBar -------------------------------- #
		# The long way
		# status_bar = qtw.QStatusBar()
		# self.setStatusBar(status_bar)
		# status_bar.showMessage('Welcome to My Text Editor')

		self.statusBar().showMessage('Welcome to My Text Editor', 1000)
		# self.statusBar().addPermanentWidget(qtw.QLabel('Permanent wodget'))

		charcount_label = qtw.QLabel("chars: 0")
		self.textedit.textChanged.connect(
			lambda: charcount_label.setText( "chars: " + str(len(self.textedit.toPlainText())) )
		)
		self.statusBar().addPermanentWidget(charcount_label)


		self.show();

	def set_font(self):
		pass

	def show_settings(self):
		pass

	def search_and_replace(self):
		pass

	def open_file(self):
		pass




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
