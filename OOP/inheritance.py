'========================Принципы ООП==========================='
# Наследование 
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация - Композиция, Агрегация

'=========================Наследование=========================='
# Наследование - принцип ООП, в котором мы можем унаследовать, переопределять и использовать в дочернем классе все аттрибуты и методы родительского класса

# class A:
#     def method(self):
#         print('Метод класса А')

# obj_A = A()
# obj_A.method()

# class B(A):
#     '''
#     Наследовали все методы и аттрибуты родительского класса А
#     '''

# obj_B = B()
# obj_B.method()

# class C(A):
#     def method(self):
#         print('Метод в классе С')

# obj_C = C()
# obj_C.method()

'----------------------------------------------------------------------------------'

# class A:
#     x = 'х в классе А'
#     y = 'у в классе А'

# class B(A):
#     x = 'x в классе B'

# print(A.x) # x в классе A
# print(A.y) # y в классе A

# print(B.x) # x в классе B
# print(B.y) # y в классе A


'------------------------------------------------------------------------------------'
'mro (method resolution order) - порядок поиска аттрибутов'

# class A:
#     ...

# class B(A):
#     ...

# # B.a

# print(B.mro()) # [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

'------------------------------------------------------------------------'

# class A:
#     def my_range(self, n):
#         return list(range(n+1))
    
# class B(A):
#     def my_range(self, n):
#         list_ = super().my_range(n)
#         list_.append(0)
#         return list_ 
    
# print(B().my_range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

'super() - это функция благодаря которой мы можем обращаться к родительскому классу'

'=======================Виды наследования=========================='
# Одиночное наследование (когда мы наследуемся в дочернем классе от 1 класса)
# Множественное наследование (когда мы наследуемся в дочернем классе от нескольких родительских)
# Многоуровневое наследование (когда мы наследуемся от класса у которых есть родитель)
# Иерархическое наследование (когда от одного родителя много дочерних классов)
# Гибридное наследование (когда используется несколько видов наследования)

'====================Проблемы множественного наследования====================='
# Проблема Ромба(Алмазная проблема)

# class A:
#     def __str__(self):
#         return 'A'
    
# class B:
#     def __str__(self):
#         return 'B'
    
# class C(A,B):
#     ...

# obj_C = C()
# print(obj_C)

# print(C.mro())

# Проблема перекрестного наследования (не решена)

# class A:
#     ...

# class B:
#     ...

# class E(A, B):
#     ...

# class D(B, A):
#     ...

# class F(E, D):
#     ...







from datetime import datetime
class SmartPhones: 
    battery = 0
    def __init__(self,name, color, memory): 
        self.name = name
        self.color = color 
        self.memory = memory
        
    def __str__(self): 
        return (f'{self.name} {self.memory}')

    def charge(self, power): 
        self.battery += power 
        
class Iphone(SmartPhones): 
    def __init__(self,name, color, memory, ios):
        self.ios = ios
        super().__init__(name, color, memory)

    def send_imessage(self,str_ ): 
        return f"sending {str_} from {self}"

class Samsung(SmartPhones): 
    def __init__(self,android, name, color, memory): 
        self.android = android
        super().__init__(name, color, memory)

    def show_time(self):
        return datetime.now().time() 

        
phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) 

print(phone.battery) 
phone.charge(20) 
print(phone.battery) 

iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 

samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time())