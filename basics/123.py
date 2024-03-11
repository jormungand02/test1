# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# def func15(users):
#     result = ''
#     for user in users:
#         if user['work'].startswith('IT'):
#             result += f"{user['name']}, скидки в магазине компьютерной техники!\n"
#     return result

# print(func15(users))


# warehouse = [
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]

# if len(warehouse) > 10:
#     raise ValueError
# for box in warehouse:
#     if len(box) > 3:
#         raise ValueError
    
# inp1 = input('Введите слова и чсла через пробел: ')
# a = inp1.split()
# list_ = []
# for i in a:
#     try:
#         list_.append(int(i))
#     except ValueError:
#         raise ValueError('Данный элемент не является числом!')

# dict_ = {1:'asd', 12:'12'}
# dict_ = {k: len(v) if k % 2 == 0 else len(v) ** 3 for k, v in dict_.items()} 
# print(dict_)


# def  to_fahrenheit(k:int):
#     try:
#         assert k > 0
#         res =  (k - 273.15) * 9 / 5 + 32
#         return res
#     except AssertionError:
#         raise AssertionError("Холоднее абсолютного нуля!")

# print(to_fahrenheit(20))

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# res = [k for k, v in dict_.items()]


# for k, v in dict_.items():
#     if max(v):
#         print(dict_)



# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
#          'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
#          'Nik': {'history': 84, 'math': 85, 'literature': 87}} 
# new_dict = {name: max(scores, key = scores.get) for name, scores in dict_.items()} 
# print(new_dict)



# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k: y for k,v in my_dict.items() for x, y in v.items()} 
# print(dict_)




# list_ = [i for i in range(1, 26) if i % 2 == 0]
# print(list_)




# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [1 if i < 0 else i for i in list_]
# print(int_list)


# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [i for i in list1 if type(i) == str]
# print(list2)



# list_ = [False, True, False, True, False, True, False, True, False, True] 
# list1 = [1 if i == True else 0 for i in list_]
# print(list1)


# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [len(i) for i in list_name]
# print(new_list)



# nums = [i for i in range(1, 1000, 125) if i > 5]
# print(nums)


# list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = [i for i in list1 if i ** 2 > 50]
# print(list2)



# string = "happy birthday!"
# list_ = [i for i in string if i != '!' and i != ' ']
# print(list_)



# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list_ = [j for k, v in dict_.items() for i, j in v.items()]
# print(list_)



# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# list_ = [k.upper() for k, v in dict_.items() if v > 200 and v < 5000]
# print(list_)



# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k.replace('i', ''): k.count('i') for k, v in dict1.items()}
# print(dict2)


# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [i for i in list1 if i]
# print(list2)



# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# readers = [i[1] * 11.95 for i in SPL_Patrons] 
# saved_amount = [round(i, 2) for i in readers]
# print(saved_amount)



# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]
# list_ = [[i[0], i[1] * 42] for i in prairie_pirates if i[2] == True]
# print(list_)



# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }
# list_ = [v['likes'] for k, v in dict_.items() if v['rating'] > 3]
# print(sum(list_))




# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# id_ = [c['id'] for k, v in dict_.items() for c in v ['comments'] if len(dict_[k]['comments']) > 3]
# print(id_)



# set1 = {x for x in range(0, 10)} 
# set2 = {a for a in range(8, 18)} 
# full_set = set1.union(set2) 
# if len(full_set) < 20: 
#     print(f'В этом сете было {20-len(full_set)} повторения, его длина составляет {len(full_set)}') 
# elif len(full_set) == 20: 
#       print("Ваш объединенный сет полностью уникальный!")




# try: 
#     num1 = int(input('Enter: ')) 
#     num2 = int(input('Enter: ')) 
#     res = num1 + num2 
# except ValueError: 
#     print('Введите число!') 
# else: 
#     print(res)


# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     print(dict_['key3'])
# except KeyError:
#     print('Нет такого ключа')
# except:
#     print('hello')



# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')




# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 / num2)
# except Exception:
#     print('Произошла ошибка!')
# except Exception:
#     print('Произошла ошибка!')



# try:
#     cash = int(input())
#     if cash < 0:
#         raise Exception('ValueError')
# except:
#     print('Сумма не может быть отрицательной!')
# else:
#     print(cash)



# list_ = [1, 2, 3]
# try:
#     print(list_.get('age'))
# except Exception:
#     ...
# print(list_.get('age'))



# string = 'hello'
# num = 250
# try:
#     print(string + num)
#     raise 'Unsupported option'
# except TypeError:
#     print('Unsupported option')


# try:
#     for i in range(0, 10):
#         list_.append(i)
# except NameError:
#     print('name')

# try:
#     list_ = [1, 2, 3, 4]
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     print('hello')




# try:
#     password = '2003010202'
#     if len(password) < 6:
#         raise ValueError
# except TypeError:
#     print('hello')



# warehouse = [
# ['1', '2', '3', '3'],
# [1, 2],
# [[1], [2], [3]],
# [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]
# for i in warehouse:
#     if len(warehouse) > 10 or len(i) > 3:
#         raise ValueError()




# def to_fahrenheit(k:int) -> float: 
#     assert k >= 0,'Холоднее абсолютного нуля!' 
#     res=(k - 273.16) * 9 / 5 + 32 
#     return res 
# print(to_fahrenheit(34))


# try:
#     import lamabimgo
# except ModuleNotFoundError:
#     print('Такого модуля нет')



# def filter_comment(comment: str, banlist=['bastard']) -> None: 
#     comment_words = comment.lower().replace('.', '').replace('!', '').replace('?', '').replace(',', '').split() 
#     for word in comment_words: 
#         if word in banlist: 
#             raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
# print(filter_comment('bastard'))



# try:
#     num = 100000000
#     for i in range(0, num):
#         print('Nope')
# except KeyboardInterrupt:
#     print('Nope')




# def collect_all_possibles(list_: list, num: int) -> list:
#     try:
#         res = []
#         res.append(list_ + num)
#         res.append(list_ * num)
#         res.append(list_ - num)
#         res.append(list_ // num)
#         res.append(list_ ** num)
#         print(res)
#     except TypeError:
#         print(res)
# print(collect_all_possibles([1,2,3], 2))

   


# def read_last(lines: int, filename: str):
#     with open(filename, 'r') as file:
#         data = file.readlines() 
#     data.reverse()
#     if lines >= len(data):
#         for line in data:
#             print(line.replace('\n', ''))
#     else:
#         count = 1
#         for line in data:
#             print(line.replace('\n', ''))
#             if lines == count:
#                 break
#             count += 1

# read_last(3, 'test1.txt')




# def longest_words(filename: str):
#     with open(filename) as file:
#         data = file.read()
#     data2 = data.split()
#     list_ = []
#     max_word = max(data2, key = len)
#     for word in data2:
#         if len(max_word) == len(word):
#             list_.append(word)

#     if len(list_) == 1:
#         print(list_[0])
#     else:
#         print(list_)



# with open('test1.txt', 'r') as f:
#     data = f.readlines()
#     count = 1
#     for line in data:
#         if count == 5:
#             break
#     print(line.replace('\n', ''))
#     count += 1







# try: 
#     inp1 = input('enter1: ') 
#     inp2 = input('enter2: ') 
#     print(int(inp1) + int(inp2)) 
# except:
#     print(inp1 + inp2)




# inp1 = input() 
# res = inp1.split(' ') 
# try:
#     list_ = [int(x) for x in res] 
# except ValueError: 
#     raise ValueError('Данный элемент не является числом!')








# def collect_all_possibles(list_: list, num: int) -> list:
#     res = []
#     for i in list_:
#         try:
#             if i ==str: 
#                 res.append(i)
#             if i ==list:
#                 for n in i:
#                     i.append(n)
#                     res.append(n)
#             if i == int:
#                 res.append(i*num)
#                 res.append(i+num)
#                 res.append(i-num)
#                 res.append(i//num)
#                 res.append(i**num)
#         except:
#             continue
#     return (res)   
        
