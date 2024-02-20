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


set1 = {i for i in range(10)}
set2 = {i for i in range(56, 66)}
full_set = set1.union(set2)
res = {i if len(i) < 20  else "Ваш объединенный сет полностью уникальный!" for i in full_set}

