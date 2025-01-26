import math     # подключаем библиотеку, from math import * что бы не вводить math.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
SrArifmet = (a + b + c) / 3
print (f'Среднее арифметическое равно: {SrArifmet}')
SrGeometr = math.pow((a * b * c), 1/3)
print (f'Среднее геометрическое равно: {SrGeometr}')
