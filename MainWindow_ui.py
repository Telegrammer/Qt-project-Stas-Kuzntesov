# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 359)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 653, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_texts_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_texts_button.setObjectName("delete_texts_button")
        self.horizontalLayout.addWidget(self.delete_texts_button)
        self.delete_all_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_all_button.setObjectName("delete_all_button")
        self.horizontalLayout.addWidget(self.delete_all_button)
        self.picture_delete_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.picture_delete_button.setObjectName("picture_delete_button")
        self.horizontalLayout.addWidget(self.picture_delete_button)
        self.mainLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.search_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.search_line.setObjectName("search_line")
        self.horizontalLayout_2.addWidget(self.search_line)
        self.mainLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.mainLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.mainLayout.addWidget(self.pushButton)
        self.sortButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sortButton.setObjectName("sortButton")
        self.mainLayout.addWidget(self.sortButton)

        self.setLayout(self.mainLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Система заметок"))
        self.delete_texts_button.setText(_translate("Form", "Удалить все текстовые заметки"))
        self.delete_all_button.setText(_translate("Form", "Удалить все заметки"))
        self.picture_delete_button.setText(_translate("Form", "Удалить все графические заметки"))
        self.label.setText(_translate("Form", "Поиск:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Дата создания"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Тип"))
        self.pushButton.setText(_translate("Form", "Создать заметку"))
        self.sortButton.setText(_translate("Form", "Сортировать"))
