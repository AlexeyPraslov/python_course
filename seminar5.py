# Задача.
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def func(n, a=0, b=1, res=0): # входные данные
#     if n == 0: #базовый случай выхода из рекурсии
#         return res
#     return func(n-1, b, a+b, res=a+b) #вызов рекурсии и изменения данных
# print(func(5))
# ##########################################################################
# Задача
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# arr = [1, 3, 3, 3, 4]

# for i in arr:
#     if arr[i] > 3:
#         arr[i] = 1
# print(arr)

# def process_array(arr, index=0):
#     # Базовый случай рекурсии: если индекс вышел за пределы массива, завершаем рекурсию
#     if index >= len(arr):
#         return arr
#     # Проверяем текущий элемент и обновляем его, если условие выполняется
#     if arr[index] > 3:
#         arr[index] = 1
#     # Рекурсивно обрабатываем оставшуюся часть массива
#     return process_array(arr, index + 1)

# arr = [1, 3, 3, 3, 4]
# print(process_array(arr))

########################################################################
# Задача
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# def func1(n):
#     for el in range(2, n): # обход чисел от 2 до n
#         if n % el == 0: # 
#             return "no"
#     return "yes" 
# print(func1(15))
######################
# def func2(n, el=2):
#     if el < n:
#         if n % el == 0:
#             return "no"
#         return func2 (n, el+1)
#     return "yes"
# print(func2(2))

########################################################################
# Задача
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# data = "3 4"
# def func(data):
#     new_str = ""
#     for el in reversed(data):
#         new_str += el
#     return new_str
# print(func(data))
#######
# data = "3 4"
# def func2(data, new_str=""):
#     if len(data) == 0:
#         return new_str
#     return func2(data[:-1], new_str+data[-1])

# print(func2(data))
#############################################################
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# def func(a, b, res=1):
#     if b == 0:
#         return res
#     return func(a,b-1,res*a)
# print(func(3, 5))  

##############################################################
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# def summ (a, b):
#     while b != 0:
#         a += 1
#         b -= 1
#     return a
# print(summ(2, 3))
# #####

# def summ2 (a, b):
#     if b == 0:
#         return a
#     return summ2(a+1, b-1)
# print(summ2(2, 6))
############################################################### 