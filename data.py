from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QPushButton, QTextEdit
from PyQt5.QtGui import QIcon,QPalette, QBrush, QPixmap
import os
#клас мое вікно на базі стандратного вікна QWidge


class My_Window(QWidget):
    def __init__(self,width, height,x, y, title, icon,bg_color):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(width,height)
        self.move(x,y)
        self.setWindowIcon(QIcon(os.path.join(os.path.abspath(__file__+"/.."),icon)))
        self.setStyleSheet("QWidget{background-color: "+bg_color+"}")
        
            
        
    def show_win(self,main_line):
        self.setLayout(main_line)
        self.show()

class My_Button(QPushButton):
    def __init__(self,text,color):
        super().__init__(text)
        self.setStyleSheet("QPushButton{background-color: "+color+";color:pink;font-size:20px}")


class My_EditTex(QTextEdit):
    def __init__(self, text):
        super().__init__()
        self.setStyleSheet("QTextEdit{border-image:url(txt.png) 0 0 0 0; }")
        self.setHtml("<html><p align=\"center\" style=\" text-indent:40px;margin:40px;font-size:20px;font-color='#DAA520'\">"+text+"</p></html>")

    def set_style(self, text):
        self.setHtml("<html><p align=\"center\" style=\" text-indent:40px;margin:40px;font-size:20px;font-color='#DAA520'\">"+text+"</p></html>")