import sys




def s():
	tameio = 100 
	prices = float(input("γραψε την αξια πωλησης :"))
	money=float(input("γραψε ενα  αριθμο:"))
	
	if tameio < money:
		print("δεν εχει   ρεστα")
	elif tameio >= money:
		print("Το  ταμειο  εχει να  δωση ρεστα ")
		if prices == money:
			print("πελατης  δεν  χρηαζεται ρεστα ")
		elif prices < money:
			resta= money -prices
			
			print(resta)

s()