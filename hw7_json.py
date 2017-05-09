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
njlist=jlist[1:] # Убрал заголовок

# pairs=[int(i[1]) for i in jlist if i[2]=="Pair"] #старое
# units=[int(i[1]) for i in jlist if i[2]=="Unit"]
d={}                                               #новое
for i in njlist: 
	if i[2] in d:
		d[i[2]]+=int(i[1])
	else:
		d.update({i[2]:int(i[1])})

# with open("results_for_json.json", "w") as d:
# 	json.dump(["Summ of Pair %d and summ of units %d" %(sum(pairs),sum(units))], d)#старое
with open("results_for_json.json", "w") as f:                                      #новое
		json.dump(d,f)
print("Результаты в этом файле -results_for_json.json ")
