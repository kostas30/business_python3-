def s():
	tameio = 100 
	prices = float(input("γράψε την αξία πώλησης :"))
	money = float(input("γράψε ενα  αριθμό:"))
	
	if tameio < money:
		print("δεν έχει   ρέστα")
	elif tameio >= money:
		print("Το  ταμείο  έχει να  δώσει  ρέστα ")
		if prices == money:
			print("πελάτης  δεν  χρήζεται ρέστα ")
		elif prices < money:
			resta = money - prices
			print(resta)


s()
