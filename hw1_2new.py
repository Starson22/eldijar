# -- coding: utf-8 --
from funpack.funcs_2 import*

print("Общество в начале XXI века")
x=int(input("Введите введите Ваш возраст: "))

if 0 <= x <= 6:
    func1()
	    
elif 7 <= x <=17:
    func2()

elif 18 <= x <= 24:
    func3()

elif 25 <= x <= 59:
    func4()

elif 60 <= x <= 119:
    func5()

else:
	func6()