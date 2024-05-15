# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# data  = "a a a b c a a d c d d".split()
# res = {}

# for el in data:
#     if el not in res:
#         print(el, end=" ")
#     else:
#         print(f"{el}_{res[el]}", end=" ")
#     res[el] = res.get(el, 0) + 1
        

########################################################################
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# data = """She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells""".lower().split()

# print(len(set(data)))



#########################################################################
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Ваня:
# n = int(input())
# max_number = 1000 -
# while n != 0:
#  n = int(input())
#  if max_number > n: -
#  max_number = n
# print(max_number)
# 
# 
# Петя:
# n = int(input()) -
# max_number = -1
# while n < 0: -
#  n = int(input())
#  if max_number < n:
#  n = max_number -
# print(n) -


#наше решение
# n = int(input())
# max_number = n
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

#таже задача только с рекурсией
# def func(n,max_number):
#     if n == 0:
#         return max_number
#     n = int(input())
#     if max_number < n:
#         max_number = n
#     return func (n, max_number)
# n = int(input())
# print(func(n, n))

################################################################

    
