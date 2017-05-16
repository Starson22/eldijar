# -- coding: utf-8 --
"""
Это для Сохранить в json структуру любой папки у Вас на компьютере
"""
import os
import errno
import json

def path_structure(path):
    hierarchy = {
        'type': 'folder',
        'name': os.path.basename(path),
        'path': path,
    }
# try попытается выполнить код ниже, для каждого файла/папки он вызовит себя если ошибка перейдет на Except, снизу 
# а там если № ошибки не равен номеру ошибки ENOTDIR-(не папка), любая ошибка которая не ENOTDIR то мы перевызываем ошибку через raise
# потом если ошибка =ENOTDIR то значение Type в hierarchy будет file
    try: 
        hierarchy['children'] = [path_structure(os.path.join(path, contents)) for contents in os.listdir(path)]
    except OSError as e:			  #
        if e.errno != errno.ENOTDIR:  # интересная штука exception
            raise					  #
        hierarchy['type'] = 'file'

    return hierarchy

with open("filesfolders.json", "w") as d:
	json.dump(path_structure(input("Ведите путь:")), d,ensure_ascii=False, indent=4)# indent делает визульнло приятным
print("Структура папки была сохранена в файле filesfolders.json") #теперь работает и с кириллицей