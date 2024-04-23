class Pet:
    #Class variable
    vet_name = "Paws & Claws Veternary"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name=owner_first_name
        self.__owner_last_name=owner_last_name
        self.__pet_id=pet_id
        self.__pet_name=pet_name
        self.__pet_type=pet_type

    #Getters for owner_first_name, owner_last_name, pet_id, pet_name, pet_type
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
        
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type

    #Setters for owner_first_name, owner_last_name, pet_id, pet_name, pet_type
    def set_owner_first_name(self, value):
        self.__owner_first_name=value

    def set_owner_last_name(self, value):
        self.__owner_last_name=value

    def set_pet_id(self, value):
        self.__pet_id=value
    
    def set_pet_name(self, value):
        self.__pet_name=value

    def set_pet_type(self, value):
        self.__pet_type=value

    #creates a method to print owner info
    def display_pet_info(self):
        print("Owner Details: ", vars(self))

    def get_info(self):
        print("Owner: "+self.__owner_first_name+" "+self.__owner_last_name)
        print("Pet Name: "+self.__pet_name)
        print("Pet ID: "+self.__pet_id)
        print("Pet Type: "+self.__pet_type+"\n")
    
def check_property(object, attribute):
    print(hasattr(object, attribute))

def main():
    pet1=Pet("Umiko", "Wolfe", "26490", "Poppy", "Rabbit")
    pet2=Pet("Alira", "Haruki", "48792", "Kuro", "Wolf-dog")
    pet3=Pet("Su Jin", "Fang", "53953", "Mocha", "Cat")

    print("\n")
    pet1.get_info()
    pet2.get_info()
    pet3.get_info()

    check_property(pet1, "owner_first_name")
    check_property(pet1, "vet_name")


main()