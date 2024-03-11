'=============================Mixins===================================='
# Миксины - классы помощники, которые будут использоваться для наследования. Но от миксинов не создаются обьекты

class FlyMixin:
    def fly(self):
        print('Я могу летать')

class WalkMixin:
    def walk(self):
        print('Я могу ходить')

class SwimMixin:
    def swim(self):
        print('Я могу плавать')

class Human(WalkMixin, SwimMixin):
    name = 'Человек'

    def talk(self):
        print('Я могу говорить')

class Fish(SwimMixin):
    name = 'Рыба'

class Duc(WalkMixin, SwimMixin, FlyMixin):
    name = 'Утка'

objects = [Human(), Fish(), Duc()]
attrs = ['fly', 'walk', 'swim', 'talk']
for obj in objects:
    print(obj.name)
    for attr in attrs:
        if hasattr(obj, attr):
            method = getattr(obj, attr)
            method()

obj = Human()
setattr(obj, 'name', 'Сверхчеловек')
print(obj.name)


# hasattr - функция, которая принимает объект и название аттрибута. Возвращает True, если у объекта есть такой аттрибут (метод)
# getattr - функция, которая принимает объект и название аттрибута. Возвращает значение аттрибута
# setattr - функция, которая принимает объект, название аттрибута и значение аттрибута. Добавляет в объект новый аттрибут или перезаписывает старый аттрибут



