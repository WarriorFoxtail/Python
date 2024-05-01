"""
    CRUD practice
"""

def main_menu():
    #present menu
    #check values
    #return choice
    main()

def check():
    #read file to list
    #if the file isn't there, create an empty customer list
    #return customer list
    print("Check for file")
    main()

def create():
    #create a new entry
    #call save()
    print("Create")

def read():
    #call search()
    #will display the found record
    print("Read")

def search():
    #called by read(), update(), delete()
    #returns record, index
    print("Search")

def update():
    
    print("Update")

def delete():
    print("Delete")

def save():
    #save the file
    print("Save")

def main():
    # present menu and call appropriate functions
    print("Welcome! You can create new email entries")
    print("Change email address, delete entries, or display")
    print("\n")
    print("1. Create a new entry")
    print("2. Display an entry by last name")
    print("3. Update an existing entry.")
    print("4. Remove an entry.")
    print("5. Quit")
    print("\nPlease enter the number of your menu choice: ")

    try:
        choice=int(input("Please enter the number of your selection: "))
        if choice<1 or choice>5:
            print("Whoops! That is not a valid option. Please try again.")
            main()
        if choice==1:
            create()
        elif choice==2:
            read()
        elif choice==3:
            update()
        elif choice==4:
            delete()
        else:
            print("Goodbye!")
    except:
        print("Sorry, that isn't a valiid choice. Please try again.")

main()