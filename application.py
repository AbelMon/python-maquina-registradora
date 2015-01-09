"""This is a cash register program."""
import sys
import os
ARTICLES = {"pera":2.0, "manzana":2.5, "sandia":12, "melon":10.0, "naranja":1.5, "tomate":0.75, "shampoo":19.5, "jabon":7.5}
InStock = {"pera":28, "manzana":37, "sandia":50, "melon":15, "naranja":80, "tomate":60, "shampoo":17, "jabon":20}
selllist = []
goldsil = []
selldic = {}
subtotaldic = {}

def Menu():
    """Main menu"""
    chooseOpt = 0
    print ""
    print "====================Menu===================="
    print "Press 1 if you want to add an item."
    print "Press 2 if you want to sell an item."
    print "Press 3 if you want to exit."
    print ""
    while chooseOpt != 3:
        try:
            chooseOpt = int(raw_input("Choose an option: "))
            if chooseOpt == 3:
                sys.exit(1)
            elif chooseOpt == 1:
                clear()
                AddItem()
            elif chooseOpt == 2:
                clear()
                print "       ---->>>>>>>Selling items<<<<<<<----       "
                sellArt()
            elif chooseOpt <= 0:
                print "You should enter NUMBERS from ONE to THREE."
            elif chooseOpt > 3:
                print "You should enter NUMBERS from ONE to THREE."
        except ValueError:
            print "You should enter NUMBERS from ONE to THREE."

def arti():
    """This function adds items to inventory"""
    key = raw_input(">Add item: ")
    global keylow
    keylow = key.lower()
    viewinventory()
    review(keylow)
    if key == "":
        print "Type some data."
        arti()
    elif keylow == "exit":
        clear()
        Menu()

def price():
    """This function adds the items price."""
    try:
        value = float(raw_input(">Add price: "))
        if keylow != "inv":
            ARTICLES[keylow] = value
    except:
        print "Ingresa correctamente los datos"
        price()


def quantity():
    """This function adds the quantity of items."""
    try:
        global numbarticles
        numbarticles = int(raw_input(">Amount of articles: "))
        if keylow != "inv":
            InStock[keylow] = numbarticles
        if numbarticles < 0:
            print "Out of Range!"
            quantity()
    except:
        print "You should enter numbers."
        quantity()


def review(key):
    """Check if there are the same items."""
    sameArt = ARTICLES.has_key(key)
    if sameArt == True:
        print "     *The article '%s' already exists. " % (keylow)
        QuestionModif = raw_input("     *Would you like change the data? y/n ")
        answer = QuestionModif.lower()
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

def again():
    """Esta funcion pregunta si se quieren agregar mas articulos"""
    question = raw_input("**/Do you want to insert another article? y/n ")
    questionlower = question.lower()
    if questionlower == "y" or questionlower == "yes":
        AddItem()
    elif questionlower == "n" or questionlower == "no" or questionlower == "not":
        clear()
        Menu()
    else:
        print "Enter 'y' to add items or 'n' to return to Menu."
        again()

def viewinventory():
    """This function displays the inventory."""
    if keylow == "inv":
        if len(ARTICLES) != 0:
            clear()
            Klist = ARTICLES.keys()
            print "=================INVENTORY================="
            for item in Klist:
                print "Article:", item, " Quantity:", InStock[item], " Price:", ARTICLES[item]
            print ""
            questinvent()
        else:
            print ""
            print "     /-No items in inventory. Please add items."
            AddItem()

def questinvent():
    """Submenu of the inventory function"""
    print "/Press 'a' to add more items."
    print "/Press 'd' to delete items."
    print "/Press 'm' to go to the main Menu."
    inventoryquest = raw_input("What you want to do? ")
    questinvlow = inventoryquest.lower()
    if inventoryquest == "a":
        clear()
        AddItem()
    elif inventoryquest == "d" or inventoryquest == "del":
        clear()
        print "    >>>>>>>>>>>>>>>DELETE<<<<<<<<<<<<<<<    "
        print "Type the name of the item you want to delete."
        print "Type 'inv' to see the items in the inventory."
        print "Type 'cancel' to return to 'Inventory'"
        delitem()
    elif inventoryquest == "m":
        clear()
        Menu()
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
        del InStock[lowerdelet]
        print "      /*/*/*-ITEM DELETED!"
        noitm()
        print ""
        print "Type the name of the item you want to delete."
        print "Type 'inv' to see the items in the inventory."
        print "Type 'cancel' to return to 'Inventory'"
        delitem()
    elif lowerdelet == "inv":
        noitm()
        Klist = ARTICLES.keys()
        for item in Klist:
            print "  Article:", item, " Quantity:", InStock[item], " Price:", ARTICLES[item]
        print ""
        print "Type the name of the item you want to delete."
        print "Type 'inv' to see the items in the inventory."
        print "Type 'add' to add items"
        print "Type 'cancel' to return to 'Inventory'"
        delitem()
    elif lowerdelet == "add":
        clear()
        AddItem()
    elif lowerdelet == "cancel":
        keylow = "inv"
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
    artlong = len(InStock)
    if artlong == 0:
        print "      /*/*/*-No items in inventory."
        print "Please add items."
        AddItem()

