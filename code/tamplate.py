from code import First


def pri_set():
	print("hello")
	meran = []
	a = First()
	for i in a.now():
		print(i)
		meran.append(f"{i:0.2f}")
	print(meran)


pri_set()
