def decorator(func):
	try:
		temp = int(input('Ведите температуру: '))
	except ValueError:
		print('Ведите число, а не букву')

	if temp >= 10:
		func()
		print('На улице тепло, давай погуляем, я непротив!')
	elif temp >= 0 and temp < 10:
		func()
		print('Прохладно.Надо одеться!')
	elif temp >= -10 and temp < 0:
		func()
		print('Холодно. Потеплее оденься и пойдем!')
	elif temp < -10:
		print('Мороз. Лучше давай дома посидим, фильм посмотрим!')

@decorator
def go_for_a_walk():
	print('Давай, пойдем погуляем на улице!')

go_for_a_walk