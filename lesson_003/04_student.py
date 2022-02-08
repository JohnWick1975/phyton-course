# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
i = 0
months_expenses = 0
month_money_needed = 0
money_needs = 0

while i < 10:
    if i == 0:
        months_expenses = expenses
    elif i >= 1:
        months_expenses = months_expenses * 1.03
    i += 1
    month_money_needed = round(months_expenses - educational_grant, 2)
    money_needs += month_money_needed
    print(f'{i + 1} month money needed = {month_money_needed}, total money needed {round(money_needs)}')


print(f'student should ask {money_needs} RUB ')
