"""This is a cash register program."""
import sys
<<<<<<< HEAD
import os
ARTICLES = {
    "pera":2.0, "manzana":2.5,
    "sandia":12, "melon":10.0,
    "naranja":1.5, "tomate":0.75, "shampoo":19.5, "jabon":7.5
}

INSTOCK = {
    "pera":28, "manzana":37, "sandia":50,
    "melon":15, "naranja":80,
    "tomate":60, "shampoo":17, "jabon":20
}

SELLLIST = []
GOLDSIL = []
SELLDIC = {}
SUBTOTALDIC = {}

def menu():
    """Main menu"""
    chooseopt = 0
    print ""
    print "====================Menu===================="
    print "Press 1 if you want to add an item."
    print "Press 2 if you want to sell an item."
    print "Press 3 if you want to exit."
    print ""
    while chooseopt != 3:
        try:
            chooseopt = int(raw_input("Choose an option: "))
            if chooseopt == 3:
                clear()
                sys.exit(1)
            elif chooseopt == 1:
                clear()
                additem()
            elif chooseopt == 2:
                clear()
                print "       ---->>>>>>>Selling items<<<<<<<----       "
                print ""
                sellart()
            elif chooseopt <= 0:
                print "You should enter NUMBERS from ONE to THREE."
            elif chooseopt > 3:
                print "You should enter NUMBERS from ONE to THREE."
        except ValueError:
            print "You should enter NUMBERS from ONE to THREE."

def arti():
    """This function adds items to inventory"""
    key = raw_input(">Add item: ")
    global KEYLOW
    KEYLOW = key.lower()
    viewinventory()
    review(KEYLOW)
    if key == "":
        print "Type some data."
        arti()
    elif KEYLOW == "exit":
        clear()
        menu()
=======
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
>>>>>>> b7c16153bb537ef01ca33b467f34b1f8b9581d82

def price():
    """This function adds the items price."""
    try:
        value = float(raw_input(">Add price: "))
        if KEYLOW != "inv":
            ARTICLES[KEYLOW] = value
    except ValueError:
        print "Ingresa correctamente los datos"
        price()


def quantity():
    """This function adds the quantity of items."""
    try:
        global NUMBARTICLES
        NUMBARTICLES = int(raw_input(">Amount of articles: "))
        if KEYLOW != "inv":
            INSTOCK[KEYLOW] = NUMBARTICLES
        if NUMBARTICLES < 0:
            print "Out of Range!"
            quantity()
    except ValueError:
        print "You should enter numbers."
        quantity()

<<<<<<< HEAD

def review(key):
    """Check if there are the same items."""
    sameart = ARTICLES.has_key(key)
    if sameart == True:
        print "     *The article '%s' already exists. " % (KEYLOW)
        questionmodif = raw_input("     *Would you like change the data? y/n ")
        answer = questionmodif.lower()
        if answer == "y" or answer == "yes":
            quantity()
            price()
            print "      Changes Saved!"
            again()
        elif answer == "no" or answer == "n":
            again()
        else:
            print "Enter 'y' to modify data or 'n' to discard changes."
            review(key)
=======
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
>>>>>>> b7c16153bb537ef01ca33b467f34b1f8b9581d82

def again():
    """Esta funcion pregunta si se quieren agregar mas articulos"""
    question = raw_input("**/Do you want to insert another article? y/n ")
    questionlower = question.lower()
    if questionlower == "y" or questionlower == "yes":
        additem()
    elif questionlower == "n" or questionlower == "no" or questionlower == "not":
        clear()
        menu()
    else:
        print "Enter 'y' to add items or 'n' to return to menu."
        again()

<<<<<<< HEAD
def viewinventory():
    """This function displays the inventory."""
    if KEYLOW == "inv":
        if len(ARTICLES) != 0:
            clear()
            klist = ARTICLES.keys()
            print "=================INVENTORY================="
            for item in klist:
                print "Article:", item, " Quantity:", INSTOCK[item], " Price:", ARTICLES[item]
            print ""
            questinvent()
        else:
            print ""
            print "     /-No items in inventory. Please add items."
            additem()

