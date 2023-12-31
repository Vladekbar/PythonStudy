# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью.
# Поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.


n: int = int(input('Введите количество кустов: '))
if n < 4:
    print('Для данного количества кустов программа подсчета максимального сбора не требуется.')
else:
    list_1 = [int(input('Введите количество ягод для %s-го куста: ' % (i+1))) for i in range(n)]
    list_max_yield = [] # Список для хранения значений  урожайности за подход модуля.

    for i in range(n):
        list_max_yield.append(list_1[i-2] + list_1[i-1] + list_1[i])
    if list_max_yield.index(max(list_max_yield)) != 0:
        print(f'Для сбора максимального количества ягод ({max(list_max_yield)}) подгоните модуль к {list_max_yield.index(max(list_max_yield))}-му кусту.')
    else:
        print(f'Для сбора максимального количества ягод ({max(list_max_yield)}) подгоните модуль к {n}му кусту.')