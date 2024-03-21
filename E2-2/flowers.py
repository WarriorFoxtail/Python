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
    flowers.sort()
    #for loop to iterate through each flower in the sorted list
    for plant in flowers:
        print(f"{flowers.index(plant)+1}. {plant}") #adjusts index number to start at 1 then displays each flower on a new line

    #getting user input to search for a specific flower
    search=input("Please enter the name of the flower you wish to search for: ")
    #if statement to check if the input flower is in the list
    while search in flowers:
        print(f"Yes! It looks like {search} is part of this list.") #if the searched flower is in the list
        number=int(input("Please enter the number of the flower you wish to search for: "))
        try:
            number==flowers.index(plant)+1
        except ValueError:
            print("The value must be an integer.")
        

    else:
        print(f"Sorry! It looks like {search} is not part of this list. Please try again.") #if the searched flower is not in the list
        search=input("Please enter the name of the flower you wish to search for: ") #asks for input again

#calling main
main()