# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

def number():
    while True:
        try:
            num = float (input(' введите число: '))
            return num
        except(ValueError):
            print('вы ввели не число')
num = number()

sum = 0
for i in str(num):
    if i != ".":
        sum += int(i)
print(sum)

# num = InputNumbers("Введите число: ")

# print(f"Сумма цифр = {sumNums(num)}")
# num = int(input('введите число'))
 
# sum_digits = 0
# if num > 0:
    #  while num > 0:
        #  digits = num % 10
        #  sum_digits = sum_digits + digits
        #  num = num // 10
        
# else:
    #  num = (-1) * num
    #  while num > 0:
        #  digits = num % 10
        #  sum_digits = sum_digits + digits
        #  num = num // 10
# print('сумма цифр числа:', sum_digits)

# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('введите число : '))
# faktorial_num = 1
# for i in range(1, num+1):
    # faktorial_num *= i
    # print(faktorial_num)

# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

# def polindrom(s):
    # return s == s[::-1]
# print(polindrom('3245'))

# def polindrom(s):
    # stri1 = ''
    # for i in range(len(s)-1, -1,-1):
        # stri1 += s[i]
    # print(stri1)
    # if s == stri1:
             
        # print('число палиндром')

    # else:
           
        # print('число не палиндром')
        # sum = (stri1)+(s)
        # print(sum)
            
# polindrom('9393')

# 4 - Реализуйте выдачу случайного числа не использовать random.randint и вообще библиотеку random Можете использовать

# a = set()

# for i in range(20):
    # a.add(str(i))

# for e in a:
    # print(int(e))
    # break
  