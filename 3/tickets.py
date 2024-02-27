#define the list of available seats
seats=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#setting a value for tracking seats sold
sold="tickets sold"

#displaying the list of available seats
while sold!="done":
    for seat in seats:
        print(seat)

    #prompt user to input what seat was purchased
    sold=int(input("\nPlease input, one at a time, the seat number you would like to purchase: "))
    int(input("Please enter 0 to complete your purchase: "))

    #checking, removing, and updating the list for the input value
    if sold in seats:
        seats.remove(sold)
        print("Thank you for your purchase!")
    elif sold>20:
        print("Oops! That isn't a valid seat number. Please select again.")
    elif sold not in seats:
        print("Oops! That seat has already been purchased. Please select again.")

    
    #checking if all the seats have been sold
    if len(seats)==0:
        print("All seats have been sold!")
        sold="done"