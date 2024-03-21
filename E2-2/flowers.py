#defining main
def main():
    seed=True #creates a variable for while loop
    flowers=[] #creating an empty list
    print("Welcome! Please enter 'Done' when finished.") #initial greeting message
    
    #initializing the while loop
    while seed:
        flower=input("Please enter a flower name: ") #getting user input
        if flower=="Done": #checks for "Done" input then breaks the loop
            break
        flowers.append(flower) #adds each flower name to list
    
    #sorts the list of flowers
    sorted=flowers.sort()
    #displaying the sorted list and its number starting with 1
    print((sorted.index()+1)+". "+sorted) 

#calling main
main()