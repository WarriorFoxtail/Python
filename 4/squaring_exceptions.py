#Simple Python program to calculate the square of a number
def square_number():
    number = input("Enter a number to square: ")
    squared_number = int(number) ** 2
    print(f"The square of {number} is {squared_number}.")

try:
    square_number()
except ValueError:
    print("Whoops! You must input an integer. Please try again.")
    