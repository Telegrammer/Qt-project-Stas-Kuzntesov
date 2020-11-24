from sort_windowUI import Ui_Form
from PyQt5.QtWidgets import QDesktopWidget, QDialog
from PyQt5.QtCore import Qt


# Класс SortWindow является диалоговым окном сортировки таблицы заметок главного окна класса MainWindow
class SortWindow(QDialog, Ui_Form):

    def __init__(self):
        super().__init__()
        self.sort = 'По названию'
        self.sort_type = False
        self.setGeometry(0, 0,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.result_button.clicked.connect(lambda: self.accept())
