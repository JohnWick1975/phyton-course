# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 37, 3

i = a
int_div = 0

while i >= 0:
    i -= b
    if i > 0:
        int_div += 1

print(f'integer division {a} / {b} = {int_div}')
