# -- coding: utf-8 --
import re
import string
import random

#для того что ниже....первый range для кол символов в слове и второй range для кол слов в предложении
randomsent=' '.join(''.join(random.choice(string.ascii_lowercase) for i in range(3)) for i in range(6))

print("Наш случайный текст:",'\n',randomsent)

chars=input("Введите символы: ")
reverchar=chars[::-1]
print("Ваши ревертированные символы: ",reverchar)
substr=re.sub(r"^%s|%s$" %(chars,chars),"%s" %reverchar,"%s" %randomsent)
if randomsent!=substr:
    print("Наш текст с вашими ревертированными символами, в начале или в конце","\n",substr)
else:
	print("В нашем тексте мы не нашли ваше слово/символы, в начале или в конце")