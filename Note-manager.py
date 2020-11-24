import sys
import sqlite3
import os

from datetime import datetime
from DrawNotepad import DrawNotepad
from sortWindow import SortWindow
from MainWindow_ui import Ui_Form
from note import Note

from PyQt5.Qt import *
from PyQt5.QtWidgets import QMessageBox, QInputDialog


# Класс MainWindow является главным окном, работающий с заметками типа Note и DrawNotepad
class MainWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.open_notes = []
        self.notes_titles = []
        self.setGeometry(300, 300,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())
        self.setupUi(self)
        self.table_setup('%')
        # Сигналы
        self.pushButton.clicked.connect(self.note_create)
        self.sortButton.clicked.connect(self.sort_launch)
        self.delete_all_button.clicked.connect(lambda: self.all_delete("""
        DELETE FROM Notepads WHERE title LIKE '%'"""))
        self.picture_delete_button.clicked.connect(lambda: self.pictures_delete("""
        DELETE FROM Notepads WHERE type = 'графическая'"""))
        self.delete_texts_button.clicked.connect(lambda: self.texts_delete("""
        DELETE FROM Notepads WHERE type = 'текстовая'"""))
        self.tableWidget.cellClicked.connect(self.open_event)
        self.search_line.textEdited.connect(lambda: self.table_setup('%' + self.search_line.text() + '%'))

    # close_event акрывает все октрытые заметки, а затем проверяет закрыты ли все заметки
    # Такая проверка происходит из-за того, что главное окно должно закрываться последним,
    # дабы не произошло падение программы
    def closeEvent(self, event):
        for note in self.open_notes:
            note.close()

        if self.open_notes:
            event.ignore()

    # Функция, которая определяет тип и название заметки, а зетеи создаеёт её
    def note_create(self):
        name, ok_pressed = QInputDialog.getText(self, "Имя заметки",
                                                "Введите имя заметки:")
        if ok_pressed:
            solution = QMessageBox()
            solution.setWindowTitle('Окно выбора')
            solution.setText(f'Выберите тип заметки')
            text_button = solution.addButton('Текстовая', QMessageBox.AcceptRole)
            draw_button = solution.addButton('Графическая', QMessageBox.RejectRole)
            solution.exec()
            if solution.clickedButton() == text_button:
                self.note = Note()
                type_string = 'текстовая'
            else:
                self.note = DrawNotepad()
                type_string = 'графическая'
            if not name:
                self.note.setWindowTitle("Безымянный")
            else:
                self.note.setWindowTitle(name)

            con = sqlite3.connect('notes.db')
            cur = con.cursor()

            data = (self.note.windowTitle(), type_string, str(datetime.now().date()))
            name_count = len(cur.execute("""SELECT title FROM Notepads WHERE
                    title LIKE ?""", (self.note.windowTitle() + '%',)).fetchall())
            if name_count >= 1:
                self.note.setWindowTitle(self.note.windowTitle() + f'-{name_count}')
                data = (self.note.windowTitle(), type_string, str(datetime.now().date()))
            cur.execute("""INSERT INTO Notepads VALUES(?, ?, ?)""", data)
            con.commit()

            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(len(data)):
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, j, QTableWidgetItem(data[j]))
            self.notepad_final_step()

            if type_string == 'текстовая':
                with open(r'texts\{}.txt'.format(self.note.windowTitle()), mode='tw', encoding='utf8'):
                    print(2)
                    pass
            else:
                self.note.canvas_heart.pixmap().save(r'pictures\{}.png'.format(self.windowTitle()))

        con.close()

    # Функция (слот), которая удаляет заметку из списка открытых заметок
    def data_update(self):
        self.open_notes.pop(self.open_notes.index(self.sender()))
        self.notes_titles.pop(self.notes_titles.index(self.sender().windowTitle()))
        self.table_setup('%')

    # Функция, которая открывает заметку и загружает на неё сохранённые данные
    def open_event(self, row):
        if self.tableWidget.item(row, 0).text() not in self.notes_titles:
            if self.tableWidget.item(row, 1).text() == 'текстовая':
                self.note = Note()
                with open(r'texts\{}.txt'.format(self.tableWidget.item(row, 0).text())
                        , mode='r', encoding='utf8') as file:
                    self.note.plainTextEdit.setPlainText(file.read())
            else:
                self.note = DrawNotepad()
                self.note.canvas_heart.setPixmap(QPixmap.fromImage(QImage(
                    r'pictures\{}'.format(self.tableWidget.item(row, 0).text()))))

            self.note.setWindowTitle(self.tableWidget.item(row, 0).text())
            self.notepad_final_step()

    # Функция, вносящая заметку в открытые заметки
    def notepad_final_step(self):
        self.open_notes.append(self.note)
        self.notes_titles.append(self.note.windowTitle())
        self.note.show()
        # также она дает на сигнал при закрытии заметки
        self.note.closed_window.connect(self.data_update)

    # 3 функции ниже отвечают за удаление заметок. Все они также используют функцию delete_event
    def pictures_delete(self, string):
        self.delete_event(string)
        for file in os.listdir('pictures'):
            os.remove(r'pictures\{}'.format(file))

        self.table_setup('%')

    def texts_delete(self, string):
        self.delete_event(string)
        for file in os.listdir('texts'):
            os.remove(r'texts\{}'.format(file))

        self.table_setup('%')

    def all_delete(self, string):

        self.delete_event(string)
        for file in os.listdir('texts'):
            os.remove(r'texts\{}'.format(file))
        for file in os.listdir('pictures'):
            os.remove(r'pictures\{}'.format(file))

        self.table_setup('%')

    # Функция, которая загружает данные в таблицу при запуске, изменении, а также во время поиска
    def table_setup(self, string):
        con = sqlite3.connect('notes.db')
        cur = con.cursor()

        source = cur.execute("""SELECT * FROM Notepads WHERE title LIKE ?""", (string,)).fetchall()
        self.tableWidget.setRowCount(0)
        for i in range(len(source)):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(len(source[i])):
                self.tableWidget.setItem(i, j,
                                         QTableWidgetItem(source[i][j]))

        con.close()

    # Функция, создающая диалоговое окно сортировки
    # Если пользователь подтвердит сортровку то она запускет функцию sorting
    def sort_launch(self):
        self.sortWindow = SortWindow()
        self.sortWindow.show()
        self.sortWindow.accepted.connect(self.sorting)

    # Функция, отвечающая за саму сортровку в таблице заметок
    def sorting(self):
        if self.sortWindow.sort == 'По названию':
            self.sortWindow.sort = 0
        elif self.sortWindow.sort == 'По типу':
            self.sortWindow.sort = 1
        else:
            self.sortWindow.sort = 2

        if self.sortWindow.sort_type:
            self.tableWidget.sortItems(self.sortWindow.sort, Qt.DescendingOrder)
        else:
            self.tableWidget.sortItems(self.sortWindow.sort, Qt.AscendingOrder)


# Функция, удаляющая данные заметки из базы данных notes.db
def delete_event(string):
    con = sqlite3.connect('notes.db')
    cur = con.cursor()
    cur.execute(string)
    con.commit()
    con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
