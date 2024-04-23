#defining the class
class Pet:
    #initializing the attributes
    def __init__(self, name, kind, breed):
        self.name=name
        self.kind=kind
        self.breed=breed

    #getter methods for name, kind, and breed
    def get_name(self):
        return self.name
    
    def get_kind(self):
        return self.kind
        
    def get_breed(self):
        return self.breed
    
    #setter methods for name, kind, and breed
    def set_name(self, value):
        self.name=value

    def set_kind(self, value):
        self.kind=value

    def set_breed(self, value):
        self.breed=value

    #method to display pet detils
    def print_details(self):
        print("Pet Details:", vars(self))

#defining main
def main():
    pet1=Pet("Fang", "Dog", "Tamaskan Dog") #defining attributes for pet 1
    pet2=Pet("Poppy", "Rabbit", "Holland Lop") #defining attributes for pet 2
    pet3=Pet("Echo", "Bird", "Cockatiel") #defining attributes for pet 3

    print()
    pet1.print_details() #printing the details of pet 1
    pet2.print_details() #printing the details of pet 2
    pet3.print_details() #printing the details of pet 3

    print(f"\nPet 2 Kind:", getattr(pet2, "kind")) #using the getattr() function to print the "kind" attribute of pet 2
    print()

#calling main
main()