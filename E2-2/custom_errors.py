#defining class
class NotNumericError(Exception):
    #custom exception implementation
    def __init__(self, message="Whoops! That isn't correct. Please try again."):
        self.message=message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

def main():
    try:
        #get user input and validate
        number=int(input("Please enter a number between 0 and 9: "))
        if number>9: #account for if the input value is over 9
            raise NotNumericError()
    except NotNumericError as e:
        #handle invalid input
        print(f"An error occured: {e}")
    except Exception as e:
        print(f"The exception is {e}")
        main()
    else:
        #confirm valid input
        print(f"Thank you for entering {number}")
    finally:
        #indicate end of this iteration
        print("Thank you for playing!")


main()