import simple_draw as sd

# Нарисовать радугу: 7 линий толщиной 4 с шагом 5 из точки (50, 50) в точку (550, 550)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_YELLOW, sd.COLOR_ORANGE, sd.COLOR_GREEN, sd.COLOR_CYAN,
                  sd.COLOR_BLUE, sd.COLOR_DARK_PURPLE)

step = 0

for color in rainbow_colors:
    start_point = sd.get_point(50+step, 50)
    end_point = sd.get_point(550+step, 550)
    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
    step += 5
sd.sleep(3)
sd.clear_screen()

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


step = 0
for color in rainbow_colors:
    center_position = sd.get_point(300, -50)
    sd.circle(center_position=center_position, radius=350 + step, color=color, width=30)
    step += 30
sd.pause()
