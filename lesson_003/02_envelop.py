# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9

# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

if envelop_x >= paper_x and envelop_y >= paper_y:
    print('paper is placed in an envelope!!!')
elif envelop_x >= paper_y and envelop_y >= paper_x:
    print('paper is placed in an envelope!!!')
else:
    print('paper DOES NOT fit in envelope')
