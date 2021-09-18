# account_manager.py
# Import necessary modules
import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
    QPushButton, QComboBox, QTableView, QHeaderView,
    QHBoxLayout, QVBoxLayout, QSizePolicy, QMessageBox)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery,
    QSqlRelationalTableModel, QSqlRelation,
    QSqlRelationalDelegate)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class AccountManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(1000, 600)
        self.setWindowTitle('10.1 – Account Management GUI')
        self.createConnection()
        self.createTable()
        self.setupWidgets()
        self.show()

    def createConnection(self):
        database = QSqlDatabase.addDatabase("QSQLITE") # SQLite version 3
        database.setDatabaseName("./users.db")
        if not database.open():
            print("Unable to open data source file.")
            sys.exit(1) # Error code 1 - signifies error

        # Check if the tables we need exist in the database
        tables_needed = {'users', 'orders'}
        tables_not_found = tables_needed - set(database.tables())
        if tables_not_found:
            QMessageBox.critical(None, 'Error',
                f'The following tables are missing from the database:{tables_not_found}')
            sys.exit(1) # Error code 1 - signifies error

    def createTable(self):
        """
        Set up the model, headers and populate the model.
        """
        self.model = QSqlRelationalTableModel()
        self.model.setTable('accounts')
        self.model.setRelation(self.model.fieldIndex('country_id'),QSqlRelation('countries', 'id', 'country'))
        self.model.setHeaderData(self.model.fieldIndex('id'),Qt.Horizontal, "ID")
        self.model.setHeaderData(self.model.fieldIndex('employee_id'),Qt.Horizontal, "User ID")
        self.model.setHeaderData(self.model.fieldIndex('first_name'),Qt.Horizontal, "First")
        self.model.setHeaderData(self.model.fieldIndex('last_name'),Qt.Horizontal, "Last")
        self.model.setHeaderData(self.model.fieldIndex('email'),Qt.Horizontal, "E-mail")
        self.model.setHeaderData(self.model.fieldIndex('department'),Qt.Horizontal, "Dept.")
        self.model.setHeaderData(self.model.fieldIndex('country_id'),Qt.Horizontal, "Country")

        # Populate the model with data
        self.model.select()

    def setupWidgets(self):
        """
        Create instances of widgets, the table view and set layouts.
        """
        icons_path = "icons"
        title = QLabel("Account Management System")
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        title.setStyleSheet("font: bold 24px")
        add_record_button = QPushButton("Add User")
        add_record_button.setIcon(QIcon(os.path.join(icons_path, "add_user.png")))
        add_record_button.setStyleSheet("padding: 10px")
        add_record_button.clicked.connect(self.addRecord)
        del_record_button = QPushButton("Delete")
        del_record_button.setIcon(QIcon(os.path.join(icons_path, "trash_can.png")))
        del_record_button.setStyleSheet("padding: 10px")
        del_record_button.clicked.connect(self.deleteRecord)
        # Set up sorting combo box
        sorting_options = ["Sort by ID", "Sort by User ID", "Sort byFirst Name", "Sort by Last Name", "Sort by Department", "Sort byCountry"]
        sort_name_cb = QComboBox()
        sort_name_cb.addItems(sorting_options)
        sort_name_cb.currentTextChanged.connect(self.setSortingOrder)
        buttons_h_box = QHBoxLayout()
        buttons_h_box.addWidget(add_record_button)
        buttons_h_box.addWidget(del_record_button)
        buttons_h_box.addStretch()
        buttons_h_box.addWidget(sort_name_cb)
        # Widget to contain editing buttons
        edit_buttons = QWidget()
        edit_buttons.setLayout(buttons_h_box)
        # Create table view and set model
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        # Instantiate the delegate
        delegate = QSqlRelationalDelegate(self.table_view)
        self.table_view.setItemDelegate(delegate)
        # Main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(title, Qt.AlignLeft)
        main_v_box.addWidget(edit_buttons)
        main_v_box.addWidget(self.table_view)
        self.setLayout(main_v_box)

    def addRecord(self):
        """
        Add a new record to the last row of the table.
        """
        last_row = self.model.rowCount()
        self.model.insertRow(last_row)
        id = 0
        query = QSqlQuery()
        query.exec_("SELECT MAX (id) FROM accounts")
        if query.next():
            id = int(query.value(0))
    def deleteRecord(self):
        """
        Delete an entire row from the table.
        """
        current_item = self.table_view.selectedIndexes()
        for index in current_item:
            self.model.removeRow(index.row())
        self.model.select()
    def setSortingOrder(self, text):
        """
        Sort the rows in table.
        """
        if text == "Sort by ID":
            self.model.setSort(self.model.fieldIndex('id'),Qt.AscendingOrder)
        elif text == "Sort by User ID":
            self.model.setSort(self.model.fieldIndex('employee_id'),Qt.AscendingOrder)
        elif text == "Sort by First Name":
            self.model.setSort(self.model.fieldIndex('first_name'),Qt.AscendingOrder)
        elif text == "Sort by Last Name":
            self.model.setSort(self.model.fieldIndex('last_name'),Qt.AscendingOrder)
        elif text == "Sort by Department":
            self.model.setSort(self.model.fieldIndex('department'),Qt.AscendingOrder)
        elif text == "Sort by Country":
            self.model.setSort(self.model.fieldIndex('country'),Qt.AscendingOrder)

        self.model.select()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AccountManager()
    sys.exit(app.exec_())