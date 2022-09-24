# Формат: Объясняет преподаватель
# 
# **Задача: предложить улучшения кода для уже решённых задач:
# 
# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**
#
# 1- Определить, присутствует ли в заданном списке строк, некоторое число
# lst_1 = ['1','21','35','6','8', 'anf']
# 
# def check_number():
#      while True:
#          try:
#              num = int (input(' введите число: '))
#              return num
#          except(ValueError):
#              print('вы ввели не число')
# 
# num = check_number()
# if [l for x in lst_1 for l in x if l == str(num)] :
#     print ('число найдено в списке')
# 
# else : 
#      print ('числa нет в списке')

# 2- Найти сумму чисел списка стоящих на нечетной позиции
# lst_1 = [1, 2,6,8,8,10]
# def SumOdds(lst_1):
#    return sum(lst_1[i] for i in range(1,len(lst_1)) if not i%2 ==0 )
# print(SumOdds(lst_1))

# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
# a = input('введите координаты точки A через запятую')
# b = input('введите координаты точки B через запятую')
import math
input1 = input('введите координаты тoчки через пробел : ')

input2 = input('введите координаты тoчки через пробел : ')
a = input1.split()
b = input2.split()
print(a)
print(a)
dist = zip(a,b)
print (dist)
# print(f'расстояние  = {round(sqrt((a-b)**2),2)}')
# def find_distance():
        # coordinata_a_x = int(input('введите координату точки A по оси X:'))
        # coordinata_a_y = int(input('введите координату точки A по оси Y:'))
        # coordinata_b_x = int(input('введите координату точки B по оси X:'))
        # coordinata_b_y = int(input('введите координату точки B по оси Y:'))
        # print(f'расстояние  = {round(sqrt((coordinata_b_x -coordinata_a_x)**2 + (coordinata_b_y -coordinata_a_y)**2),2)}')

# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# x = input('введите буквы для поиска:') 
# n = [n for (n,e) in enumerate(lst) if e == x] 
# print(n)


# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.



# 6-Сформировать список из N членов последовательности.
# 
# def number():
#     while True:
#         try:
#             num = int (input(' введите число: '))
#             return num
#         except(ValueError):
#             print('вы ввели не число')
# number_n = number()
# 
# a = list( (-3)**x for x in range(number_n))
# print(a)
