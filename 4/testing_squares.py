def square_number(userInput):
    number = int(userInput) ** 2
    return number

def printNumber(userInput, squared):
    print(f"The square of {userInput} is {squared}.")

def main():
    userInput = input("Enter a number to square: ")
    squared = square_number(userInput)
    printNumber(userInput, squared)

main()