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
    try:
        hierarchy['children'] = [path_structure(os.path.join(path, contents)) for contents in os.listdir(path)]
    except OSError as e:			  #
        if e.errno != errno.ENOTDIR:  # интересная штука exception
            raise					  #
        hierarchy['type'] = 'file'

    return hierarchy

with open("files.json", "w") as d:
	json.dump(path_structure(input("Ведите путь:")), d,ensure_ascii=False, indent=4)# indent делает визульнло приятным
print("Структура папки была сохранена в файле files.json") #теперь работает и с кириллицей