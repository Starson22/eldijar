# -- coding: utf-8 --
"""
Написать абстрактный класс в котором будет только один атрибут который
и есть введённое нами число  по умолчанию в конструкторе задается значение ноль
"""
from abc import ABC, ABCMeta, abstractmethod, abstractproperty

class Abstract(ABC):
	__metaclass__ = ABCMeta
	@abstractproperty
	def age():
		pass
#______________________________________________________________________________

"""
написать Класс в котором будут описанны все функции с первого домашнего задания
"""
class Functions(Abstract):
	def func1(self,x):
		s=input("Введите строку: ")
		n=int(input("Введите число повторов для Вашей строки: "))
		for i in range(n):
		    print(s)
		    n+=1

	def func2(self,x):
		m=int(input("Введите степень в которую нужно возвести Ваше число: "))
		print(x**m)

	def func3(self,x):
		y=[i for i in range(x+1,x+11)] #генеротор списка
		for t in y:
			print(t)

	def func4(self,x):
		print("Вы ввели неверное число!")

#_____________________________________________________________________________

"""
создаем конечный класс в котором наследуем два предыдущих 
класса в нем же перегружаем конструктор 
"""
class Final(Functions): # Вместе с Functions класс Final наследует и абстрактный класс Abstract

	age=0 # наш @abstractproperty
	def __init__(self,x):
		self.age=x # @abstractproperty будет перезаписан
		if 1 <= self.age <= 3:
			super(Final,self).func1(x)
		elif 4 <= self.age <= 6:
			super(Final,self).func2(x)
		elif 7 <= self.age <= 9:
			super(Final,self).func3(x)
		else:
			super(Final,self).func4(x)


	

d=Final(int(input("Введите число ")))
