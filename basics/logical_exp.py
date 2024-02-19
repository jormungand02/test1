'===========Логические и условные операторы============'
# логические операторы - это выражения, которые возвращают True, если выражения верное, False - если выражение не верное

'равенство'
5 == 6 # False 
5 == 5 # True

'неравенство'
4 != 5 # True
5 != 5 # False

'больше'
10 > 0 # True
-5 > 2 # False

'меньше'
5 < 4 # False
5 < 10 # True

'больше или равно'
5 >= 10 # False
10 >= 5 # True
5 >= 5 # True

'меньше или равно'
10 <= 5 # False
5 <= 10 # True
5 <= 5 # True

'============And, Or, Not============'

# and - и
# or - или
# not - не

'AND'
a = 5
b = 6

# True and True --> True
a == 5 and b == 6 
# True and False -->False
a == 5 and b == 3 # False
# False and False --> False
a > 10 and b < 2

# возвратится True, если справа True и слева True.
# если хотябы с одной стороны будет False, либо сразу в двух сторонах то возвратится False

'OR'
a = 20
b = 5
# True или True  --> True
a == 20 or b > 1
# True или False --> True 
a == 20 or b < 1
# False или True --> True
a > 100 or b == 5 
# False или False --> False
a < 10 or b < 1 


# если хотябы одна часть выражения возвращает True, то будет True

'NOT'

# not False - True
# not True - False
a = 5
not a < 10 # False
not a != 5 # True

not not not not not a != 10 # True

b = 10 
c = 5
a <= 10 and c < 10 
not b <= 10 and c < 10 # False

'=========Boolean Type========='
# Булевый тип данных имеет всего 2 значения 

# булевый тип данных используется в условных операторах, для выполнения ситуативных задач

bool(1) # True
bool(0) # False
bool(-123) # True

bool('hello') # True
bool(' ') # True
bool() # False


bool(True) # True
bool(False) # False

bool([]) # False
bool([[]]) # True

'===============None Type=============='
# None - неизменямый тип данных с одним значением - None, который используется для обазначения отсуствия значения 

a = None
print(a) 

bool(None) # False 
bool('None') # True

'=============Услоные операторы ================='
# условные операторы - констуркция, которая используется для того, чтобы при разных входных данных код работал по разному





num = int(input('введите число: '))
if num > 0:
    print(f'Число {num} - положительное')
elif num < 0:
    print(f'число {num} - отрицательное')
elif num == 0:
    print(f'числа {num} равные ')
else:
    print('If не сработал, elif не сработал')



'Тернарный оператор'
# тернарный оператор - условие в одну строку

# telo1 if uslovie1 else telo2

a = -20
res = a ** 2 if a > 0 else a - 2
print(res)





