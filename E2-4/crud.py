"""
    CRUD practice
"""

def main_menu():
    #present menu
    try:
        print("\nMain Menu - Customer Directory")
        print("1. Create new entry")
        print("2. Read and display by name")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Quit")
        #check values
        choice=int(input("Please enter the number of your selection: "))
        if choice < 0 or choice > 5:
            print("Oops! That number is out of range. Please try again.")
            main_menu()
        else:
            return choice #return choice
    except ValueError:
        print("Oops! That is not a valid number. Please try again.")
        main_menu()
    except Exception as e:
        print(f"MAIN MENU: {e}")
    main()

def check():
    #read file to list
    #if the file isn't there, create an empty customer list
    #return customer list
    try:
        file=open("customer_directory.txt", "r")
        curr_customer=file.readlines()
        for line in curr_customer: #for loop for test purposes
            print(line)
        file.close()
        return curr_customer
    except FileNotFoundError:
        print("That file does not exist. We will create a new file for you!")
        curr_customer=[]
        return curr_customer
    except Exception as e:
        print(f"CHECK: {e}")
    main()

#save need the parameter of current Users (str Array)
#array will be saved to the file, file will override all customers in customer, to re save ALL 
#Array = list, collection of the users in a list 
#open file in write mode, write then close
def save(current_customer): #save will save the CURR_CUSTOMER from param
    #save the file
    #save does not need to preform advanced CHECK before saving, as check should *ALWAYS* be called before using CHECK, otherwise issues 
    #check before create, update, and all remaining crud operations
    #open file to save
    try:
        # open in WRITE mode, for saving to file 
        to_save_file=open("customer_directory.txt", "w")
        #for loop to iterate through list of customers and write them to the .txt
        for record in current_customer:
            print("Saved line to record: ", record) #checking the saved record
            #use to save the record to the file
            to_save_file.write(record)
        #all customers written to file
        print("Finnished saving customers", current_customer)
        to_save_file.close()
    except IOError:
        print("SAVE: Error occured during save file operation, IOError")
    main()

def create():
    #create a new entry
    #call save()
    print("Create")
    try:
        customers=check()
        print("\nPlease enter the customer's information: ")
        first_name=input("First name: ")
        last_name=input("Last Name: ")
        phone=input("Phone Number: ")
        email=input("Email Address: ")
        entry=f"{first_name}, {last_name}, {phone}, {email}\n"
        customers.append(entry)
        #debug loop
        for line in customers:
            print(line)
        #implementing save customers after debug loop
        save(customers)
    except Exception as e:
        print(f"CREATE: {e}")
    main()

def read():
    #call search()
    #will display the found record and index
    print("Read")
    try:
        found_me, found_index=search()
        print(f"System Found Customer {found_me} at index {found_index}")
    except Exception as e:
        print(f"READ: {e}")
    main()

def search():
    #called by read(), update(), delete()
    #returns both the record and the index
    #try/except statement to check for customer entries and retrieving all entered customers
    try:
        #calling check()
        current_customers=check()
        find_me=input("Enter a name or part of a name to search for a specific customer: ")
        #for loop to check each customer entry for given parameter
        for cust in current_customers:
            print(f"searching customers: {cust}")
            if find_me in cust:
                print("Customer Found!\n")
                #if customer is found, return the entry index
                customer_index=current_customers.index(cust)
                return cust, customer_index #return both record and index
            else:
                print("Customer not found. Please try again.")
    except Exception as e:
        print(f"SEARCH: {e}")
    main()

def update():
    #output.split
    print("Update")
    
    main()

def delete():
    print("Delete")
    main()

def main():
    # present menu and call appropriate functions
    print("Welcome! You can create new email entries")
    print("Change email address, delete entries, or display")
    choice=main_menu()
    try:
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
    except Exception as e:
        print(f"Main: {e}")

main()