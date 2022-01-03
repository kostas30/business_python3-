def data():
	# εισαγωγή στοιχειών τιμολογίου
	day = input("ημέρα:")
	month = input("μήνας:")
	year = input("έτος:")
	here = input("Τόπος:")
	bissnes_name = input("Επωνυμία:")
	AFM = input("ΑΦΜ:")
	andress = input("Διεύθυνση :")
	city = input("Πόλη:")
	tel1 = input("τηλ:")
	# Περιγραφή πώλησης ή αγοράς τιμολογίου
	description = input("περιγραφή:")    # περιγραφή
	quantity = float(input("ποσότητα :"))       # ποσότητα
	unit_price = float(input("τιμή μονάδας:"))		# τιμή μονάδας
	Value = 	quantity * unit_price		# Αξία
	epi100 = int(input("συντελεστής φπα :"))
	fpa = Value*(epi100/100)


def import_date():
	# εισαγωγή αγορών
	pass


def export_date():
	#  πώλησης
	pass
