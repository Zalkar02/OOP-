class Calculator:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def __str__(self):
		return f'{self.brand} {self.model} is ready to work!'

	def add(self, num1, num2):
		return num2 + num1

	def subtract(self, num1, num2):
		return num1 - num2

	def multiply(self, num1, num2):
		return num1 * num2

	def divide(self, num1, num2):
		return num1 / num2

	def integer_division(self, num1, num2):
		return num1 // num2

	def modulo(self, num1, num2):
		return num1 % num2


if __name__ == '__main__':
	cl = Calculator('Aote', 'cl455')
	print(cl)
	print(cl.add(25+25, 65))
	print(cl.subtract(100, 12+23))
	print(cl.multiply(5,5))
	print(cl.divide(1000,300))
	print(cl.integer_division(450, 86))
	print(cl.modulo(5000, 72))