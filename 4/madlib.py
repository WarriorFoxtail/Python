def madlib(person, size, animal, color, noun):
    print(f"{person} had a {size} {animal} ")
    print(f"Whose fleece was {color} as {noun}")

def get_info():
    person=input("Please enter the name of a person: ")
    size=input("Please enter a descriptive word for size: ")
    animal=input("Please enter a kind of animal: ")
    color=input("Please enter a color: ")
    noun=input("Please enter a noun: ")
    return person, size, animal, color, noun

def main():
    person, size, animal, color, noun=get_info()
    madlib(person, size, animal, color, noun)

main()
