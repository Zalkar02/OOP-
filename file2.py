class WashingMachine:
	def __init__(self):
		self.powder = 1000
		self.conditioner = 1000

	def __subtract_powder(self, num):
		self.powder -= num

	def __subtract_conditioner(self, num):
		self.conditioner -= num

	def wash_clothes(self, powder, conditioner):
		if self.conditioner >= conditioner and self.powder >= powder:
			self.__subtract_powder(powder)
			self.__subtract_conditioner(conditioner)
			print('Процесс стирки завершен!')
		else:
			if self.powder < powder:
				n = self.powder - powder
				print(f'“Пополните запасы порошка на {-n} гр!')
			if self.conditioner < conditioner:
				n = self.conditioner - conditioner
				print(f'“Пополните запасы ополаскивателя на {-n} гр!')


if __name__ == '__main__':
	wm = WashingMachine()
	powder = int(input('Введите количества порошка: '))
	conditioner = int(input('Введите количества ополаскивателя: '))
	wm.wash_clothes(powder,conditioner)