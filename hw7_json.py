# -- coding: utf-8 --
"""
Это для Выполнить первое задание считывая значения из 
json файла результат выдать в другом json файле
"""
import json
with open("dataj.json", "r") as file:
	l=file.read()
	l1=json.loads(l)


jlist=[]

for i in l1:
	jlist.append(list(i.values()))

pairs=[int(i[1]) for i in jlist if i[2]=="Pair"]
units=[int(i[1]) for i in jlist if i[2]=="Unit"]

with open("results_for_json.json", "w") as d:
	json.dump(["Summ of Pair %d and summ of units %d" %(sum(pairs),sum(units))], d)


print("Результаты в этом файле -results_for_json.json ")
