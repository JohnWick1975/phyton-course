# Есть строка с перечислением фильмов


my_favorite_movies = 'Terminator, The Fifth Element, Avatar, Aliens, Back to the Future'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

movies = my_favorite_movies

print('\n', movies[:10], '\n', movies[-18:], '\n', movies[12:29], '\n', movies[-26:-20])
