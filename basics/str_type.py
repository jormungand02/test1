'===========String=========='
#строки - это неименямый тип данных, который пердназначен для хранения текста, заключонного в одинарные либо двойные кавычки

string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# string3 = 'не правильная строка"
string4 = "Don't" # внутри двойной кавычки все одинарные - просто символы
string5 = """Многострочный текст в одинарных кавычках, тут можно ставить 'любые' кавычки
"""

string6 = 'hello '+ ' ' + 'world'
print(string6)

string7 = 'hello world|' * 8
print(string7)

'===============Экранизация строк================='
'/n' # переносит текст на новую строку 
print('hello\nworld')
#hello
#world

'\t' # табуляция
print('hello\tworld')

str1 = 'don\'t' # отображает кавычку '
print(str1)

str2 = "don\"t"
print(str2)

str3 = 'Символ - \\'
print(str3)

'\v' # перенос на новую строку со смещением впрвао на длину предыдущей строки
print('hello\vworld\vmakers\vbootcamp')
'\r' # перенос каретки на начало строки и замена начала строки
print('Makers bootcamp\rHi')
# Hikers bootcamp

'=============Форматирование строк=============='
#1
title = 'iPhone 14'
price = 150
format_1 = 'Мой телефон ', title, 'стоит', price, 'долларов'
format_2 = f'Мой телефон {title} стоит {price}$'

print(format_2)

#2
string = 'Название: {} Цена: {}$'
print(string.format('iPhone', 150))

#3
string = 'Название: %s Цена: %s'
print(string % ('iphone', 150))

'==========Методы строк==========='
# методы - функции которые относятся к определенному классу, к ним можно обращаться через точку

print(dir(str))

string = 'makers'

print(string.upper()) # makers -> MAKERS
print(string.lower()) # MAKERS -> makers
print(string.swapcase()) # MAKers -> makERS

print(string.title()) # helLo wOrld -> Hello World
print(string.capitalize()) # hello world -> Hello world
print(string.center(11, '-')) # '---hello---'
print(string.count('')) # hello -> 2 пробел и пустота  тоже ищет 
print(string.strip()) # убирает пробелы


print(string.startswith('a')) #False
print(string.startswith('h')) #True
print(string.startswith('H')) #False проверяет, начинается ли строка на указанную подстроку
print(string.endswith('d')) #False
print(string.endswith('llo')) #True


print(string.islower()) # makers -> True
print(string.isupper()) # MAKERS -> True

string = '124sfd4'
print(string.isdigit()) # True - проверяет весь ли текст состоит из чисел
print(string.isalpha()) # False - проверка на буквы в тексте
print(string.isalnum()) # True - проверка на то что является ли строка с числами или с буквами или все вместе, но не символы
string2 = 'hello.world.makers.bootcamp'
print(string2.split('.')) # Делит предложения 


'=============Индексы==========='
# индекс это порядковый номер элемента последовательности (символа в строке), (инедксация начинается с 0)

'h e l l o  w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#               -3 -2 -1
string = ' hello world'
print(string[0]) # 'h' 
print(string[7]) # 'o'
print(string[10]) # 'd'
print(string[-1]) # 'd'

#срезы - подстрока (часть строки)
#string[start:end(не включительно):step]
string = 'hello world'
print(string[3:5]) # l'lo wo'
print(string[:]) # 'hello world'
print(string[6:]) # 'world'
print(string[:5]) # 'hello'
print(string[::-1]) # 'dlrow olleh'
print(string[::2]) # 'hlowrd'
print(string[::3]) # 'hlwl'
print(string[::4]) # 'hor'

string = 'hello'
string = string.upper() # hello -> HELLO
print(string)





