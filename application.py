"""This is a cash register program."""
import sys
articles = {}
reviewnum = []
products = []

def EvaluateItem():
	print "------- Add to Inventory -------"
	arti()
	price()
	again()


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

def  arti():
	key = raw_input("Add item: ")
	global keylow
	keylow = key.lower()
	review(keylow)
	if key == "":
		print "Ingresa algun dato"
		arti()

def price():
	try:
		value = float(raw_input("Add price: "))
		articles[keylow] = value
		print articles
	except:
		print "Ingresa correctamente los datos"
		price()



def review(key):
	sameArt = articles.has_key(key)
	if sameArt == True:
		QuestionModif = raw_input("quieres modificar algun dato? ")
		answer = QuestionModif.lower()
		if answer == "y" or answer == "yes":
			try:
				value = float(raw_input("Add new price: "))
				articles[keylow] = value
				again ()
			except:
				print "ingresa algun dato"
		elif answer == "no" or answer == "n":
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
				sys.exit(0)
		except ValueError:
			print "Ingresa una opcion valida"
menu()