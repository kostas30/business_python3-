
import sys

def data():
	# εισαγωγη στοιχειων τιμολογιου
	day=input("ημερα:")
	month=input("μηνας:")
	year=input("ετος:")
	here=input("Τοπος:")
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

def import_date():
	# εισαγωγη αγωρων 
	pass


def export_date():
	#  πωλησης 
	pass