# print((collect_all_possibles([
#     'hello',
#     6, 
#     [1,2,3]
# ], 2)))

         
# def get_type(a, b):
#     print(f'{type(a)}\n{type(b)}')
    
# print(get_type('hello', 6))


# def get_type(x,y): 
#     print(f'{type(x)}\n{type(y)}') 
# get_type(5,'s')



# num = 6 
# def check(num): 
#     if num % 2 == 0: 
#         return("It is even number") 
#     else: 
#         return("It is odd number")

# print(check(num))




# def is_palindrome(str_: str):
#     if ''.join(reversed(str_.lower())) == str_.lower():
#         return True
#     else:
#         return False

# print(is_palindrome('Hah'))




# def multiply_list(list_: list):
#     res = 1
#     for i in list_:
#         res *= i
#     return res
# print(multiply_list([1, 2, 3, 4, 5, 6]))




# def sum_digits(num1):
#     sum_ = 0
#     for i in str(num1):
#         sum_ += int(i)
#     return sum_
# print(sum_digits(105))




# def func11(a, b, c):
#     try:
#         res = a / c
#         res1 = b / c
#         return res + res1
#     except ZeroDivisionError:
#         return a + b
# print(func11(10, 8, 2))




# def func12(list_: list, str_):
#     if str_ == 'lower':
#         return list(map(str.lower(), list_))
#     else:
#         return list(map(str.lower(), list_))
    
# func12(['hello', 'world'], 'lower')


# def func12(list_, str_):
#     res = []
#     for i in list_:
#         if str_ == 'lower':
#             res.append(i.lower())
#         elif str_ == 'upper':
#             res.append(i.upper())
#     return res
# func12(['heLLo', 'woRld'], 'lower')



# def func13(s):
#     return {i: s.count(i) for i in set(s)}
# print(func13('hello'))



# def func13(s):
#     dict_ = {}
#     for i in str(s):
#         dict_[i] = s.count(i)
#     return dict_
    
# print(func13('hello'))

# def calc(a, b, oper):
#     if oper == '+':
#         return a + b
#     elif oper == '-':
#         return a - b
#     elif oper == '/':
#         return a / b
#     elif oper == '*':
#         return a * b
# print(calc(10, 5, oper = '+'))


# def add_(a, b): 
#     return a + b 
# def sub_(a, b): 
#     return a - b 
# def mult_(a, b): 
#     return a * b 
# def div_(a, b): 
#     return a / b 

# def calc(x, y, oper): 
#     if oper == "+": 
#         return add_(x, y) 
#     elif oper == "-": 
#         return sub_(x, y) 
#     elif oper == "*": 
#         return mult_(x, y) 
#     elif oper == "/": 
#         return div_(x, y)
# print(calc(40, 20, oper = "+"))


# def func16(a, b):
#     return (f'На 100км было расходовано {round(100 * b / a)}л горючего')

# print(func16(53, 8))



# def func16(km, v): 
#     return(f'На 100км было расходовано {round(100 * v / km)}л горючего') 

# print(func16(53, 8))






# dict_1 = [{'name': 'Jack', 'salary': 10000, 'overTime': 4}, 
#              {'name': 'Tom', 'salary': 15000, 'overTime': 3}]
# for i in dict_1:
#     if 'overTime' in i:
#         i['salary'] += i['overTime'] * 200
# print(dict_1)


# def func18(list_: list):
#     int_ = []
#     str_ = []
#     for i in list_:
#         if type(i) == int:
#             int_.append(i)
#         else:
#             str_.append(i)
#     return [int_, str_]

# print(func18([25, 'hello', 87, 'bootcamp', 13, 27, 'makers', 'war']))






