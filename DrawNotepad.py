import sys
import sqlite3
from datetime import datetime

from PyQt5.QtCore import pyqtSignal
from DrawNotepad_ui import Ui_Form
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QColorDialog


# Класс DrawNotepad является заметкой графического типа
class DrawNotepad(QWidget, Ui_Form):
    closed_window = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.color = (0, 0, 0)
        self.setGeometry(0, 0,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())
        self.setupUi(self)

        self.canvas = QPixmap(self.frameGeometry().width(), self.frameGeometry().height())
        self.canvas.fill(QColor(255, 255, 255))
        self.canvas_heart.setPixmap(self.canvas)

        self.buttonGroup.buttonClicked.connect(self.set_color)
        self.colorSelectButton.clicked.connect(self.set_color_alt)
        self.spinBox.valueChanged.connect(lambda: self.canvas_heart.set_pen_width(self.spinBox.value()))
        self.backColorSelect.clicked.connect(self.set_back_color)

    # close_event сохранет данные в папке pictures, а также в базе данных notes.db
    def closeEvent(self, event):
        self.canvas_heart.pixmap().save(r'pictures\{}.png'.format(self.windowTitle()))

        con = sqlite3.connect('notes.db')
        cur = con.cursor()
        source = cur.execute("""SELECT * FROM Notepads 
                                                WHERE title = ?""", (self.windowTitle(),)).fetchall()
        if not source:
            data = (self.windowTitle(), 'графическая', datetime.now().date())
            cur.execute("""INSERT INTO Notepads VALUES(?, ?, ?)""", data)
            con.commit()

        con.close()

        self.closed_window.emit()

    # Функции, отвечающие за изменение цвета кисти и холста
    def set_color(self, button):
        self.color = button.styleSheet().split(';')[0]
        self.color = self.color[self.color.index('(') + 1:self.color.index(')')]
        self.color = [int(number) for number in self.color.split(', ')]
        self.color = QColor(self.color[0], self.color[1], self.color[2])
        self.canvas_heart.set_pen_color(self.color)

    def set_color_alt(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas_heart.set_pen_color(color)

    def set_back_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.fill(color)
            self.canvas_heart.setPixmap(self.canvas)
