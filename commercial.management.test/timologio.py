
import sys

def data():
	# εισαγωγη στοιχειων τιμολογιου
	fullyear=input("ημερα/μηνας/ετος:")
	# here=input("Τοπος:")
	bissnes_name =input("Επονυμια:")
	AFM=input("ΑΦΜ:")
	andress=input("Διευθηνση :")
	city=input("Πολη:")
	tel1=input("τηλ:")
	# Περιγραφη πωλησης ή αγορας τιμολογιου 
	description= input("περιγραφη:")    #περιγραφη
	quantity=float(input("ποσοτητα :") )       #ποσοτητα
	unit_price=float(input("τιμη μοναδας:"))		#τιμη μοναδας
	Value= 	quantity * unit_price		#Αξια
	epi100=int(input("συντελεστης φπα :" ))
	fpa= Value*(epi100/100)
	fullnum = Value + fpa
	print(f" στην ημερομινια {fullyear}, παραγματοποιηθηκε {description} συνολικης αξιας {fullnum} \
		της ποσοτητας {quantity} με τιμη μοναδας  και Συντελεστη ΦΠΑ {epi100} στον {bissnes_name} με ΑΦΜ: {AFM}και που εχει εδρα {andress} ,{city},{tel1} ")

def import_date():
	# εισαγωγη αγωρων 
	pass


def export_date():
	#  πωλησης 
	pass



data()
