'==========Области видимости========'
#LEGB - local enclosed global build-in

'================Build-in================='
# встроенное пространство имен (list, print, dict, len, input)

'=============Global============='
# все переменные, которые мы создали внутри файла
# чтобы посмотреть все глобальные переменные, можно использовать функцию globals
a = 10
b = 'hello'
print(globals())

'===============enclosed==============='
# замкнутое пространство имен - это локальное пространство, у которого есть внутреннее локальное пространство

var = 'global' # хранится в глобальном пространстве

def func():
    var = 'enclosed' # замкнутое пространство
    def inner_func():
        var = 'local' # локальное пространство
        print(var)
    print(var)
    inner_func()
print(var)
func()

'==============Local=============='
# локальное пространство имен - это пространство которое находится внутри функции

a = 10
c = 'hello'
def func(a, b):
    res = a + b
    print(c)
    print(locals())
    print(globals())
func(10, 5)

def count_(num):
    count = 0
    def inner_count():
        nonlocal count
        count += 1
        print(count)

