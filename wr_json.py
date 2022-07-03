import os 
import json

def path(name_file):
    p = os.path.abspath(__file__+"/..")
    p = os.path.join(p,name_file)
    return p

def write_json(name_file, name_dict):
    name_file = path(name_file)
    with open(name_file,'w',encoding="utf-8") as file:
        json.dump( name_dict,file, indent=4)

def read_json(name_file):
    name_file = path(name_file)
    with open(name_file,'r',encoding="utf-8") as file:
        name_dict = json.load(file)
    return name_dict


# notes_dict = {
#                 "Про планети" : 
#                         {
#                                 "текст" : "Що якщо вода на Марсі це ознака життя?",
#                                 "теги" : ["Марс", "гіпотези"]
#                             },
#                 "Про чорні діри" : 
#                         {
#                                 "текст" : "Сингулярність на горизонті подій відсутня",
#                                 "теги" : ["чорні діри", "факти"]
#                             }
# }
# write_json("notes.json",notes_dict)