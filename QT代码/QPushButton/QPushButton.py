import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        button1 = QPushButton("OK", self) ## 创建名为ok的Button
        ## label的内容可以在构造函数创建，也可借助于setText函数实现后期修改
        button1.setText("&help")
        ## 设置默认按键驱动Button(Enter or Return key in the dialog)
        button1.setAutoDefault(False)
        ## 快捷键设置(简单的快捷键的设置方法：字母前加&，快捷键即为alt+字母)
        # button1.setText("&help")
        # 小Tips：使用 "&&" to represent the actual ampersand
        
   



        button1.clicked.connect(lambda: self.onClicked(button1)) ## 此处借助于lambda实现函数内部参数的传入
        '''
        1. 此处为什么使用lambda表达式：
            为将函数传入的同时，将函数参数一起传入
        2. 为什么传入函数名可以实现函数调用：
            
        '''
        

    def onClicked(self, button):
        print("Button {0} is clicked.".format(button.text())) ## 返回标签的内容


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())