def clear():
    """Cleans the data on screen."""
    if os.name == "posix":
        os.system("reset")
    elif os.name == ("nt"):
        os.system("cls")

def AddItem():
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

def sellArt():
    """Main function to sell items."""
    sale = raw_input(" >>Item to Sell: ")
    global saleminus
    saleminus = sale.lower()
    if saleminus == "done":
        countingsell(selllist)
        bill()
        newdict()
        revgld()
        revslv()
        billnormal()
    elif saleminus == "gold":
        goldsil.append("gold")
        print "gold card"
        sellArt()
    elif saleminus == "silver":
        goldsil.append("silver")
        print "silver card"
        sellArt()
    else:
        existindic(saleminus)

def existindic(x):
    """Check the existence of items for sale."""
    itmtrue = ARTICLES.has_key(x)
    if itmtrue == True:
        selllist.append(x)
        noexist()
        sellArt()
    else:
        print "No existe"
        sellArt()

def countingsell(y):
    """Creates a dictionary that saves the items sold."""
    for variable in selllist:
        selldic[variable] = y.count(variable)


def noexist():
    """Subtract 1 when an item is sold"""
    InStock[saleminus] -= 1


def bill():
    artln = len(ARTICLES)
    slln = len(selldic)
    if artln >= slln:
        artst = set(ARTICLES)
        stsell = set(selldic)
        dif = artst - stsell
        global lstdif
        lstdif = list(dif)
        global artcop
        artcop = ARTICLES.copy()
        for var in artcop:
            if var > 0:
                for var in lstdif:
                    artcop[var] = 0

def newdict():
    global copSell
    copSell = selldic.copy()
    stcop = set(artcop)
    stcopsll = set(copSell)
    dif = stcop - stcopsll
    lsta = list(dif)
    for var in lsta:
        copSell[var] = 0

def revgld():
    if "gold" in goldsil:
        total = 0
        grantotal = 0
        for var in artcop:
            total = total + artcop[var] * copSell[var]
        total = round(total / 1.05, 2)
        grantotal = round(total *1.12, 2)
        subtotalgld()


def revslv():
    if "silver" in goldsil:
        total = 0
        grantotal = 0
        for var in artcop:
            total = total + artcop[var] * copSell[var]
        total = round(total / 1.02, 2)
        grantotal = round(total * 1.12, 2)
        subtotalslv()
        print total
        print grantotal


def billnormal():
    total = 0
    grantotal = 0
    for var in artcop:
        total = total + artcop[var] * copSell[var]
    grantotal = round(total * 1.12, 2)
    print ""
    print " ----->>Total: ", grantotal
    subtotal()
    print ""
    print "    ///---Payment"
    money(grantotal)
    clear()


def subtotal():
    for var in copSell:
        subtotaldic[var] = round((artcop[var] * copSell[var]) * 1.12, 2)


def subtotalslv():
    for var in copSell:
        subtotaldic[var] = round(((artcop[var] * copSell[var]) / 1.02) * 1.12, 2)

def subtotalgld():
    for var in copSell:
        subtotaldic[var] = round(((artcop[var] * copSell[var]) / 1.05) * 1.12, 2)
    print subtotaldic
    print "yolo"


def money(gran):
    mon = float(raw_input(" >>>Cash: "))
    if mon > 0:
        if mon >= gran:
            invoice()
        elif mon < gran:
            print ""
            print "Not enough money"
            money(gran)

def solvent():
	print "s"

def invoice():
    print "____________________INVOICE____________________"
    print ""
    print "----------Items----------"




Menu()