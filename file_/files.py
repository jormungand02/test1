# '=============Module & package==============='
# # .py - module 
# # more modules - package 

# '=============File============'
# # open() - функция, которая открывает файл в определном режиме 

# # r - read(только для чтения) (стоит по умолчанию)
# # w - write(только для записи, каждый раз файл очищается)
# # a - append (только для дозаписи, добаляется в конец)
# # x - созадет файл, но если он сушествует выйдте ошибка 

# '--------------Read-----------------'
# file = open('test1.txt', 'r')
# file.close()
# print(dir(file))
# print(file.writable()) # False
# print(file.readable()) # True
# print(file.read())
# file.seek(15) 
# print(file.read())
# print(file.read(10))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.tell())
# print(file.readlines())

# 'read -> str, readline -> str, readlines:List[str]'

# print(file.tell())


# '====================Write===================='
# file = open('test1.txt', 'w')
# file.write('Makers\nHELLO WORLD\n')
# file.writelines(['hello world\n', 'makers\n'])
# file.close() 

# 'write(str) , writelines(List[str, str])'

# '===================Append======================'
# # append(a) - добваляется в конец

# file = open('test1.txt', 'a')
# file.write('py33\n')
# file.seek(0)
# file.write('py32\n')

# '===================Контекстный менеджер=================='
# # with

# with open('test1.txt', 'r') as file:
#     print(file.read())

# print(file.closed) # True - файл закрылся False - открыт
