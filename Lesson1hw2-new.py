# -- coding: utf-8 --
from funpack import func2

print("Общество в начале XXI века")
x=int(input("Введите введите Ваш возраст: "))

if func2.compar2(x)==1:
    print("Вам в детский сад")
	    
elif func2.compar2(x)==2:
    print("Вам в школу")

elif func2.compar2(x)==3:
    print("Вам в профессиональное учебное заведение")

elif func2.compar2(x)==4:
    print("Вам на работу")

elif func2.compar2(x)==5:
    print("Вам предоставляется выбор")

else:
	print("Ошибка! Это программа для людей!"*5)