# -- coding: utf-8 --
def func1():
	s=input("Введите строку: ")
	n=int(input("Введите число повторов для Вашей строки: "))
	for i in range(n):
	    print(s)
	    n+=1

def func2(x):
	m=int(input("Введите степень в которую нужно возвести Ваше число: "))
	print(x**m)

def func3(x):
	y=[i for i in range(x+1,x+11)] #генеротор списка
	for t in y:
		print(t)

def func4():
	return "Вы ввели неверное число!"