def questinvent():
    """Submenu of the inventory function"""
    print "/Press 'a' to add more items."
    print "/Press 'd' to delete items."
    print "/Press 'm' to go to the main menu."
    inventoryquest = raw_input("What you want to do? ")
    questinvlow = inventoryquest.lower()
    if questinvlow == "a":
        clear()
        additem()
    elif questinvlow == "d" or questinvlow == "del":
        clear()
        print "    >>>>>>>>>>>>>>>DELETE<<<<<<<<<<<<<<<    "
        print "Type the name of the item you want to delete."
        print "Type 'inv' to see the items in the inventory."
        print "Type 'cancel' to return to 'Inventory'"
        delitem()
    elif questinvlow == "m":
        clear()
        menu()
    else:
        print "   ***Invalid data***   "
        questinvent()


def delitem():
    """Deletes inventory items"""
    todelete = raw_input(">")
    lowerdelet = todelete.lower()
    itemexist = ARTICLES.has_key(lowerdelet)
    if itemexist == True:
        del ARTICLES[lowerdelet]
        del INSTOCK[lowerdelet]
        print "      /*/*/*-ITEM DELETED!"
        noitm()
        print ""
        print "Type the name of the item you want to delete."
        print "Type 'inv' to see the items in the inventory."
        print "Type 'cancel' to return to 'Inventory'"
        delitem()
    elif lowerdelet == "inv":
        noitm()
        klist = ARTICLES.keys()
        for item in klist:
            print "  Article:", item, " Quantity:", INSTOCK[item], " Price:", ARTICLES[item]
        print ""
        print "Type the name of the item you want to delete."
        print "Type 'inv' to see the items in the inventory."
        print "Type 'add' to add items"
        print "Type 'cancel' to return to 'Inventory'"
        delitem()
    elif lowerdelet == "add":
        clear()
        additem()
    elif lowerdelet == "cancel":
        viewinventory()
    else:
        print "      /*/*/*-Invalid instruction! The item is not in inventory!"
        print ""
        print "Type the name of the item you want to delete."
        print "Type 'inv' to see the items in the inventory."
        print "Type 'add' to add items"
        print "Type 'cancel' to return to 'Inventory'"
        delitem()

def noitm():
    """Displays a message when there are no items in inventory."""
    artlong = len(INSTOCK)
    if artlong == 0:
        print "      /*/*/*-No items in inventory."
        print "Please add items."
        additem()

def clear():
    """Cleans the data on screen."""
    if os.name == "posix":
        os.system("reset")
    elif os.name == ("nt"):
        os.system("cls")

def additem():
    """Contains functions 'arti', 'price', 'quantity', 'again'."""
    print ""
    print "====================Add to Inventory===================="
    print "Type 'inv' in 'Add item', to see the added items currently."
    print "Type 'exit' in 'Add item' to go to main menu."
    print ""
    arti()
    quantity()
    price()
    again()

def sellart():
    """Main function to sell items."""
    sale = raw_input(" >>Item to Sell: ")
    print ""
    global SALEMINUS
    SALEMINUS = sale.lower()
    if SALEMINUS == "done":
        countingsell(SELLLIST)
        bill()
        newdict()
        revgld()
        revslv()
        billnormal()
    elif SALEMINUS == "gold":
        GOLDSIL.append("gold")
        print "*<Gold card has been added.>*"
        print ""
        sellart()
    elif SALEMINUS == "silver":
        GOLDSIL.append("silver")
        print "*<Silver card has been added.>*"
        print ""
        sellart()
    elif SALEMINUS == "exit":
        deletedata()
        clear()
        menu()
    else:
        existindic(SALEMINUS)

def existindic(vararg):
    """Check the existence of items for sale."""
    itmtrue = ARTICLES.has_key(vararg)
    if itmtrue == True:
        SELLLIST.append(vararg)
        noexist()
        sellart()
    else:
        print "No existe"
        sellart()

def countingsell(counting):
    """Creates a dictionary that saves the items sold."""
    for variable in SELLLIST:
        SELLDIC[variable] = counting.count(variable)


def noexist():
    """Subtract 1 when an item is sold"""
    INSTOCK[SALEMINUS] -= 1


def bill():
    """Generates a copy of the dictionary "articles" with value zero on items that did not sell."""
    artln = len(ARTICLES)
    slln = len(SELLDIC)
    if artln >= slln:
        artst = set(ARTICLES)
        stsell = set(SELLDIC)
        dif = artst - stsell
        global LSTDIF
        LSTDIF = list(dif)
        global ARTCOP
        ARTCOP = ARTICLES.copy()
        for var in ARTCOP:
            if var > 0:
                for var in LSTDIF:
                    ARTCOP[var] = 0

