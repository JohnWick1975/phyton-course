# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

months_day_count = {'1':  31,
                    '2':  28,
                    '3':  31,
                    '4':  30,
                    '5':  31,
                    '6':  30,
                    '7':  31,
                    '8':  31,
                    '9':  30,
                    '10': 31,
                    '11': 30,
                    '12': 31,
                    }

month = input('Input month number (1 - 12): ')

if month in months_day_count:
    print(f'{month} month have: {months_day_count[month]} days')
else:
    print('is incorrect month number!')
