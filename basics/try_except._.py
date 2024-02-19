'==============Exceptions============'
# исключения - объекты, которые прерывают работу кода, если не были обработаны 

'SyntaxError' 
'a ='
# исключение, которое выходит, когда в коде допущена синтаксическая ошибка
'--------------------------------------------------------------------------------'
'NameError'
'print(adasd)'
# исключение, которое выходит когда мы обращаемся к несуществующей переменной
'---------------------------------------------------------------------------'
'IndexError'
'''
list_ = [1,2,3,4]
list_[100000]
'''
# исключение, которое выходит при обращении к несуществующему индексу
'--------------------------------------------------------------------'
'KeyError'
'''
dict_ = {'a':1, 'b':2}
print(dict_['c'])
'''
# исключение, которое выходит при обращении к несуществующему ключу 
'------------------------------------------------------------------'
'ValueError'
# когда мы передаем в функцию не корректный для нее тип данных
'''
int('10d')
'''
# когда мы распаковываем итерируемый объект на несколько переменных и кол-во переменных не совпадает с кол-во значений 
'''
a, b, c = [1, 2]
'''
'-----------------------------------------------------------------'
'TypeError'
# когда мы пытаемся использовать методы не свойственные какому то типу данных
# когда мы пытаемся передать в функцию больше или меньше аргументов, чем принимает функция 

'''
for i in 1:
'''
'''
5 + '5'
'''
'''
{[1,2,3]:'a'}
'''

'------------------------------------------------------------'
'ZiroDivisionError'
# выходит когда делим что-то на 0
'''
45 / 0 | 100 // 0 | 3 % 0
'''

'--------------------------------------------------------'
'AttributError'
# выходит когда мы обращаемся к несуществующему аттрибуту или методу (тип данных)
'''
[1,2,3].replace(1, 5)
'''
'--------------------------------------------------------------------------'
'IndentationError'
# выходит когда мы неправильно используем отступы
'''
    a = 5
'''
'''
for i in range(10):
print(i)
'''
Exception
# исключение, которое создали, чтобы его вызывать
'===============Вызов исключений================='
# raise ZeroDivisionError('Я вызвал name_error')

'==============Try except============='
# конструкция, которая помогает обрабатывать исключения 

try: # конструкцию try используют если разработчик не уверен или знает что в коде есть ошибка и хочет обработать ее в except
    num = int(input('Введите число'))
except ValueError: # конструкция except нужна для обработки исключения, в данном случае исключение VallueError
    print('Введите число, а не символы')
else: # срабатывает когда не вышло ошибки, исключения (когда не сработал except)
    print(f'Вы ввели число {num}')
finally: # работает всегда
    print('До свидания')

number = 25
try:
    print(number)
except (ValueError, NameError, TypeError):
    print('Нет такой переменной, Проверил вот такие исключения: NameError, VallueError, TypeError ')


try:
    raise Exception
except: # отлавливаются все ошибки
    print('Отловлена любая ошибка')


try:
    raise ValueError
except Exception: # отлавливаются вссе ошибки
    print('Отловлена любая ошибка')


try:
    print(1)
finally:
    print(2)

