from app import *
user = None
while True:
	print("-"*80)
	print("                            Welcome to Sia Resorts!\n                       Looking for a luxurious Vacation?\n                           We know what you truely love!\n ")
	print("-"*80)


	ch = input("                             What would you like to do?\n1.Login\n2.Signup\nGet Accomodation now! \n -->")

	if ch == "1":

		user = login()
		print(type(user))
		if user is not None:
			def che():
				choice = input("How can we help you?\n1.Room Booking\n2.Food\n3.Activity\n4.CurrentBilling")
				
				if choice == "1":
					book_room(user)
					che()
				elif choice == "2":
					order_food(user)
					che()
				elif choice == "3":
					book_activity(user)
					che()
				elif choice == "4":
					tot_cost(user)	
				'''else:
					continue'''
			che()		
		else:
			print("Credentials do not match. Or Create New Account.")

	elif ch == "2":
		signup()

	else: 
		break