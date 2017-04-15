x=int(input("Введите число от 1 до 9: "))

if 1 <= x <= 3:
	s=input("Введите строку: ")
	n=int(input("Введите число повторов для Вашей строки: "))
	#print(s*n)
	for i in range(n):
	    print(s)
	    n+=1
	    
elif 4 <= x <= 6:
    m=int(input("Введите степень в которую нужно возвести Ваше число: "))
    print(x**m)

elif 7 <= x <= 9:
	for y in range(1,11): #по сути от 1 до 10, 11 не включается
		print(x+y)

#elif x not in range(1,10):
#    print("Вы ввели неверное число!")
else:print("Вы ввели неверное число!")