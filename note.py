import sqlite3
from datetime import datetime
from os import path
from note_ui import Ui_Form

from PyQt5 import QtCore, QtWidgets


# Класс Note является заметкой текстового типа
class Note(Ui_Form):
    closed_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.font_color = '#000000'
        self.notepad_color = ''
        self.setGeometry(0,
                         0,
                         QtWidgets.QDesktopWidget().availableGeometry().width(),
                         QtWidgets.QDesktopWidget().availableGeometry().height())
        self.setupUi(self)
        self.colorButton.clicked.connect(lambda: self.notepad_color_update(''))
        self.textColorButton.clicked.connect(lambda: self.font_update(''))

    # close_event изначально пытается сохранить данные в текстовой файл, имеющий такое же название что и окно
    # Если же заметка новая или старые данные были удалены, то close_event создаёт новый файл с таким же названием
    def closeEvent(self, event):
        flag = True
        text_path = r'texts\{}.txt'.format(self.windowTitle())
        try:
            with open(text_path, mode='r', encoding='utf8') as file:
                pass
        except FileNotFoundError:
            with open(text_path, mode='tw', encoding='utf8') as file:
                pass
        finally:
            with open(text_path, mode='r', encoding='utf8') as file:
                source = file.read()
                if source != self.plainTextEdit.toPlainText():
                    flag = False
                    solution = QtWidgets.QMessageBox()
                    solution.setWindowTitle('Окно сохранения')
                    solution.setText(f'Сохранить заметку {self.windowTitle()}?')
                    accept_button = solution.addButton('Да', QtWidgets.QMessageBox.AcceptRole)
                    reject_button = solution.addButton('Нет', QtWidgets.QMessageBox.RejectRole)
                    cancel_button = solution.addButton("Отмена", QtWidgets.QMessageBox.NoRole)
                    solution.exec()

                    if solution.clickedButton() == cancel_button:
                        event.ignore()
                    else:
                        if solution.clickedButton() == accept_button:
                            with open(text_path, mode='w', encoding='utf8') as result_file:
                                result_file.write(self.plainTextEdit.toPlainText())
                        self.closed_window.emit()

                con = sqlite3.connect('notes.db')
                cur = con.cursor()
                source = cur.execute("""SELECT * FROM Notepads 
                                        WHERE title = ?""", (self.windowTitle(),)).fetchall()
                if not source:
                    data = (self.windowTitle(), 'текстовая', datetime.now().date())
                    cur.execute("""INSERT INTO Notepads VALUES(?, ?, ?)""", data)
                    con.commit()

                con.close()

            if flag:
                self.closed_window.emit()

    # Функции отвечающие за графические изменения самой заметки
    def set_notepad_color(self, notepad_color):
        self.setStyleSheet("background-color: {}".format(notepad_color))
        self.plainTextEdit.setStyleSheet(
            "background-color: {}".format(notepad_color))
        self.colorButton.setStyleSheet(
            "background-color: {}".format(notepad_color))
        self.textColorButton.setStyleSheet(
            "background-color: {}".format(notepad_color))
        if notepad_color == '#000000' and self.font_color == notepad_color:
            self.colorButton.setStyleSheet("QPushButton { color: white;}""")
            self.textColorButton.setStyleSheet("QPushButton { color: white;}")
            self.plainTextEdit.setStyleSheet("QPlainTextEdit {color: white;}")
        elif self.font_color != 'black':
            self.font_update(self.font_color)
        self.notepad_color = notepad_color

    def set_font_color(self, font_color):
        self.colorButton.setStyleSheet("color: {}""".format(font_color))
        self.textColorButton.setStyleSheet("color: {}""".format(font_color))
        self.plainTextEdit.setStyleSheet("color: {}""".format(font_color))
        self.font_color = font_color

    def notepad_color_update(self, notepad_color):
        if not notepad_color:
            notepad_color = QtWidgets.QColorDialog.getColor()
            if notepad_color.isValid():
                self.set_notepad_color(notepad_color.name())
        else:
            self.set_notepad_color(notepad_color)

    def font_update(self, font_color):
        if not font_color:
            font_color = QtWidgets.QColorDialog.getColor()
            if font_color.isValid():
                self.set_font_color(font_color.name())
        else:
            self.set_font_color(font_color)
