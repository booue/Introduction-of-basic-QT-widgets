import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = QLabel("input: ", self)
        label.move(0, 0)
        self.textEdit = QTextEdit(self)
        self.textEdit.move(100, 0)

        self.textEdit.setPlainText("Hello, PyQt5")
        self.textEdit.textChanged.connect(self.displayText)

    def displayText(self):
        print(self.textEdit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())


