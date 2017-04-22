# -- coding: utf-8 --
'''
Написать функцию в которую можно передать сколько угодно значений 
и оно возводит каждое последующее число в степень 
предыдущего (первое значение возводим в степень один)

'''

def fun(*args):
	tmp = 1 
	result=list() 
	for i in args: 
		result.append(int(i)**tmp) 
		tmp=int(i) 
	print(', '.join(map(str,result)))

x=input("Введите числа разделенные запятой: ").split(",")

fun(*x)