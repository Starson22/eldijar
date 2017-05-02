# -- coding: utf-8 --
"""
Это для Выполнить первое задание считав все значения из csv 
"""
l=[]
with open("datacsv.csv", "r") as file:
	for line in file:
		l.append(line.strip("\n"))

l1=[i.split(',') for i in l[1:]]

pairs=[int(i[1]) for i in l1 if i[2]=="пары"]
units=[int(i[1]) for i in l1 if i[2]=="шт"]

with open("datacsv.csv", "a") as d:
	d.write("\nСумма пар %d и  сумма шт %d" %(sum(pairs),sum(units)))

