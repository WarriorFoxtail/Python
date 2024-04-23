#defines class Person
class Person:
    #Initializer with private variables
    def __init__(self, first_name, last_name, age, address, phone):
        self.__first_name=first_name  #Private variable for first name
        self.__last_name=last_name    #Private variable for last name
        self.__age=age                #Private variable for age
        self.__address=address        #Private variable for address
        self.__phone=phone            #Private variable for phone number

#Get method to get person's info as a formatted string
    def get_info(self):
        return f"Name: {self.__first_name} {self.__last_name}, Age: {self.__age}, Address: {self.__address}, Phone Number: {self.__phone}"
    
    #Getter for first_name
    def get_first_name(self):
        return self.__first_name

    #Getter for last_name
    def get_last_name(self):
        return self.__last_name

    #Getter for age
    def get_age(self):
        return self.__age

    #Getter for address
    def get_address(self):
        return self.__address
    
    #Getter for phone number
    def get_phone(self):
        return self.__phone

    #Setter for first_name
    def set_first_name(self, first_name):
        self.__first_name=first_name

    #Setter for last_name
    def set_last_name(self, last_name):
        self.__last_name=last_name

    #Setter for age
    def set_age(self, age):
        self.__age=age

    #Setter for address
    def set_address(self, address):
        self.__address=address

    #Setter for phone number
    def set_phone(self, phone):
        self.__phone=phone

def main():
    person1=Person("Nitori", "Haruki", "27", "435 Whitefalls Rd.", "587-6228")
    person2=Person("Alira", "Haruki", "25", "726 Embers St.", "279-5395")
    person3=Person("Su Jin", "Fang", "25", "846 Slate Ave.", "835-1849")

    print("\n")
    print(person1.get_info())
    print(person2.get_info())
    print(person3.get_info())
    print("\n")

main()