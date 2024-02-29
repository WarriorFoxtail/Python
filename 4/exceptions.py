def main():
    try:
        print(10/0)

    except ZeroDivisionError:
        print("You cannot divide by 0")
    except:
        print("Sorry! That won't work!")

main()