def newdict():
    """Generates a copy of the dictionary "SELLDIC" with zero on items that did not sell."""
    global COPSELL
    COPSELL = SELLDIC.copy()
    stcop = set(ARTCOP)
    stcopsll = set(COPSELL)
    dif = stcop - stcopsll
    lsta = list(dif)
    for var in lsta:
        COPSELL[var] = 0

def revgld():
    """Generates total to pay for the gold card."""
    if "gold" in GOLDSIL:
        total = 0
        grantotal = 0
        for var in ARTCOP:
            total = total + ARTCOP[var] * COPSELL[var]
        total = round(total / 1.05, 2)
        grantotal = round(total *1.12, 2)
        subtotalgld()
        print " ----->>Total: ", grantotal
        print ""
        print "      ///---Payment"
        print ""
        money(grantotal)


def revslv():
    """Generates total to pay for the silver card."""
    if "silver" in GOLDSIL:
        total = 0
        grantotal = 0
        for var in ARTCOP:
            total = total + ARTCOP[var] * COPSELL[var]
        total = round(total / 1.02, 2)
        grantotal = round(total * 1.12, 2)
        subtotalslv()
        print " ----->>Total: ", grantotal
        print ""
        print "      ///---Payment"
        print ""
        money(grantotal)


def billnormal():
    """Generates total to pay in a normal sale."""
    total = 0
    grantotal = 0
    for var in ARTCOP:
        total = total + ARTCOP[var] * COPSELL[var]
    grantotal = round(total * 1.12, 2)
    print ""
    print " ----->>Total: ", grantotal
    subtotal()
    print ""
    print "      ///---Payment"
    print ""
    money(grantotal)

def subtotal():
    """Stores the subtotal of each item sold."""
    for var in COPSELL:
        SUBTOTALDIC[var] = round((ARTCOP[var] * COPSELL[var]) * 1.12, 2)


def subtotalslv():
    """Stores the subtotal of each item sold with silver card."""
    for var in COPSELL:
        SUBTOTALDIC[var] = round(((ARTCOP[var] * COPSELL[var]) / 1.02) * 1.12, 2)

def subtotalgld():
    """Stores the subtotal of each item sold with gold card."""
    for var in COPSELL:
        SUBTOTALDIC[var] = round(((ARTCOP[var] * COPSELL[var]) / 1.05) * 1.12, 2)

def newsell():
    """This function asks the user to make a new sale."""
    print "  //-Type 'new' to sell again."
    print "  //-Type 'exit' to return to the main menu."
    print ""
    what = raw_input("       > What you want to do? ")
    whatmin = what.lower()
    if whatmin == "new":
        deletedata()
        clear()
        print "       ---->>>>>>>Selling items<<<<<<<----       "
        print ""
        sellart()
    elif whatmin == "exit":
        deletedata()
        clear()
        menu()
    else:
        print "           > Invalid data!"
        newsell()

def numtrue(revkey):
    """This function checks if the argument can be converted to float."""
    try:
        float(revkey)
        return True
    except ValueError:
        return False


def money(gran):
    """This function stores the cash to generate the invoice."""
    mon = raw_input("       >Cash: ")
    bol = mon.isalpha()
    condic = numtrue(mon)
    print bol
    if bol == False and mon != "" and condic == True:
        monnum = float(mon)
        if monnum >= 0:
            if monnum >= gran:
                invoice(monnum, gran)
            elif monnum < gran:
                print ""
                print "Not enough money"
                money(gran)
        elif monnum < 0:
            print ""
            print "Invalid data."
            money(gran)
        else:
            print "Invalid data."
            money(gran)
    else:
        print "pera"
        money(gran)


def deletedata():
    """Clears the data stored in lists and dictionaries, for use on a new sale."""
    del SELLLIST[0:]
    del GOLDSIL[0:]
    SELLDIC.clear()


def invoice(efect, total):
    """Invoice with totals, subtotals, cash and change."""
    clear()
    print "  ____________________INVOICE____________________"
    print ""
    for var in COPSELL:
        if COPSELL[var] > 0:
            if SUBTOTALDIC[var] > 0:
                print "    -", str(COPSELL[var]), str(var), ".............."\
                "subtotal: ", str(SUBTOTALDIC[var])
    print ""
    print "       ---------------------------------"
    print "                          ", "Total: ", str(total)
    print "                          ", "Cash:  ", str(efect)
    print "                          ", "Change:", str(efect - total)
    print "     --> Thank you for shopping with us!"
    print ""
    print "       ---------------------------------"
    print ""
    newsell()

clear()
menu()
=======
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
>>>>>>> b7c16153bb537ef01ca33b467f34b1f8b9581d82
