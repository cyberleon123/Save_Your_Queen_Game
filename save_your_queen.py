from sys import exit

def haveli():
	print("So Finally, You Reach To The Haveli.")
	print("In A Room You Saw Your Queen Is Banded Up With Ropes.")
	print("Ah Shit!, The Goon \"Thanos\" Is Entered In The Room ")
	print("Now You Have To Fight With Him")
	print("There Is A Gun On The Table.")
	print("Now You Have Two Options")
	print("1. Take The Gun And Shoot \"Thanos\"")
	print("2. Run Away")
	action=input(">>")
	if action=="1":
		print("Good Job!, Thanos Died")
		print("You Save Your Queen")
		print("Now Your Queen Is Kissing You....")

	elif action=="2":
		print("You Foolish Coward, Your Queen Will Will Never Marry You")
		exit(0)
	else:
		print("Wrong Input, Come Back Later.")
		exit(0)

def crocodile():
	print("Good!, But Thers Is A Lots Of Crocodile In The River.")
	print("What Should You Do?")
	print("1. Before Entering Into River Throws Stones On Crocs.")
	print("2. Enter Into The River And Swim Fast.")
	print("3. Quit")
	croc=input(">>")
	if croc=="1":
		print("Great!, The Crocodiles Ran Away.")
		print("Now You Can Move Forward.")
		print("Now You Are Moving Forward And Saw A Haveli In a Villge")
		print("It's Look Mysterious")
		print("I Think Your Queen Is There.")
		print("Do You Want To Go There:")
		a=input(">>")
		if a=="yes":
			haveli()
		else:
			print("You Will Never Find Your Queen")
			exit(0)
	elif croc=="2":
		print("The Crocodiles Ate You, RIP...")
		exit(0)
	else:
		print("Wrong Input, Come Back Later.") 

def one():
	print("This Way Is Full Of Darkness")
	print("You Have To Go Through A Large Jungle")
	print("So Many Wild Animals Are Also Here. Be Aware")
	print("OMG!, There Is A Tiger In Front Of You What Should You Do?")
	print("You have 3 Options:")
	print("1. Scream Louder And Try To Run Tiger Away.")
	print("2. Being Steady Till The Tiger Goes Away.")
	print("3. Run")
	choice=input(">>")
	if choice == "1":
		print("Tiger Gets Angry And Ate You")
		print("May Your Soul Rest In Peace....")
		exit(0)
	elif choice == "2":
		print("The Tiger Is Gone Away After Some Time.")
		print("Now you Can Go Forward.")
		print("Now, You Are Moving Forward And Came In A Village")
		print("Where Is A Mysterious Haveli")
		print("I Think Your Queen Is There.")
		print("Do You Want To Go There:")
		choose=input(">>")
		if choose=="yes":
			haveli()
		else:
			print("You Will Never Find Your Queen")
			exit(0)
	elif choice=="3":
		print("The Tiger Catch You And Ate You, RIP!...")
		exit(0)
	else:
		print("Wrong Input, Try Again!")
		exit(0)

def two():
	print("There Is A Big River In Front Of You")
	print("Do You Know Swimming:")
	ask=input(">>")
	if ask=="yes":
		crocodile()
	elif ask=="no":
		print("You Better Go Home.")
		exit(0)
	else:
		print("Wrong Input, Come Back Later")

def three():
	print("You Are Going Good, But Suddenly A Anaconda Comes In Your Way And Bites You.")
	print("You Died!, RIP...")
	exit(0)

def start():
	print("There Is A 3 Ways To Reach To Your Queen")
	print("She Is Kidnapped By A Goon Whose Name Is \"Thanos\"")
	print("But You Have To Choose Only One Way To Reach To Your Queen")
	print("Choose a Number Between 1 To 3")
	next = input(">>")
	if next=="1":
		one()
	elif next=="2":
		two()
	elif next=="3":
		three()
	else:
		print("Wrong Choice, Come Again")
		exit(0)
start()

		
