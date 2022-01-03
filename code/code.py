import time


class First:
	def __int__(self, one, two):
		self.one = one
		self.two = two
		self.now()

	def now(self):
		timer1 = time.time()
		# print(f"{timer1:.2f}")
		time.sleep(2.2)
		timer2 = time.time()
		# print(f"{timer2:.2f}")
		time.sleep(2.2)
		timer3 = time.time()
		# print(f"{timer3:.2f}")
		return timer1, timer2, timer3


class Second:
	pass


a = First()
print(a.now())
