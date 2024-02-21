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


import json
python_data = None
json_data = json.dumps((python_data))
print(json_data)

with open('test.json', 'w') as file:
    json.dump(json_data, file)
