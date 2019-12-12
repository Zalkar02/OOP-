class Book:
	def __init__(self, name, pages, author):
		self.name =name
		self.pages =pages
		self.author =author

	def __repr__(self):
		return self.name + ', ' + self.author

	def __str__(self):
		return self.name

	def __add__(self, num):
		return self.pages + num

	def __sub__(self, num):
		return self.pages - num

	def __lt__(self, num):
		return self.pages < num

	def __le__(self, num):
		return self.pages <= num

	def __ne__(self, num):
		return self.pages != num

	def __gt__(self, num):
		return self.pages > num

	def __ge__(self, num):
		return self.pages >= num


book1 = Book('Изучаем Python', 833, "Марк Лутц")
book2 = Book('Грокаем алгоритмы', 290, "Адитья Бхаргава")

print(book1)
print(book2)

print(book1.__repr__())
print(book2.__repr__()) 

print(book1.__add__(book2.pages))
print(book1.__sub__(book2.pages))
print("Меньше" ,book1.__lt__(book2.pages))
print("Меньше или равно" ,book1.__le__(book2.pages))
print("Не равно" ,book1.__ne__(book2.pages))
print("Больше" ,book1.__gt__(book2.pages))
print("Больше или равно" ,book1.__ge__(book2.pages))