# def func18(list_):
#     int_ = [i for i in list_ if type(i) == str]
#     str_ = [y for y in list_ if type(y) == int]
#     return int_, str_
# print(func18([25, 'hello', 87, 'bootcamp', 13, 27, 'makers', 'war']))



# work = [ {'name': 'Jack', 'salary': 10000, 'overTime': 4}, 
#              {'name': 'Tom', 'salary': 15000, 'overTime': 3}, 
#              {'name': 'Jessica', 'salary': 20000, 'overTime': 9}, 
#              {'name': 'Helen', 'salary': 25000, 'overTime': 2}, 
#              {'name': 'Peter', 'salary': 30000, 'overTime': 7} ] 
# def func17(dict_): 
#     for x in dict_: 
#         if 'overTime' in x: 
#             x['salary'] += x['overTime'] * 200 
#             x.pop('overTime')
#     return dict_ 

# print(func17(work))



# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]
# def func19(list_):
#     list_.sort(key = lambda i: i['marks'], reverse = True)
#     return list_
# print(func19(students))




# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]

# def func20(list_:list, str_:str): 
#     result=list() 
#     for i in list_: 
#         if str_.lower() in i['title'].lower(): 
#             result.append(i) 
#     return result

# print(func20(products, 'I'))






# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ] 
# def func21(list_:list, str_:str):
#     res = []
#     for i in list_:
#         if str_ in i['category']:
#             res.append(i)
#     return res
# print(func21(products, 'samsung'))




# balance = 10000 
# def spent(target, sum_, bal): 
#     if bal - sum_ >= 0: 
#         bal -= sum_ 
#         return ({'target':target, 'spend':sum_}, bal) 
#     else: 
#         return 'Недостаточно средств' 
# print(spent('iphone15_pro_max', 1500, balance)) 


# def deposit(a, b):
#     b += a 
#     return b
# print(deposit(20000, balance))



# database = list() 

# def create(db:list,title:str,price:int,category:str): 
#     db.append({'title':title, 'price':price, 'category':category}) 
#     return db 


# def read(db:list): 
#     print(db) 
#     return db

# def update(db:list,index:int,title:str,price:int,category:str): 
#     db[index]['title'] = title 
#     db[index]['price'] = price 
#     db[index]['category'] = category 
#     return db 

# def delete(db,index): 
#     db.pop(index) 
#     return db




# def foo():
#     global var
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
  
#     def bar():
#         global var
#         var = 'переменная bar'
        
 
#     bar()
# foo()
# print('переменная в foo: ', var)



# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     print(x)

#     def bar():
#         global x
#         x = 'Я могу изменяться'
        
#     bar()
# my_func()
# print(x)



# num = 3
# def mul():
#     global num
#     num = num ** 2

# mul()
# mul()
# mul()
# print(num)



# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount
    
# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')


# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()


# result = 0
# def pow_first(x, y):
#     global result
#     result = x ** y

# def pow_second(z):
#     global result
#     result %= z
        
# pow_first(2, 3)
# pow_second(3)
# print(result)


# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age_control(dict_):
#     global a
#     for k, v in a.items():
#         if v >= 17:
#             print(f'{k}, Вы можете войти в клуб')
#         else:
#             print(f'{k}, извините, Вы не проходите по age-control')
#     return dict_

# age_control(a)



# a = ['pipi', 'papa', 'mama'] 
# b = [] 
# for i in a: 
#     b.append(i.capitalize()) 
# print(b)
    



# def count_symbols(str_): 
#     glasnye = 0 
#     soglasnye = 0 
#     drugie = 0 
#     for i in str_: 
#         if i.lower() in 'аяуюоеёэиы': 
#             glasnye += 1 
#         elif i.lower() in 'бвгджзйклмнпрстфхцчшщ':
#             soglasnye += 1 
#         else: 
#             drugie += 1 
#     return (f'Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов: {drugie}') 

# print(count_symbols('Марлен'))


# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def lower_7():
#     b = []
#     global a
#     for i in a:
#         if i < 7:
#             b.append(i)
#     return b

# print(lower_7())



# list_ = [1, 2, 3, 4]
# from functools import reduce
# new_list = reduce(lambda x, y: x + y, list_)
# print(new_list)



# list_ = [1, 5, -9, 6, -4]
# result = all(3 < i for i in list_)
# print(result)



# list_ = [1, 2, 3, 4]
# result = list(filter(lambda x: x % 2 == 0, list_))
# print(result)


# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)

# from functools import reduce
# list_ = [5, 6, 7, 8]
# result = reduce(lambda x, y: x * y, list_)
# print(result)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# list2 = list(filter(lambda x: x % 2 == 0, list_))
# list3 = list(filter(lambda x: x % 2 != 0, list_))
# result = f'even: {len(list2)}, odd: {len(list3)}'
# print(result)


# list_ = [-1, 2, 3, 5, -3, 7]
# list2 = list(map(lambda x: x > 0, list_))
# result = list2
# print(result)


# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x:True if x > 0 else False,list_)) 
# print(result)



# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John']
# result = reduce(lambda x, y: x if len(x) > len(y) else y, list_) 
# print(result)




# result = list(map(lambda x: "Fizz" if x % 3 == 0 else "Buzz", range(1,50))) 
# print(result)



# from functools import reduce
# list_ = [1, 2, 3, 4, 5, 6, 7]
# result = reduce(lambda x, y: x if x > y else y, list_) 
# print(result)



# string = 'hello world'
# res = enumerate(string)
# print(tuple(res))


# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# res = [abs(i) for i in list_]
# print(res)


# list_ = ['hello', 123]
# res = [type(i) for i in list_]
# print(res)




# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# result = map(lambda x: f'{x} Python' if len(x) >= 5 else f'{x} JavaScript', names)
# print(list(result))



# list_ = ['123hello@gmail.com', '123', 'hello']
# res = map(lambda x: x if '@gmail.com' in x else 'Not valid email', list_)
# print(list(res))



# list1 = ['M', 'A', 'K', 'E', 'R', 'S'] 
# list2 = [236, 54, 33, 21, 89, 1]
# res = zip(list1, list2)
# print(list(res))



# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# list2 = list(filter(lambda x: x > 0, list_))
# list3 = list(filter(lambda x: x <= 0, list_))
# result = zip(list2, list3)
# print(list(result))



# import requests
# from bs4 import BeautifulSoup as BS
# response = requests.get('https://www.wikipedia.org/')
# html = response.text
# soup = BS(html, 'lxml')
# block = soup.find('div', class_="central-featured-lang lang5")
# title = block.find('strong').text
# count = block.find('small').text
# print(title)
# print(count)



# import requests
# from bs4 import BeautifulSoup as BS

# html = requests.get('http://www.example.com/').text
# soup = BS(html, 'lxml')
# title = soup.find('h1').text
# description = soup.find('p').text
# link = soup.find('a').get('href')

# print(f'h1: {title}')
# print(f'p: {description}')
# print(f'a: {link}')



# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]
# res = map(lambda x: round(x ** 2, 3), list_ )
# print(list(res))




# list_ = ['a', 'n', 'n', 'a']
# res = filter(lambda x: 'YES' if list_[::-1] == list_ else 'NO', list_)
# print(list(res))


# list_ = ['a', 'n', 'n', 'a'] 
# result = list(map(lambda x: 'YES' if list_[::-1] == list_ else 'NO',list_)) 
# print(result[3]) 



# def filter_text(text_filename: str) -> str:
#     with open(text_filename, 'r') as f:
#         text = f.read()

#     with open('forbidden_words.txt', 'r') as file_:
#         forbidden_words = file_.read().split()

#     modified_text = text

#     for word in forbidden_words:
#         modified_text = modified_text.lower(). replace(word, '*' * len(word))

#     result = ''

