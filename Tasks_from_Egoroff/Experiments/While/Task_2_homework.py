"""
Задача №3062. Утренняя пробежка
В первый день спортсмен пробежал x километров,
а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
Входные данные
Программа получает на вход действительные числа x и y
Выходные данные
Программа должна вывести одно натуральное число - номер дня, на который пробег спортсмена составит не менее y километров.
"""
start = 10 # километра
finish = 20 # дня
day = 1
while start <= finish:
    start = start * 1.1
    day += 1
print(day)