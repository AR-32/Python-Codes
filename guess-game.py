sec_num = 7
guess_count = 2
guess = int(input("enter your guess no.:  "))
while guess_count != 0:
     if guess == sec_num:
       print("You guess it right",end = "")
       break
     else:
       guess_count -= 1
       print("try again")
       guess = int(input("enter again:  "))
if guess_count == 0:
  print("you lose")
