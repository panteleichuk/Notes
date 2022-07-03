from PyQt5.QtWidgets import QApplication, QWidget,QListWidget, QLineEdit, QTextEdit,QPushButton,QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from data import*
from application import app



#головна лінія
main_line = QHBoxLayout()
#ствоюємо віджети
#для тексту замітки 
edit_text_note = My_EditTex("Enter text note....")

# edit_text_note.setStyleSheet("QTextEdit{border-image:url(txt.png) 0 0 0 0; }")
# edit_text_note.setText()
#для списку усіх заміток, за назвою
list_note = QListWidget()
list_note.setStyleSheet("QListWidget{border-image:url(list.png) 0 0 0 0;font-size:18px;color:red; }")
#кнопка створити замітку
btn_add_note = My_Button("Creat note","#696969")

#кнопка видалити замітку
btn_del_note = My_Button("Delet note","#696969")
#кнопка зберігти замітку
btn_save_note = My_Button("Save note","#696969")
#для списку-тегів
list_teg = QListWidget()
list_teg.setStyleSheet("QListWidget{border-image:url(list.png) 0 0 0 0;font-size:18px; }")
#для ввода назви тегу
edit_teg = QLineEdit()
edit_teg.setStyleSheet("QLineEdit{background-color:#696969; }")
edit_teg.setText("Enter teg")
#кнопка додати тег до замітки #696969
btn_add_teg = My_Button("Add teg","#696969")
#кнопка відкріпити тег від замітки
btn_del_teg = My_Button("Delet teg","#696969")
#кнопка пошук заміток за тегом
btn_find_note = My_Button("Find for teg","#696969")

#створюємо основні вертикаль 2 лінії
#1 лінія - для віджета-текста замітки
line_v1 = QVBoxLayout()
#2лінія - для усіх інших віджетів(вони будуть у стовпчик) зправа
line_v2 = QVBoxLayout()

#лінії для правої частини - 5 горизонтальних ліній
#1 лінія - для кнопок створити та видалити
line_h1 = QHBoxLayout()
#2 лінія - для кнопки зберігти замітку
line_h2 = QHBoxLayout()
#3 лінія - для кнопок додати та відкріпити тег
line_h3 = QHBoxLayout()
#4 лінія - для кнопки пошук
line_h4 = QHBoxLayout()

line_h1.addWidget(btn_add_note)
line_h1.addWidget(btn_del_note)
line_h2.addWidget(btn_save_note)
line_h3.addWidget(btn_add_teg)
line_h3.addWidget(btn_del_teg)
line_h4.addWidget(btn_find_note)

line_v1.addWidget(edit_text_note)
line_v2.addWidget(list_note)
line_v2.addLayout(line_h1)
line_v2.addLayout(line_h2)
line_v2.addWidget(list_teg)
line_v2.addWidget(edit_teg)
line_v2.addLayout(line_h3)
line_v2.addLayout(line_h4)

main_line.addLayout(line_v1)
main_line.addLayout(line_v2)
