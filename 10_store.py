# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamp_key = goods['Лампа']
lamp_quantity = store[lamp_key][0]['quantity']
lamp_price = store[lamp_key][0]['price']
lamp_general_price = lamp_quantity * lamp_price

print('\n', 'All lamp quantity in the store = ', lamp_quantity,
      '\n', 'general tables price = ', lamp_general_price)

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

table_key = goods['Стол']
table_quantity = store[table_key][0]['quantity'] + store[table_key][1]['quantity']
table_general_price = (store[table_key][0]['quantity'] * store[table_key][0]['price']) + (
        store[table_key][1]['quantity'] * store[table_key][1]['price'])

print('\n', 'All table quantity in the store = ', table_quantity,
      '\n', 'general tables price = ', table_general_price)

sofa_key = goods['Диван']
sofa_quantity_1 = store[sofa_key][0]['quantity']
sofa_quantity_2 = store[sofa_key][1]['quantity']
sofa_general_quantity = sofa_quantity_1 + sofa_quantity_2
sofa_price_1 = store[sofa_key][0]['price']
sofa_price_2 = store[sofa_key][1]['price']
sofa_general_price = (sofa_price_1 * sofa_quantity_1) + (sofa_price_2 * sofa_quantity_2)

print('\n', 'All sofa quantity in the store = ', sofa_general_quantity,
      '\n', 'general sofa price = ', sofa_general_price)

chair_key = goods['Стул']
chair_quantity_1 = store[chair_key][0]['quantity']
chair_quantity_2 = store[chair_key][1]['quantity']
chair_quantity_3 = store[chair_key][2]['quantity']
chair_general_quantity = chair_quantity_1 + chair_quantity_2
chair_price_1 = store[chair_key][0]['price']
chair_price_2 = store[chair_key][1]['price']
chair_price_3 = store[chair_key][2]['price']
chair_general_price = (chair_price_1 * chair_quantity_1) + (chair_price_2 * chair_quantity_2) + (
        chair_price_2 * chair_quantity_2)

print('\n', 'All chair quantity in the store = ', chair_general_quantity,
      '\n', 'general sofa price = ', chair_general_price)
