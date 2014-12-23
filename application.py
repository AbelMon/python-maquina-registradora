"""This is a cash register program."""
import sys
articles = {}
review = []
products = []

def addItem():
	"""Esta funcion permite agregar datos a las listas y diccionarios"""
	try:
		key = raw_input("Add item: ")
		keylow = key.lower()
		sizeinp = len(key)
		review(key)
		if sizeinp > 0:
			value = float(raw_input("Add price: "))
			print articles
			print products
		else:
			print "Ingresa algun dato"
			print articles
			print products
			addItem()
		articles[keylow] = value
		print articles
		print products
		again()
	except ValueError:
		print "Ingresa correctamente los datos"
		print articles
		print products
		addItem()

def changevalue():
	"""Esta funcion pregunta si se quiere cambiar el valor a un articulo"""
	print "Quieres cambiar valor"
	
def again():
	"""Esta funcion pregunta si se quieren agregar mas articulos"""
	question=raw_input("Do you want to insert another article y/n ")
	questionlower = question.lower()
	if questionlower == "y" or questionlower == "yes" or questionlower == "y " or questionlower == "yes ":
		addItem()
	elif questionlower == "n" or questionlower == "no" or questionlower == "n " or questionlower == "no ":
		menu()
	else:
		print "que quieres que haga?"
		again()

def correctinput():
	"""Esta funcion valua si las entradas son correctas"""
	print "lol"


def sellArt():
	print "olakase"

def review(key):
	redefin = articles.has_key(key)
	if redefin == True:
		abc = raw_input("lola y/n")
		cde = abc.lower()
		return cde


def menu():
	chooseOpt = 0
	print "Press 1 if you want to add an item."
	print "Press 2 if you want to sell an item."
	print "Press 3 if you want to exit."
	while chooseOpt != 3:
		try:
			chooseOpt = int(raw_input("Choose an option: "))
			if chooseOpt == 1:
				addItem()
			elif chooseOpt == 2:
					sellArt()
			elif chooseOpt <= 0:
				print "Valor no valido"
				chooseOpt
			elif chooseOpt > 3:
				print "valor no valido"
				chooseOpt
			elif chooseOpt == 3:
				sys.exit(3)
		except ValueError:
			print "Ingresa una opcion valida"
menu()
