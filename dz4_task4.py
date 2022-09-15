#4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное 
#количество символов влево или вправо. 
#При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать
# "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
#Сдвиг часто называют ключом шифрования.
#Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также 
#функцию, которая спрашивает ключ, считывает текст и дешифровывает его


# #def ceasar(str):
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# message = input('Введите строку: ').lower()
# key = int(input('Введите ключ: '))
# encrypted = ''
# for letter in message:
    # if letter in alphabet:
        # pos = alphabet.find(letter)
        # new_pos = (pos + key) % len(alphabet)
        # encrypted += alphabet[new_pos]
    # else:
        # encrypted += letter
# print ('зашифрованное слово: ', encrypted)
# #print(ceasar(str))

# def write_file():
    # new_l =str.append(encrypted)
    # print(new_l)
    # f = open('file.txt', 'w')
    # f.write(new_l)
    # f.close()
# write_file()


def read_file(n_stri):
    x = open('file.txt', 'r')
    n_stri = str(x.readline())
    x.close()
    return n_stri
