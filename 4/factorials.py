#defining the function
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
    
#defining the main function
def main():
    #getting user input for integer
    n=int(input("Please enter a positive integer: "))
    result=factorial(n) #calculating results
    print(f"The factorial of {n} is {result}.")

#calling main
main()