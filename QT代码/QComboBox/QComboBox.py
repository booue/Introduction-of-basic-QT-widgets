import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QWidget


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.combo = QComboBox(self)
        ## 添加元素addItem
        self.combo.addItem("Apple")
        self.combo.addItem("HuaWei")
        self.combo.addItem("XiaoMi")
        self.combo.addItem("Oppo")

        ## 添加元素insertItem(index,str)或者insertItems
        self.combo.insertItem(1,"Meizu")
        ## change item(setItemText)
        self.combo.setItemText(1,"Chuizi")
        ## removeItem(index)
        # self.combo.removeItem(1)
        ## clear(all items can be removed)
        
        ## itemText(the text of a numbered item)
        # string = self.combo.itemText(1)
        # print(string)

        ## setMaxCount(int)
        ## count
        
        ## comboBox每个词条内容可编辑
        # self.combo.setEditable(True)
        
        ## 设置内容是否可以重复
        self.combo.setDuplicatesEnabled(True)
        
        


        self.combo.currentIndexChanged.connect(self.onCurrentIndex)

    def onCurrentIndex(self, index):
        ## the text of the current item
        print("current item is {0}".format(self.combo.currentText()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())