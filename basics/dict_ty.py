'====================Словари====================='
# dict - изменяемый, итерируемый, неупорядоченный, неиндексируемый тип данных, для хранения данных парах(ключ:значение)
user = {'name':'sultan', 'age':20, 'nick': 'katana'}
print(user['age']) # 20
print(user['nick']) # katana
print(user['name']) # sultan

# {ключ:значение, ключ:значение...}
# ключ - не изменяемый тип данных, уникальный(если ключ повторяется то сохранится тот, который является последним)
# значение - любые: и изменяемый, и неизменяемый тип данных. Могут повторятся

'==============Создание================'
dict1 = {'a':1, 'b':2}
dict2 = dict([('a',1),('b',2)])
dict3 = dict(['a1','b2'])
dict4 = {}
dict4['name'] = 'tima'
dict4['age'] = 100
dict4['nick'] = 'collection'
print(dict4)

'====================Методы словарей====================='
# get - метод, который возвращает значение по ключу, если такого ключа нет то возвращает дефолтное значение, чаще всего None
user = {
    'name':'Nick',
    'age': 100,
    'telephon_number':'1234567'
}
#print(user['asfasda']) # KeyError
print(user.get('age')) # 100
print(user.get('name')) # Nick
print(user.get('id')) # None

# pop - удаляет пару по ключу и возвращает значение 
dict_2 = {'a':1, 'b':2, 'c':3}
popped_values = dict_2.pop('a')
print(popped_values) # 1
print(dict_2) # {'b': 2, 'c': 3}

#popitem - удаляет последнюю пару и возвращает ее

dict_ = {'a':1, 'b':2, 'c':3}
popped_values1 = dict_.popitem()
print(popped_values1) # ('c', 3)

# print(dir(dict()))

# update - расширяет словарь парами из второго словаря 

dict5 = {1:'a', 2:'b'}
dict6 = {2:'c', 4:'d'}
dict5.update(dict6)
print(dict5) # {1:'a', 2:'c', 4:'d'}

#clear - очищает словарь 
dict_1 = {1:1, 2:2, 3:3}
dict_1.clear()
print(dict_1) # {}

# fromkeys - метод для создания нового словаря, используя список ключей

dict_3 = dict.fromkeys([1,2,3])
print(dict_3) # {1: None, 2: None, 3: None}

dict_4 = dict.fromkeys('abcd', 0)
print(dict_4) # {'a':0, 'b':0, 'c':0, 'd':0}


list.copy()
list.deepcopy()
dict.setdefault()

# items - это метод, который достает ([ключ, значение), (ключ, значение]...)
# keys - метод, который возвращает ключи 
# values - метод, который возвращает значения 

dict_ = {'a':1, 'b':2, 'c':3}
print(dict_.values())
print(dict_.keys())
print(dict_.items())

'====================Циклы с dict========================='
dict_ = {'a':1, 'b':2, 'c':3}

for k, v in dict_.items():
    print(f'ключ - {k}, а значение - {v}')



