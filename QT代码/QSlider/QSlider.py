import sys
from PyQt5.QtWidgets import QApplication, QSlider, QWidget
from PyQt5.QtCore import Qt


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ## 水平滑栏
        # slider = QSlider(Qt.Horizontal, self)
        ## 竖直滑栏
        slider = QSlider(Qt.Vertical, self)
        ## 设置Slider的上下限
        slider.setMaximum(20)
        slider.setMinimum(10)

        slider.valueChanged.connect(self.onValueChanged)

    def onValueChanged(self, value):
        print("current value is {0}".format(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())