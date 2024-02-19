'==========Set========='
# множество - изменямый, неупорядоченный, итерируемый, неиндексируемый тип данных, для хранения уникальных значений.
# Множества могут хранить в  себе только неизменяемые типы данных, если же в set использовать tuple, то внутри tuple не должно быть изменяемого тип данных

set1 = {1, 2, 2, 3, 4, True, 'hello', None}
print(set1)

#set_2 = {1,2,3, ('hello', 1,[1,2])}
#print(set_2)

'============FIFO / LIFO==========='
# FIFO - first in first out
# LIFO - last in first out

set_ = {1,2,3,4,2}
print(set_)

'================Методы set========='
print(dir(set()))
# pop - удаляет случайный элемент из set 
set2 = {1,2,3}
popped = set2.pop()
print(popped)
print(set2)

# add - добавляет элемент в set 
set3 = {1,2,3}
set3.add(3)
print(set3) # {1, 2, 3}

# remove - удаляет элементы из set по значению
set4 = {1,2,3}
set4.remove(3)
print(set4)

# difference (-) 
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 - set2) # {1, 2}
print(set2 - set1) # {4, 5}

set3 = {5,6,7}
set4 = {6,8,9}
print(set3 - set4) # {5,7}
print(set4 - set3) # {8,9}

# symmetric_difference
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.symmetric_difference(set2)) # {1, 2, 4, 5}
print(set1)

# intersection (&)
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.intersection(set2)) # {3,4}
print(set1 & set2) # {3,4}

# union 
set1 = {1,2,3,4}
set2 = {5,6,7,8}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}

# update
set1 = {1,2,3,4}
set2 = {4,5,6,7}
set1.update(set2)
print(set1) # {1, 2, 3, 4, 5, 6, 7}



