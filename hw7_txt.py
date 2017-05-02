# -- coding: utf-8 --
"""
Для Дан файл с прайс листом одежды. Помимо названия товара указывается
 количество штук и количество пар. В одной строке указывается только 
 один товар. Посчитать количество товаров которые считаются штуками и 
 количество товаров считаемых парами.  Результаты дописать в конец файла
"""
l=[]
with open("data.txt", "r") as file:
	for line in file:
		l.append(line.strip("\n"))

l1=[i.split() for i in l[1:]]
pairs=[int(i[1]) for i in l1 if i[2]=="пары"]
units=[int(i[1]) for i in l1 if i[2]=="шт"]

with open("data.txt", "a") as d:
	d.write("\nСумма пар %d и  сумма шт %d" %(sum(pairs),sum(units)))

