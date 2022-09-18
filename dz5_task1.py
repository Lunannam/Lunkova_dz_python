
# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"
# 
# with open('Lekcia3_py\input_txt.txt', 'r', encoding = 'utf=8'  ) as data:
#     for line in data:
#         s = str.split(line)
#         print(s)
# letters = "абв" 
# '''
# letters - сочетание , которое надо найти в словах
# в 39 строке поиск в каждой сроке в списке
# вывод новой строки без слова с абв
# '''
# lst = [i for i in s if letters not in i]
# print(f' {" ".join(lst)}')

# 2- Создайте программу для игры с конфетами человек против человека.
# 
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите).
#  Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер,
#  с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
lst_2 = ['1', '2', '3', '4', '5']
lst_1 = ['Python', 'Java', 'C', 'C++', 'JavaScript']
new_lst = list(map(str.upper, lst_1))

print(new_lst)
data = list(zip(new_lst, lst_2))
print(data)

input = input(lst_1)
word = []
print(word)
 
for i in line(len):
    number =int ord(char)
    word.append(number)
    print (word)
# sums = list(map(sum, list_of_lists))

# 2- Создайте программу для игры с конфетами человек против человека.
# 
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
#  Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

################ Human Vs Human
# from random import randint
# 
# def step(name):
#     a = int(input(f"{name}, можно брать от 1 до 28, введите количество: "))
#     while a < 1 or a > 28:
#         a = int(input(f"{name}, неверный ход! Возьмите от 1 до 28 конфет: "))
#     return a
# 
# 
# def p_print(name, k, amount):
#     print(f"{name} взял {k}. На столе {amount} конфет.")
# 
# 
# player1 = input("Игрок 1, введите Ваше имя: ")
# player2 = input("Игрок 2, введите Ваше имя: ")
# amount = int(input("Напишите сколько конфет на столе: "))
# flag = randint(0,1) # жеребьевка
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
# 
# count1 = 0 
# count2 = 0
# 
# while amount > 28:
#     if flag:
#         k = step(player1)
#         count1 += k
#         amount -= k
#         flag = False
#         p_print(player1, k, amount)
#     else:
#         k = step(player2)
#         count2 += k
#         amount -= k
#         flag = True
#         p_print(player2, k, amount)
# 
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


################# BOT_глупый Vs Human
# import random
# def step(name):
#     a = int(input(f"{name}, можно брать от 1 до 28, введите количество: "))
#     while a < 1 or a > 28:
#         a = int(input(f"{name}, неверный ход! Возьмите от 1 до 28 конфет: "))
#     return a
#  
# def p_print(name, k, amount):
#     print(f"{name} взял {k}. На столе {amount} конфет.") 
# 
# def choice_regim(name):
#     
#     
#     
# 
# player1 = input("Игрок 1, введите Ваше имя: ")
# player2 = 'БОТ'
# print(f"Привет, я - глупый  {player2} , сыграем? ")
# amount = int(input("Напишите сколько конфет на столе: "))
# 
# flag = True
# if flag:
#      print(f"Первый ходит {player1}")
# else:
#      print(f"Первый ходит {player2}")
# 
# count1 = 0 
# count2 = 0
#  
# while amount > 28:
#     if flag:
#         k = step(player1)
#         count1 += k
#         amount -= k
#         flag = False
#         p_print(player1, k, amount)
#     else:
#         k = random.randrange(1,28)
#         count2 += k
#         amount -= k
#         flag = True
#         p_print(player2, k, amount)
#  
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")