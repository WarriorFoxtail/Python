import random
# Working with modules, random and math


def game(win):
    # getting input, checking for Value Errors, and initializing loop
    try:
        guess = int(input("Please enter a number between 1 and 100: "))
        distance = win-guess
        abs_distance = abs(distance)
        if guess == win:
            print("You guessed the correct number! You're on fire!")
            return
        elif abs_distance < 5:
            print("Hot")
        elif abs_distance < 15:
            print("Warmer")
        elif abs_distance < 25:
            print("Cooler")
        else:
            print("Cold")
        game(win)

    except:
        print("Whoops! That isn't a valid value. Please enter an integer.")
        game(win)


def main():
    # testing random modules
    win = random.randint(1, 100)
    game(win)


main()
