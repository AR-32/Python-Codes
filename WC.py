print("Welcome !!!\nTo weight conversion app")
print("NOTE:-\n\t1. Write everything in small letters\n\t2. You can convert kg to pounds, tons, quintal")
unit = input("In which unit you want to convert your weight:  ")
weight = int(input("Enter weight in kg:  "))
if unit == "pounds" or unit == "pound":
    weight = weight * 2.204623
    print("Weight is converted from kg to pounds:  ",weight,end="lb")
elif unit == "tons" or unit == "ton":
    weight = weight * 0.001
    print("Weight is converted from kg to tons:  ",weight,end="t")
elif unit == "quintals" or unit == "quintal":
    weight = weight * 0.01
    print("Weight is converted from kg to quintal:  ",weight,end="q")
else:
    print("You entered wrong")