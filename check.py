# def number():
#     while True:
#         try:
#             num = int (input(' введите число: '))
#             return num
#         except(ValueError):
#             print('вы ввели не число')
# num = abs(number())
import random

def bot_step ():
    number = random.randrange(1,28)
    print(number)   
bot_step()