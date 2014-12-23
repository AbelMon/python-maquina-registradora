"""This is a cash register program."""
import sys
articles = {}
reviewnum = []
products = []

def EvaluateItem():
	"""Esta funcion permite agregar datos a las listas y diccionarios"""
	try:
		key = raw_input("Add item: ")
		global keylow
		keylow = key.lower()
		sizeinp = len(key)
		review(keylow)
		if sizeinp > 0:
			value = float(raw_input("Add price: "))
			print articles
			print "1"
		else:
			print "Ingresa algun dato"
			print articles
			print "2"
			EvaluateItem()
		articles[keylow] = value
		print articles
		print "3"
		again()
	except ValueError:
		print "Ingresa correctamente los datos"
		print articles
		print ""
		EvaluateItem()

def addItem():
	print "Quieres cambiar valor"
	
def again():
	"""Esta funcion pregunta si se quieren agregar mas articulos"""
	question=raw_input("Do you want to insert another article y/n ")
	questionlower = question.lower()
	if questionlower == "y" or questionlower == "yes" or questionlower == "y " or questionlower == "yes ":
		EvaluateItem()
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
		abc = raw_input("quieres modificar algun dato? ")
		cde = abc.lower()
		if cde == "y" or cde == "yes":
			try:
				value = float(raw_input("Add new price: "))
				reviewnum = value
				articles[keylow] = value
			except:
				print "ingresa algun dato"
		elif cde == "no" or cde == "n":
			again()
		else:
			print "que qieres que haga"
			review(key)



def menu():
	chooseOpt = 0
	print "Press 1 if you want to add an item."
	print "Press 2 if you want to sell an item."
	print "Press 3 if you want to exit."
	while chooseOpt != 3:
		try:
			chooseOpt = int(raw_input("Choose an option: "))
			if chooseOpt == 1:
				EvaluateItem()
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