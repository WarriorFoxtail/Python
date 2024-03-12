#defining main
def main():
    #getting user input
    user_input=input("Enter a character: ")
    #checking that the input is one character
    while len(user_input) != 1: #loop will iterate until a single character is entered
        print("Please enter exactly one character.")
        user_input=input("Enter a character: ")
    
    #convering to ascii value
    ascii_value=ord(user_input)

    #displaying the results
    print(f"The ASCII value of {user_input} is {ascii_value}.")

main()