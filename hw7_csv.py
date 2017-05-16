# -- coding: utf-8 --
"""
Это для Выполнить первое задание считав все значения из csv 
"""
l=[]
with open("datacsv.csv", "r") as file:
	for line in file:
		l.append(line.strip("\n"))
# l это лист, где каждый элемент это стока файла, стока в виде str
l1=[i.split(',') for i in l[1:]]
# l1 это лист, где каждый элемент это еще один лист, в каждом элементе данные разделены ','
# pairs=[int(i[1]) for i in l1 if i[2]=="пары"]
# units=[int(i[1]) for i in l1 if i[2]=="шт"]   #старое
d={}                                            #новое
for i in l1: 
	if i[2] in d: # i[2] это "пара" или "шт", если он есть в словаре d,
		d[i[2]]+=int(i[1]) #тогда к ее значению + i[1]--это количество тов.
	else:
		d.update({i[2]:int(i[1])})# а если нет то мы заводим новый ключ в слваре
# with open("datacsv.csv", "a") as d:                                 #старое
# 	d.write("\nСумма пар %d и  сумма шт %d" %(sum(pairs),sum(units)))
with open("datacsv.csv", "a") as f:                                   #новое
	for key, val in d.items():
		f.write("Сумма '%s' равна %d\n" %(key,val))

