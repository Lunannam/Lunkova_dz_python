#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
#Пример:*
#
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#def Sum_odd():
#    my_list = [2, 3, 5, 7, 3,5]
#    result = 0
#    for i in range(1,len(my_list),2):
#        result += my_list[i]
#    return result
#print(Sum_odd())

#my_list = [2, 3, 5, 9, 3]
#print(sum(my_list[1::2]))

#__________________________________________________________________
#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

#def multiElements():
#    lst = [2, 3, 4, 5, 6]

    #'''
    #cоздает новый спискок с длинной в два р меньше начального
    #записываем в него произведение попарно элементов (1 и последний)
    #'''
#    res_lst = []
#    for i in range((len(lst)+1)//2):
#        res_lst.append(lst[i]*lst[len(lst)-i-1])
#    return res_lst
#print(multiElements())

# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# def fractional_diff():
    # lst = [1.1, 1.3, 3.1, 5, 10.01]
    # '''
    # функция создает новый список, в который помещяет дробные части чисел>0
    # далее находит рзницу между max и min значениями
    # '''
    # new_lst = []
    # for i in lst:
        # if i%1 >0:
            # new_lst.append(i%1)
    # return round(max(new_lst)-min(new_lst),2) 
   
# print(fractional_diff())

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
#*Пример:*
#
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10
#def number():
#    while True:
#        try:
#            num = int (input(' введите число: '))
#            return num
#        except(ValueError):
#            print('вы ввели не число')
#
#num = abs(number())
##num = int(input('введите десятичное натуральное число: ')) 
#bin_num = ''
#while num > 0:
#    bin_num = str(num % 2)+bin_num
#    num = num // 2
#print(f'число в двоичное системе счисления = {bin_num}')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число: '))

def fibonacci(num):
    f_nums = []
    f1, f2 = 1, 1
    for i in range(num):
        f_nums.append(f1)
        f1, f2 = f2, f1 + f2
    f1, f2 = 0, 1
    for i in range (num+1):
        f_nums.insert(0, f1)
        f1, f2 = f2, f1 - f2
    return f_nums

print(fibonacci(num))

