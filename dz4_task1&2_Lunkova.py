# 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from unittest import result


#def number():
#    while True:
#        try:
#            num = int (input(' введите натуральное число: '))
#            return num
#        except(ValueError):
#            print('вы ввели не число')
#
#def prime_factor(): 
#    num_input = abs(number())
#    i = 2 
#    new_lst = []
#    
#    while i <= num_input :
#        if num_input % i == 0:
#            new_lst.append(i)
#            num_input //= i
#            i = 2
#        else:
#            i += 1
#    print(f"Простые множители : {new_lst}")
#
#prime_factor()

# 2 - Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
#  Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

#lst_1 = [1,1,1,1,2,2,2,3,3,3,4]
#uniq_elem =[]
#[uniq_elem.append(i) for i in lst_1 if i not in uniq_elem]
#
#print(f'список уникальных элементов: {uniq_elem}')
#5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.
#файл первый:
#AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
#файл второй:
#сжатый текст.
def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res