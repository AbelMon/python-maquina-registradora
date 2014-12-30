"""This is a cash register program."""
import sys
articles = {}
InStock = {}
reviewnum = []
products = []


def AddItem():
	print "Type 'inventory' in 'Add item', to see the added items currently."
	print "------- Add to Inventory -------"
	quantity ()
	arti()
	price()
	print articles
	FunctionInstock()
	again()

def ItemMenu():
	print "instructions"
	
def again():
	"""Esta funcion pregunta si se quieren agregar mas articulos"""	
	question=raw_input("Do you want to insert another article y/n ")
	questionlower = question.lower()
	if questionlower == "y" or questionlower == "yes" or questionlower == "y " or questionlower == "yes ":
		AddItem()
	elif questionlower == "n" or questionlower == "no" or questionlower == "n " or questionlower == "no ":
		menu()
	else:
		print "que quieres que haga?"
		again()

def save():
	questionsave = raw_input("Save changes? y/n ")
	savelower = questionsave.lower()
	if savelower == "y" or savelower == "yes":
		Inventoryfile = open("inventory.txt","w")
		Inventoryfile.write("articles")
		Inventoryfile.close()
	else:
		print "Que quieres que haga?"
		save()


def quantity():
	try:
		global numbarticles
		numbarticles = int(raw_input("Cantidad de articles: "))
		if numbarticles < 0:
			print "Fuera de rango"
			quantity()
	except:
		print "Ingresa datos validos"
		quantity()

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
		print InStock
	except:
		print "Ingresa correctamente los datos"
		price()

def FunctionInstock():
	InStock[keylow] = numbarticles
	print InStock


def review(key):
	sameArt = articles.has_key(key)
	if sameArt == True:
		QuestionModif = raw_input("quieres modificar algun dato? ")
		answer = QuestionModif.lower()
		try:
			if answer == "y" or answer == "yes":
				newprice()
			elif answer == "no" or answer == "n":
				again()
			else:
				print "que qieres que haga"
				review(key)
		except:
			print "ingresa algun dato"
			newprice()

def newprice():
	try:
		value = float(raw_input("Add new price: "))
		articles[keylow] = value
		print articles
		again()
	except:
		print "Ingresa correctamente los datos"
		newprice()

def menu():
	chooseOpt = 0
	print "Press 1 if you want to add an item."
	print "Press 2 if you want to sell an item."
	print "Press 3 if you want to exit."
	while chooseOpt != 3:
		try:
			chooseOpt = int(raw_input("Choose an option: "))
			if chooseOpt == 1:
				AddItem()
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