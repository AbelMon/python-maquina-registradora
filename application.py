"""This is a cash register program."""
articles={}
def addItem():
	key=raw_input("Add item: ")   
	value=float(raw_input("Add price: "))
	articles[key]=value

	question=raw_input("Do you want to insert another article y/n or to write the bill estender -Done-:?")


	if question =="Done":

		iva =(value*0.12)
		total = value+iva
			
		print "Total to pay:" , total
		pass
		cash = input("cash:  ")
		
		change = cash - total

		print "   "
		print "     YOUR BILL"
                print "   "
		print ("___Articles:___")
		for i in articles:

			print i
		print ("________________")
		print ("total     %.2f\t")%total
		print ("iva       %.2f\t")%iva
		print ("cash      %.2f\t")%cash
		print ("________________")
		print ("change"),change
		print "Thanks for your purchase:::"
		print "   "
		print "   "
		print "   "

	if question=="y":

		addItem()


	else:
	
		menu()
	print articles

def sellArt(): 
	print "olakase"

def menu():       
	chooseOpt=0
	while chooseOpt!=3:
		print "Press 1 if you want to add an item."
		print "Press 2 if you want to sell an item."
		print "Press 3 if you want to exit."
		chooseOpt=int(raw_input("Choose an option: "))
		if chooseOpt==1:
			addItem()
		elif chooseOpt==2:
			sellArt()

menu()
