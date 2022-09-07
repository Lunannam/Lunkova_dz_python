#  напишите программу , кот приним на вход число N
# и выдает последовательность из N членов 
# Пример для N = 5 : 1, -3 , 9 , - 27 , 81

# def number():
    # while True:
        # try:
            # num = int (input(' введите число: '))
            # return num
        # except(ValueError):
            # print('вы ввели не число')
# number_n = number()

# for i in range(number_n):
    # print((-3)** i, end= ', ')

# найти сумму элементов массива ,лежащих между макс и мин по значению элементами
# [ 1,8,16,3,5,9,4] 1+8+16 = 25

# list_number = [ 1,8,16,3,5,9,4]
# index_min = list_number.index(min(list_number))
# index_max = list_number.index(max(list_number))
# if index_max > index_min:
    # result = sum(list_number[index_min:index_max+1])
    
# else:
    # result = sum(list_number[index_max:index_min+1])
# print(result)

# найдите кол-во элементов массива, КОТ отличны от
# наибольшего элемента не более чем на 10%

# list_number = [ 1,8,10,7,5,9,4]
# count = 0
# max_num = max(list_number)
# number_10 = max_num * 0.1

# for i in list_number:
    # if i != max_num:
        # if (max_num - i) <= number_10:
            # count += 1
# print(count)



# cортировка пузырьком

list_num = [ 1,8,10,7,5,9,4]
n= len(list_num)
for i in range(n-1):
    for j in range (n-i-1):
        if list_num[j] > list_num[j +1]:
            list_num[j], list_num[j +1] = list_num[j +1] , list_num[j]
print(list_num)