#     for index in range(len(text)):
#         if modified_text[index] != '*':
#             result += text[index]
#         else:
#             result += '*'
#     return result



# import requests
# from bs4 import BeautifulSoup as BS

# def find_category(categories: list, keyword: str):
#     result = []
#     for category in categories:
#         if keyword.lower() in category.lower():
#             result.append(category)
#     return result

# category_list = []

# URL = 'https://enter.kg/'
# response = requests.get(URL)
# soup = BS(response.text, 'html.parser')

# categories_li = soup.find_all('li', {'class': 'VmClose'})
# for category_li in categories_li:
#     title = category_li.find('a').text
#     category_list.append(title)

# categories_span = soup.find_all("span", {"class": "category-product-count"})
# for category_span in categories_span:
#     title = category_span.text.strip()
#     category_list.append(title)

# print(find_category(category_list, 'Ноутбуки'))





# def read_last(lines, filename): 
#     with open(filename) as file: 
#         list_ = file.readlines() 
#         list_.reverse() 
#         if len(list_) > lines: 
#             i = 0 
#             while i < lines: 
#                 print(list_[i].replace('\n', '')) 
#                 i += 1 
#         else: 
#             for i in list_: 
#                 print(i.replace('\n', '')) 
                
# read_last(25, 'article.txt')




# class BankAccount:
#     balance = 0
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом') 

#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом') 

# account = BankAccount()
# account.deposit(1000) 
# account.withdraw(500) 




# class Password:
#     def __init__(self, password):
#         self.passw = password

#     def validate(self):
#         # Проверка длины пароля
#         if len(self.passw) not in range(8, 15):
#             raise ValueError('Password should be longer than 8, and less than 15')

#         # Проверка наличия хотя бы одной цифры в пароле
#         if not any(c.isdigit() for c in self.passw):
#             raise ValueError('Password should contain numbers too')

#         # Проверка наличия хотя бы одной буквы в пароле
#         if not any(c.isalpha() for c in self.passw):
#             raise ValueError('Password should contain letters as well')

#         # Проверка наличия хотя бы одного из специальных символов в пароле
#         if not any(i in ['@', '#', '&', '$', '%', '!', '~', '*'] for i in self.passw):
#             raise ValueError('Your password should have some symbols')

#         return 'Ваш пароль сохранен.'

#     def __str__(self):
#         # Возвращаем строку из звездочек той же длины, что и пароль
#         return '*' * len(self.passw)

# # Пример использования
# obj = Password('ads1@12')
# print(obj.validate())






# def longest_words(filename: str):
#     with open(filename, 'r') as file:
#         content = file.read()

#     words = [word.strip(".,?!\"'()[]{}") for word in content.split()]

#     if words:
#         max_length = max(len(word) for word in words)

#         longest_words_list = [word for word in words if len(word) == max_length]

#         if len(longest_words_list) == 1:
#             print("Слово с максимальной длиной:", longest_words_list[0])
#         else:
#             print("Список слов с максимальной длиной:", longest_words_list)
#     else:
#         print("Файл пустой или не содержит слов.")

# longest_words('article.txt')



# from datetime import datetime
# class SmartPhones:
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self):
#         return (f'{self.name} {self.memory}')
    
#     def charge(self, power):
#         self.battery += power

# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios):
#         self.ios = ios
#         super().__init__(name, color, memory)
    
#     def send_imessage(self, str_):
#         return f'sending {str_} from {self}'

# class Samsung(SmartPhones):
#     def __init__(self, android, name, color, memory):
#         self.android = android
#         super().__init__(name, color, memory)
    
#     def show_time(self):
#         return datetime.now().time()

# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone)
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) 





# class Game:
#     __level = 0
#     def __init__(self, name):
#         self.name = name

#     def play(self, hours):
#         if hours > 2:
#             self.__level += 1
    
#     def get_level(self):
#         return self.__level

# game = Game('War Robots')
# print(game.get_level())
# game.play(10)
# game.play(5)
# print(game.get_level())
