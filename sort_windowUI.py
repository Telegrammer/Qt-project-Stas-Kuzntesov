from PyQt5 import QtCore, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 250)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.widget.setObjectName("widget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.widget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.sortWorklLayout = QtWidgets.QVBoxLayout()
        self.sortWorklLayout.setObjectName("sortWorklLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.sortWorklLayout.addWidget(self.label)
        self.name_sort_button = QtWidgets.QRadioButton(self.widget)
        self.name_sort_button.setChecked(True)
        self.name_sort_button.setObjectName("name_sort_button")
        self.sortButtonGroup = QtWidgets.QButtonGroup(Form)
        self.sortButtonGroup.setObjectName("sortButtonGroup")
        self.sortButtonGroup.addButton(self.name_sort_button)
        self.sortWorklLayout.addWidget(self.name_sort_button)
        self.type_sort_button = QtWidgets.QRadioButton(self.widget)
        self.type_sort_button.setObjectName("type_sort_button")
        self.sortButtonGroup.addButton(self.type_sort_button)
        self.sortWorklLayout.addWidget(self.type_sort_button)
        self.date_isort_button = QtWidgets.QRadioButton(self.widget)
        self.date_isort_button.setObjectName("date_isort_button")
        self.sortButtonGroup.addButton(self.date_isort_button)
        self.sortWorklLayout.addWidget(self.date_isort_button)
        self.mainLayout.addLayout(self.sortWorklLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.plusRadioButton = QtWidgets.QRadioButton(self.widget)
        self.plusRadioButton.setChecked(True)
        self.plusRadioButton.setObjectName("plusRadioButton")
        self.typeButtonGroup = QtWidgets.QButtonGroup(Form)
        self.typeButtonGroup.setObjectName("typeButtonGroup")
        self.typeButtonGroup.addButton(self.plusRadioButton)
        self.verticalLayout.addWidget(self.plusRadioButton)
        self.minusRadioButton = QtWidgets.QRadioButton(self.widget)
        self.minusRadioButton.setObjectName("minusRadioButton")
        self.typeButtonGroup.addButton(self.minusRadioButton)
        self.verticalLayout.addWidget(self.minusRadioButton)
        self.mainLayout.addLayout(self.verticalLayout)
        self.result_button = QtWidgets.QPushButton(self.widget)
        self.result_button.setObjectName("result_button")
        self.mainLayout.addWidget(self.result_button)

        self.setLayout(self.mainLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Окно сортировки"))
        self.label.setText(_translate("Form", "Способы сортировки:"))
        self.name_sort_button.setText(_translate("Form", "По названию"))
        self.type_sort_button.setText(_translate("Form", "По типу"))
        self.date_isort_button.setText(_translate("Form", "По дате"))
        self.label_2.setText(_translate("Form", "Типы сортировки:"))
        self.plusRadioButton.setText(_translate("Form", "Возрастающий (c графических)"))
        self.minusRadioButton.setText(_translate("Form", "Убывающий (с текстовых)"))
        self.result_button.setText(_translate("Form", "Сортировать"))
