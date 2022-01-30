# task Nr.1--------------------------------------------------------------------------------
# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

pi = 3.1415926

s = round(pi * radius ** 2, 4)

print(s)

# task Nr.2----------------------------------------------------------------------------------
# Далее, пусть есть координаты точки
point = (23, 34)

# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

distance = round(((0 - point[0]) ** 2 + (0 - point[1]) ** 2) ** .5, 4)

print('coordinates (23, 34) within a circle:', distance <= radius)

point_2 = (30, 30)

# где 30 - координата х, 30 - координата у

distance = round(((0 - point_2[0]) ** 2 + (0 - point_2[1]) ** 2) ** .5, 4)

print('coordinates (30, 30) within a circle:', distance <= radius)
