import sys
from PyQt5.QtWidgets import QApplication, QInputDialog, QWidget, QPushButton


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        button = QPushButton("OK", self) ## 在组件上添加一个按钮

        self.resize(800, 600)
        button.clicked.connect(self.onOKClicked)

    def onOKClicked(self):

        # QInputDialog提供多个用户选择getItem,getText,getInt,getDouble
        items = ["C++", "Python", "Java", "Go"]
        item, ok = QInputDialog.getItem(self, "Select an Item", "Programing Language", items, 1, True)
        if ok and item:
            print("selected item: ", item)

        text, ok = QInputDialog.getText(self, "Input an text", "text:")
        if ok:
            print("input text: ", text)

        ## int提供内部选择的功能(输入小数，输不进去)
        num, ok = QInputDialog.getInt(self, "Input an int number", "num:")
        if ok:
            print("input num: ", num)
        ## 用户实际进行选择(按下OK键后，ok变量接受为True)
        print(ok)

        ## 内部会自动携带换行符
        text, ok = QInputDialog.getMultiLineText(self, "Input MultiLineText", "Text:")
        if ok:
            print("input text: ", text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())