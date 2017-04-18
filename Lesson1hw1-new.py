# -- coding: utf-8 --
# для Переписать первое задание использую генераторы списков, в конце
from funpack import func1

x=int(input("Введите число от 1 до 9: "))

if func1.compar(x)==1:
	s=input("Введите строку: ")
	n=int(input("Введите число повторов для Вашей строки: "))
	for i in range(n):
	    print(s)
	    n+=1
	    
elif func1.compar(x)==2:
    m=int(input("Введите степень в которую нужно возвести Ваше число: "))
    print(x**m)

elif func1.compar(x)==3:
	#for y in range(1,11): #по сути от 1 до 10, 11 не включается
	#	print(x+y)
	y=[i for i in range(x,x+10)] #генеротор списка
	for t in y:
		print(t)
else:
	print("Вы ввели неверное число!")