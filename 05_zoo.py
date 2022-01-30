# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(1, 'bear')

print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка

birds = ['rooster', 'ostrich', 'lark', ]

#  и выведите список на консоль

zoo.extend(['rooster', 'ostrich', 'lark'])

print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

print('\n', 'lion in a cage Nr. - ', zoo.index('lion') + 1, '\n', 'lark in a cage Nr. - ', zoo.index('lark') + 1)
