# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# num = 5
# fact = 1

# while num > 1:
#     fact *= num
#     num -= 1
# print(fact)

# for el in range(1, num + 1):
#     fact *= el
# print(fact)

# def factorial(num, fact=1):
#     if num == 0:
#         return fact
#     return factorial(num-1, fact*num)

# print(factorial(5))


#########################################################
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# a = 5
# fiboP, fiboN = 0, 1
# position = 2

# while fiboN < a:
#     fiboP, fiboN = fiboN, fiboP + fiboN
#     position += 1
# if a == fiboN:
#     print(position)
# else:
#     print(-1)

# def func(a, fiboP=0, fiboN=1, position=2):
#     if fiboN == a:
#         return position
#     elif fiboN < a:
#         return func(a, fiboN, fiboP+fiboN, position+1)
#     else:
#         return "-1"
# print(func(5))

##########################################################
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# n = 6
# numbers = "-20 30 -40 50 10 -10".split()

# max_len = 0
# cur_len = 0

# for el in numbers:
#     num = int(el)
#     if num > 0:
#         cur_len += 1
#     else:
#         cur_len = 0

#     if cur_len > max_len:
#         max_len = cur_len

# print(max_len)

# def func(n, numbers="-20 30 -40 50 10 -10".split(), max_len=0, cur_len=0):
#     if len(numbers) == 0:
#         return max_len
    
#     num = int(numbers[0])
    
#     if num > 0:
#         cur_len += 1
#     else:
#         cur_len = 0

#     if cur_len > max_len:
#         max_len = cur_len
#     return func(n, numbers[1:], max_len, cur_len)

# print(func(6))


##########################################################
# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

# data = [5, 1, 6, 5, 9]
# # list(map(int, input("Введите числа через пробел: ").split()))
# max_num = data[0]
# min_num = data[0]

# for el in data:
#     if el > max_num:
#         max_num = el
#     if el < min_num:
#         min_num = el

# print(min_num, max_num)

# def func(data=[5, 1, 6, 5, 9], max_num=data[0], min_num=data[0]):
#     if len(data) == 0:
#         return max_num, min_num
#     if data[0] > max_num:
#         max_num = data[0]
#     if data[0] < min_num:
#         min_num = data[0]
#     return func(data[1:], max_num, min_num)

# print(func(data))




    