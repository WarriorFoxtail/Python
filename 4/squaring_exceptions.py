#Simple Python program to calculate the square of a number
def square_number():
    number = input("Enter a number to square: ")
    squared_number = int(number) ** 2
    print(f"The square of {number} is {squared_number}.")

#initializing the try except block
def main():
    try: #testing the function
        square_number()
    except ValueError: #accounting for potential value errors
        print("Whoops! You must input an integer. Please try again.")
        main()

#calling the main function
main()