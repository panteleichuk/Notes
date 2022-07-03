from PyQt5.QtWidgets import (QApplication, QWidget,QListWidget, 
QLineEdit, QTextEdit,QPushButton,QHBoxLayout, QVBoxLayout, QInputDialog)
from PyQt5.QtGui import QIcon
from application import app
from window import*
from data import*
from wr_json import*
#вікно - свій клас, або стандартне вікно та налаштування вікна- розмір, заголовок іт.д
window = My_Window(800,650,100,100,"Easly Editor","icon.png",'#FFC0CB')

def show_not():
    note = list_note.selectedItems()[0].text()
    list_teg.clear()
    edit_text_note.clear()
    list_teg.addItems(notes_dict[note]["теги"])
    # edit_text_note.setPlainText(notes_dict[note]["текст"])
    # edit_text_note.setHtml("<font color = 'red' size = '10'  left = '200px'></font> "+notes_dict[note]["текст"])
    # edit_text_note.setHtml("<html><p align=\"center\" style=\" text-indent:40px;margin:40px;font-size:20px;font-color='#DAA520'\">"+notes_dict[note]["текст"]+"</p></html>")
    edit_text_note.set_style(notes_dict[note]["текст"])

def add_note():  
    notes_name, result = QInputDialog.getText(window,"Add new note", "Enter name new note")
    print(notes_name)
    print(result)
    if result and notes_name:
        notes_dict[notes_name] = {
                                    "текст" : "NEW TEXT",
                                    "теги" : ["new_teg"]
        }
    
    list_note.clear()
    list_note.addItems(notes_dict)
    list_note.setCurrentRow(len(notes_dict)-1)
    edit_text_note.set_style("New note")
    list_teg.clear()
    list_teg.addItems(notes_dict[notes_name]["теги"])

def del_note():
    note = list_note.selectedItems()[0].text()
    del notes_dict[note]
    write_json("notes.jsom",notes_dict)
    list_note.clear()
    list_teg.clear()
    edit_text_note.setPlainText("")
    list_note.addItems(notes_dict)
def save_note():  
    # if len(list_note.selectedItems())>0:
    #     note = list_note.selectedItems()[0].text()
    #     print(note)
    #     text = edit_text_note.toPlainText()
    #     print(text)
    #     notes_dict[note]["текст"] = text
    #     write_json("notes.json",notes_dict)
    if (list_note.currentItem()):
        note = list_note.currentItem().text()
        text = edit_text_note.toPlainText()
        notes_dict[note]["текст"] = text
        write_json("notes.json",notes_dict)
        

def add_teg():
    note = list_note.selectedItems()[0].text()
    teg = edit_teg.text()
    print(teg)
    list_teg.addItem(teg)
    notes_dict[note]["теги"].append(teg)
    write_json("notes.json",notes_dict)
  
    edit_teg.clear()
def del_teg():
    note = list_note.selectedItems()[0].text()
    teg = list_teg.selectedItems()[0].text()
    del notes_dict[note]["теги"][teg]
    list_teg.clear()
    list_teg.addItems(notes_dict[note]["теги"])

def find_note():
    if btn_find_note.text() == "Find for teg":
        teg = edit_teg.text()
        list_note.clear()
        for note in notes_dict:
            for t in notes_dict[note]["теги"]:
                if teg == t:
                    list_note.addItem(note)
        edit_teg.clear()
        btn_find_note.setText("Reset search")
    else:
        list_teg.clear()
        list_note.clear()
        edit_text_note.clear()
        list_note.addItems(notes_dict)



notes_dict = read_json("notes.json")
list_note.addItems(notes_dict)

list_note.itemClicked.connect(show_not)
btn_add_note.clicked.connect(add_note)
btn_del_note.clicked.connect(del_note)
btn_save_note.clicked.connect(save_note)
btn_add_teg.clicked.connect(add_teg)
btn_del_teg.clicked.connect(del_teg)
btn_find_note.clicked.connect(find_note)


window.show_win(main_line)
app.exec_()