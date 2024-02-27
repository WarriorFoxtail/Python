#collect age from user
age=int(input("How old are you? "))

#checking if user is old enough to drive
if age>16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive yet.")

#checking if user is old enough to vote
if age>18:
    print("You are old enough to register to vote.")
else:
    print("You are not old enough to register to vote yet.")

#checking if user is old enough to buy alcohol
if age>21:
    print("You can legally buy alcohol.")
else:
    print("You cannot legally buy alcohol yet.")

#checking if user is old enough to qualify for discount
if age>65:
    print("You qualify for the senior discount.")
else:
    print("You do not qualify for the senior discount yet.")