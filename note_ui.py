from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")

        Form.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 5, 391, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        plainTextEdit_font = self.plainTextEdit.font()
        plainTextEdit_font.setBold(True)
        self.plainTextEdit.setFont(plainTextEdit_font)
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.colorButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton.sizePolicy().hasHeightForWidth())
        self.colorButton.setSizePolicy(sizePolicy)
        self.colorButton.setObjectName("colorButton")
        self.colorButton.setText("Изменить цвет заметки")
        colorButton_font = self.colorButton.font()
        colorButton_font.setBold(True)
        self.colorButton.setFont(colorButton_font)
        self.horizontalLayout.addWidget(self.colorButton)

        self.textColorButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textColorButton.sizePolicy().hasHeightForWidth())
        self.textColorButton.setSizePolicy(sizePolicy)
        self.textColorButton.setObjectName("textColorButton")
        self.textColorButton.setText("Изменить цвет шрифта")
        textColorButton_font = self.textColorButton.font()
        textColorButton_font.setBold(True)
        self.textColorButton.setFont(textColorButton_font)
        self.horizontalLayout.addWidget(self.textColorButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.setLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.setWindowIcon(QIcon('note_image.png'))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
