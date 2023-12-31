"""
A. Вася и носки
У Васи есть n пар носков. Утром каждого дня, собираясь в школу, Вася должен надеть пару носков.
Вечером, прийдя со школы, Вася снимает надетые носки и выбрасывает их.
Каждый m-й день мама покупает Васе одну пару носков.
Она делает это поздно вечером, поэтому Вася может надеть новые носки не раньше следующего дня.
На сколько подряд идущих дней Васе хватит носков?
"""
socks, mama_day = map(int, input("Введите количество носков и день, на который мама купит носки: ").split(' '))
day = 0
while socks > 0:
    socks -= 1
    day += 1
    if day % mama_day == 0:
        print(f'Мама пришла на {day}-й день.')
        socks += 1
print(day)
