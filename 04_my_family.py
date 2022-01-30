# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother', 'father', 'wife', 'son']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['name', height],
    ['Liuda',160],
    ['Valera',170],
    ['Natalija',176],
    ['Martynas',90]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print(my_family[1], 'height - ', my_family_height[1][1], 'centimeters')



# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print('overall family height - ', my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
      + my_family_height[3][1])
