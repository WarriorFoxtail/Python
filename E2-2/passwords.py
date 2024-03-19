"""
Set up your program in a main() function
Create a Python program that asks the user to input a password.
Ensure the password meets the following criteria:
Between 8 to 20 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Includes at least one number.
Includes at least one symbol from the set: !@#$%&*.
Use a while loop to keep asking for the password until all criteria are met.
Once a valid password is entered, prompt the user to enter it again for confirmation.
Use try-except blocks to handle any errors or exceptions that occur.
If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.
"""

def main():
    valid=False #changes to true if all conditions are met
    while not valid:
        valid=True #will change to false if ANY requirements are not met
        print("""Password Requirements:\n
              Between 8 to 20 characters.\n
              Contains at least one uppercase letter.\n
              Contains at least one lowercase letter.\n
              Includes at least one number.\n
              Includes at least one special character from the set: !@#$%&*\n""")
        
        password=input("Please enter a password that meets the criteria above: ")

        #checking the length
        length=len(password)
        if 7<length<21: #continues to next step if password is correct length
            continue
        elif length<8: #if password is too short
            valid=False
            print("Whoops! That password isn't long enough. Please try again.")
        elif length>20: #if password is too long
            valid=False
            print("Whoops! That password is too long. Please try again.")

        #checking for uppercase letters
        is_upper=False #changes to true if found
        #for loop to iterate through input to find uppercase character
        for char in password:
            if char.upper==True:
                is_upper==True
                continue
        if is_upper==False: #for if a lowercase letter isn't found
            valid==False
            print("Sorry! You must include an uppercase letter.")

        #checking for lowercase letters
        is_lower=False #changes to true if found
        #for loop to iterate through input to find lowercase character
        for char in password:
            if char.lower==True:
                is_lower==True
                continue
        if is_upper==False: #for if an uppercase letter isn't found
            valid==False
            print("Sorry! You must include a lowercase letter.")

        #checking for numbers
        has_number=False #will change if a number is found
        number=['!', '@', '#', '$', '%', '&', '*'] #creating a list of number options
        for n in number:
            for cha in password:
                if n==cha:
                    has_number==True
                    continue
        if has_number==False: #for if there isn't a number in the password
            valid=False
            print("Sorry! You must include a number.")
        
        #checking for symbols
        has_symbol=False #will change if a symbol is found
        symbol=['!', '@', '#', '$', '%', '&', '*'] #creating a list of symbols options
        for s in symbol:
            for c in password:
                if s==c:
                    has_symbol==True
                    continue
        if has_symbol==False: #for if there isn't a symbol in the password
            valid=False
            print("Sorry! You must include a symbol.")

    if valid==True:
        confirmed=input("Please re-enter your password to confirm: ")
    if confirmed==password:
        print("Your password is set!")
    else:
        print("Sorry! Your passwords don't match.")

main()