# -- coding: utf-8 --
"""
Для HW2
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
написать Класс в котором будут описанны все функции со второго домашнего задания
"""

class Functions(Abstract):
	def func1(self,x):
		print("Вам в детский сад")
	def func2(self,x):
		print("Вам в школу")
	def func3(self,x):
		print("Вам в профессиональное учебное заведение")
	def func4(self,x):
		print("Вам на работу")
	def func5(self,x):
		print("Вам предоставляется выбор")
	def func6(self,x):
		print("Ошибка! Это программа для людей!"*5)

#__________________________________________________________________________

"""
создаем конечный класс в котором наследуем два предыдущих 
класса в нем же перегружаем конструктор 
"""

class Final(Functions):
	age=0 # наш @abstractproperty
	def __init__(self,x):
		self.age=x # @abstractproperty будет перезаписан
		if 0 <= self.age <= 6:
			super(Final,self).func1(x)
		elif 7 <= self.age <= 17:
			super(Final,self).func2(x)
		elif 18 <= self.age <= 24:
			super(Final,self).func3(x)
		elif 25 <= self.age <= 59:
			super(Final,self).func4(x)
		elif 60 <= self.age <= 119:
			super(Final,self).func5(x)
		else:
			super(Final,self).func6(x)
		
p=Final(int(input("Введите число ")))