# 1/ Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day_number = int(input('введите число от 1 до 7:'))
# if day_number > 5:
   # print('да')
# else:
   # print('нет')

# 3/ Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# coordinata_x = int(input('введите координату по оси X:'))
# coordinata_y = int(input('введите координату по оси Y:'))
# if coordinata_x > 0 and coordinata_y > 0:
   # print('1 четверть плоскости')
# if coordinata_x < 0 and coordinata_y < 0:
   # print('3 четверть плоскости')
# if coordinata_x < 0 and coordinata_y > 0:
   # print('2 четверть плоскости')
# if coordinata_x > 0 and coordinata_y < 0:
   # print('4 четверть плоскости')

# 4/ Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter_numb = int(input('введите номер четверти плоскости координат'))
# while quarter_numb != 1 or 2 or 3 or 4:
    # quarter_numb = int(input('введите номер четверти плоскости координат'))
    # if quarter_numb == 1:
        # print('координаты точки по оси х > 0 и по оси y > 0')
    # if quarter_numb == 2:
        # print('координаты точки по оси х < 0 и по оси y > 0')
    # if quarter_numb == 3:
        # print('координаты точки по оси х < 0 и по оси y < 0')
    # if quarter_numb == 4:
        # print('координаты точки по оси х > 0 и по оси y < 0')

# 5/ -Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# from cmath import sqrt


# def find_distance():
        # coordinata_a_x = int(input('введите координату точки A по оси X:'))
        # coordinata_a_y = int(input('введите координату точки A по оси Y:'))
        # coordinata_b_x = int(input('введите координату точки B по оси X:'))
        # coordinata_b_y = int(input('введите координату точки B по оси Y:'))
        # print(f'расстояние  = {round(sqrt((coordinata_b_x -coordinata_a_x)**2 + (coordinata_b_y -coordinata_a_y)**2),2)}')
# find_distance()
# 2/ Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.


print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not(x and y and z)) == ((not x) and (not y) and (not z)) :
                print(x, y, z, True)
            else:
                print(x, y, z, False)
