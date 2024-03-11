'===================JSON=================='
#JavaScript Object Notation - универсальный формат, в котором мы можем хранить данные в итпах данных, почти для всех языков программирования

# import json
# json_data = "null"
# python_data = json.loads(json_data)
# print(python_data)

# with open('test.json', 'r') as file:
#     python_data = json.load(file)
    

# десериализация - перевод с json строки в python объекты
# loads - метод для десериализации с json строки
# load - метод для десериализации с json файла

# сериализация - перевод python  объектов в json строку
# dumps - метод для сериализации в json строку
# dump - метод для сериализации в json файл


# import json
# python_data = None
# json_data = json.dumps((python_data))
# print(json_data)

# with open('test.json', 'w') as file:
#     json.dump(json_data, file)








'==========---------------================-----------------=================----------------------================='

# with open('test1.txt', 'r') as file_:
#     for line in file_.readlines(8):
#         print(line)





# with open('test1.txt', 'a+') as file_:
#     file_.write('0*1*2*3*4*5*6*7*8*9')
#     file_.seek(0)
#     print(file_.read())
    



# with open('test1.txt', 'r') as file_:
#     print(len(file_.readlines()))



# with open('test1.txt', 'r') as file_:
#     list_ = file_.readlines()
#     list_1 = [line.replace('\n', '') for line in list_]
#     list_2 = []
#     for i in list_1:
#         res = int(i)
#         list_2.append(res)
#         min_ = min(list_2)
#         max_ = max(list_2)
# with open('test2.txt', 'w') as f:
#     f.write(f'{min_}-{max_}')




# def read_last(lines: int, filename: str):
#     with open(filename, 'r') as f:
#         list_ = f.readlines(lines)
    
# read_last(1, 'test1.txt')


def read_last(lines, filename): 
    with open(filename) as file: 
        list_ = file.readlines() 
        list_.reverse() 
        if len(list_) > lines: 
            i = 0 
            while i < lines: 
                print(list_[i].replace('\n', '')) 
                i += 1 
        else: 
            for i in list_: 
                print(i.replace('\n', '')) 
read_last(2, 'test1.txt')




# def read_last(lines, filename): 
#     with open(filename) as file: 
#         list_ = file.readlines() 
#         if lines < len(list_): 
#             i = 0 
#             reversed_list_ = list_[::-1] 
#             while i < lines: 
#                 print(reversed_list_[i].replace('\n', '')) 
#                 i+=1 
#         else: 
#             list_.reverse() 
#             for i in list_: 
#                 print(i.replace('\n', '')) 

# read_last(9, 'article.txt')

