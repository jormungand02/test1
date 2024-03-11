'======================OOP========================='
# OOP - object-orientated programing
# ООП - объектно-ориентированное программирование (парадигма)

class Person:
    # переменные, которые находятся внутри класса называются аттрибутами
    head = 1
    body = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name} ходит')

int
obj1 = Person('Tima', 35)
obj2 = Person('Katana', 21)
print(obj1.name, obj1.age, obj1.head, obj1.body)
print(obj2.name, obj2.age, obj2.head, obj2.body)      


obj1.walk()
obj2.walk()


'Объекты, экземпляры, instance - конечный продукт, созданный по шаблону класса(он перенимает все аттрибуты и методы класса)'

class A:
    var1 = 'аттрибут класса'

    def __init__(self):
        self.var2 = 'аттрибут объекта'

print(dir(A)) # класс не видит аттрибуты объекта


obj1 = A()
print(dir(obj1)) # объект видит аттрибуты класса

'self - это ссылка на объект'
# Что отрабатывает при создании объекта
obj1 = Person('makers', 5)
'__new__ - создает пустой объект'
'__init__ - инициализирует этот объект (создает аттрибуты со значениями внутри пустого объекта)'


class Calc:
    def add(self, a, b):
        return a + b
    def sqrt(self, a):
        return a ** 0.5
    def percent(self, total, _percent):
        return (total * _percent) / 100
    
calc = Calc()
print(calc.add(10, 20))
print(calc.sqrt(81))
print(calc.percent(34250, 13))

class Sniper:
    health = 100

    def __init__(self, name):
        self.name = name

    def shoot(self, sniper):
        sniper.health -= 20
        print(f'атаковал {self}')
        print(f'у {sniper} осталось {sniper.health}HP')

    def __str__(self):
        return self.name

Sniper1 = Sniper('Anonim')
Sniper2 = Sniper('Tima')

import random
while Sniper1.health > 0 and Sniper2.health > 0:
    choice = random.randint(1, 2)
    if choice == 1:
        Sniper1.shoot(Sniper2)
    elif choice == 2:
        Sniper2.shoot(Sniper1)
    
if Sniper1.health:
    print(f'Выиграл снайпер {Sniper1}')
else:
    print(f'Выиграл снайпер {Sniper2}')




