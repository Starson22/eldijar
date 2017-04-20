# -- coding: utf-8 --
import os
from datetime import datetime 

addr=input("Введите путь к папкам:")
thefile=input("Введите название папки или файла с расширением:")
fullpath=os.path.join(addr,thefile)
thesize=os.stat(fullpath).st_size
creation=os.stat(fullpath).st_ctime
recentmodif=os.stat(fullpath).st_mtime
if os.path.isdir(fullpath):
	ptype="Папка"
else:
	ptype="Файл"


print("Полный путь: ",fullpath)
print("Тип: ",ptype)
print("Размер: %d байт" %thesize)
print("Дата/время создания: ", datetime.fromtimestamp(creation))
print("Дата/время последнего изменения: ",datetime.fromtimestamp(recentmodif))