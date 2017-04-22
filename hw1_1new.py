# -- coding: utf-8 --
from funpack.funcs_1 import*

x=int(input("Введите число от 1 до 9: "))

if 1 <= x <= 3:
    func1()
	    
elif 4 <= x <= 6:
    func2(x)

elif 7 <= x <= 9:
	func3(x)

else:
	s=func4()
	print(s)