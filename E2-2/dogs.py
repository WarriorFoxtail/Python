"""
    Creating and using a Dog SuperClass
    and a herding sub class
    and making objects
"""

class Dog: #Dog is a Super class of the Herding_Dog class
    def __init__(self, color, coat, size, name):
        self.color=color
        self.coat=coat
        self.size=size
        self.name=name

    def bark(self):
        print("Woof!")

    def happy(self):
        print("Wag wag")

    def __str__(self):
        return f"Dog Details: Color: {self.color}, Coat: {self.coat}, Size: {self.size}, Name: {self.name}\n"
    
class HerdingDog(Dog):
    def __init__(self, color, coat, size, name, favorite_toy):
        super().__init__(color, coat, size, name)
        self.favorite_toy=favorite_toy

    def herding(self):
        print("Run! I want to play chase!")
    
    def __str__(self):
        return super().__str__()+" "+self.favorite_toy+", with herding skills.\n"

def main():
    gilly=Dog("Black and Brown", "Short", "Large", "Gilly")
    print("Gilly")
    gilly.bark()
    gilly.happy()
    print(gilly)

    bessie=HerdingDog("Black and White", "Long", "Medium", "Bessie", "Tug Rope")
    print("Bessie")
    bessie.herding()
    print(bessie)

main()