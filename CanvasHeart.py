from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


# Класс CanvasHeart является скелетом для холста заметки класса DrawNotepad
class CanvasHeart(QLabel):
    def __init__(self, parent=None):
        super(CanvasHeart, self).__init__(parent)
        self.last_x, self.last_y = None, None
        self.pen_color = QColor('#000000')
        self.pen_width = 5
        self.setContentsMargins(0, 0, 0, 0)

    # 2 Функции ниже отвечают за изменяемые характеристики кисти (Толщина, цвет)
    def set_pen_color(self, color):
        self.pen_color = QColor(color)

    def set_pen_width(self, width):
        self.pen_width = width

    # mouseMoveEvent отвечает за само рисование на холсте заметки
    def mouseMoveEvent(self, event):
        if self.last_x is None:
            self.last_x = event.x()
            self.last_y = event.y()
            return

        painter = QPainter(self.pixmap())
        painter.setPen(QPen(self.pen_color, self.pen_width,
                            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.last_x, self.last_y + 12, event.x(), event.y() + 12)
        painter.end()
        self.update()

        self.last_x = event.x()
        self.last_y = event.y()

    def mouseReleaseEvent(self, event):
        self.last_x = None
        self.last_y = None
