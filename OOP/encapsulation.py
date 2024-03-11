'======================Encapsulation======================'
# Инкапсуляция - принцип ООП, у которого есть 2 трактовки
# 1. Сбор всех данных, аттрибутов и методов в одну 'капсулу' (class)
# 2. Сокрытие данных, есть 3 уровня сокрытия данных

"Виды доступа к аттрибутам"
#1 public (публичный)
#2 protected (защищенный) - c одним  underscore в начале (_name, _fly)
#3 private (приватный) - с двумя underscore (__name, __fly)

# class A:
#     attr1 = 'публичный'
#     _attr2 = 'защищенный'
#     __attr3 = 'приватный'

# print(A.attr1)
# print(A._attr2)
# # print(A.__attr3) # не найдет, python добавляет в начало аттрибута underscore и название класса
# print(A._A__attr3)

# print(A.__dict__)

'================================Getters/Setters========================================'
# Функции, для работы с приватными, защищенными и публичными аттрибутами. При помощи этих функций можно получать и менять значения аттрибутов

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age
    
#     def set_age(self, new_age):
#         if new_age > 0:
#             self.__age = new_age
#         else:
#             raise Exception('Возраст не может быть меньше 0')
        
# obj = Person('Anonym', 30)
# print(obj.get_age())
# obj.set_age(50)
# print(obj.get_age())

'-----------------------------------------------------'
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age
    
#     @age.getter
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, new_age):
#         if type(new_age) != int:
#             raise Exception('Введите возраст как число')
#         if new_age > 0:
#             self.__age = new_age
#         else:
#             raise Exception('Введите число больше 0')   
        

# obj = Person('Anonym', 30)
# print(obj.age)
# obj.age = 50
# print(obj.age)


'@property - декоратор который позволяет обращаться к методам как к аттрибутам'

'@name.setter - декоратор, который позволяет менять значение защищенного аттрибута'

'@name.getter - декоратор, который позволяет получать значение защищенного аттрибута'


class Phone:
    def __init__(self, number):
        self.__number = number

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number):
        if type(new_number) != str:
            raise Exception('Введите ввиде текста')
        if len(new_number) != 13:
            raise Exception('Некорректный номер')
        if not new_number.startswith('+'):
            raise Exception('Добавьте символ "+"')
        
        self.__number = new_number

phone = Phone('+996558328877')
print(phone.number)
phone.number = '+996555999333'
print(phone.number)
