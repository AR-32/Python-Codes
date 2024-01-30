print("Welcome to car game !!!")
while (1):
    user = input("What to do:  ")
    if user == "start":
        print("Car started.....")
    elif user == "gear 1":
        print("Shifted to gear 1\nYour speed increases to 10 km/h.....")
    elif user == "gear 2":
        print("Shifted to gear 2\nYour speed increases to 25 km/h.....")
    elif user == "gear 3":
        print("Shifted to gear 3\nYour speed increases to 40 km/h.....")
    elif user == "gear 4":
        print("Shifted to gear 4\nYour speed increases to 65 km/h.....")
    elif user == "gear 5":
        print("Shifted to gear 5\nYour speed increases to 100 km/h.....")
    elif user == "gear 6":
        print("Shifted to gear 6\nYour speed increases to 120 km/h.....\nreached to max speed")
    elif user == "break":
        print("You applied break.....\nspeed decreases.....shift gear accordingly")
    elif user == "emergency_break":
        print("Car stopped.....shift to gear 1....")
    elif user == "help":
        print("Team is on the way for help.....")
    elif user == "quit":
        print("Car stopped....engine turned off....Game over....")
        break
    else:
        print("Invalid")