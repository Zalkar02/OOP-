class Plane:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def __str__(self):
		return self.brand + ' ' + self.model


class SwimMixin:
	def swim(self):
		print('Swim')


class Destroyer(Plane, SwimMixin):
	def __init__(self, brand, model):
		self.can_fire = True
		super().__init__(brand, model)

	def fire(self):
		print('Fire')


class Stelth(Plane, SwimMixin):
	def __init__(self, brand, model):
		self.is_visible = False
		super().__init__(brand, model)

	def hide(self):
		print('Hide')


class Kukuruznik(Plane, SwimMixin):
	def __init__(self, brand, model):
		self.can_fertilize = True
		super().__init__(brand, model)

	def fertilize(self):
		print('Fertilize')


d = Destroyer('hok', 'dgds23q3')
s = Stelth("cd", 'xsx32')
k = Kukuruznik('frsf', 'of96')

print(f'{d} \n{s} \n{k}')
print(d.can_fire)
print(s.is_visible)
print(k.can_fertilize)

d.fire()
d.swim()

s.hide()
s.swim()

k.fertilize()
k.swim()