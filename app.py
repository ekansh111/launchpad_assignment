from models import Room, Activity, User, Food, resortdb

resortdb.connect()


def signup():
	username = input("Create username: ")
	password = input("Create Password: ")

	exists = len(User.select().where(User.username == username))

	if not exists: 
		User.create(username=username, password=password)
		print("User created successfully!\n\n")
	else:
		print("Username already exists. Please try new username.")

def login():
	username = input("Enter Username: ")
	password = input("Enter Password: ")

	# user = User.select().where(User.username == username)
	# print(user)
	try:
		user = User.get(User.username==username, User.password==password)

	except:
		print("Invalid Password.\n\n")

	return user



def book_room(user):

	choice = int(input("Choose Type of Room:\n1. Single Room-5,000\n2. Deluxe-10,000\n3. Luxury-15,000\n4. Guest House-25,000"))

	if choice == 1:
		dur = input("enter the duration of your stay")
		Room.create(owner=user,rname='single',cost=5000,duration=dur)	
	elif choice == 2:
		dur = input("enter the duration of your stay")
		Room.create(owner=user,rname='deluxe',cost=10000,duration=dur)		
	elif choice == 3:
		dur = input("enter the duration of your stay")
		Room.create(owner=user,rname='luxury',cost=15000,duration=dur)
				
	elif choice == 4:
		dur = input("enter the duration of your stay")
		Room.create(owner=user,rname='ghouse',cost=25000,duration=dur)
	else:
		print("invalid choice")



def order_food(user):

	choice = int(input("Choose your Food:\n1. breakfast\n2. lunch\n3. dinner"))

	if choice == 1:

		Food.create(owner=user, ftype='bk', cost=500)	
	elif choice == 2:
		Food.create(owner=user, ftype='lnch',cost=1000)		
	elif choice == 3:
		Food.create(owner=user, ftype='dnr', cost=1500)
	else:
		print("invalid choice")

def book_activity(user):
	choice = int(input("Choose Activity:\n1. Swimming\n2. Paragliding\n3. ScubaDiving"))

	print(user)
	if choice == 1:
		activity = Activity.create(owner=user,aname='swmm',cost=500)
		activity.save
	elif choice == 2:
		Activity.create(owner=user,aname='pgl',cost=1000)		
	elif choice == 3:
		Activity.create(owner=user,aname='scb',cost=1500)
				
	else:
		print("invalid choice")

def tot_cost(user):
	sum1 = 0
	#print(user)
	try:
		s1 = Food.get(Food.owner_id == user).cost
		if s1 is not None :
			sum1= s1 + sum1
			print("the total cost of food is")
			print(s1)
	except:
		pass
	try :
		s2 = Activity.get(Activity.owner_id == user).cost
		if s2 is not None :
			sum1 = s2 + sum1
			print("Cost of your activity is")
			print(s2)
	except :
		pass




	try:
		s3 = Room.get(Room.owner_id == user).cost
		if s3 is not None :
			sum1 = s3 + sum1
			print("Cost of your Room is")
			print(s3)
		
	except:
		pass


	print(sum1)