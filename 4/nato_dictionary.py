#creating alphabet
alphabet={"A":"Alyssum", "B":"Bluebell", "C":"Carnation", "D":"Daisy", "E":"Eucalyptus", "F":"Foxglove", "G":"Gardenia",
          "H":"Hydrangea", "I":"Iris", "J":"Jasmine", "K":"Kalmia", "L":"Lily", "M":"Marigold", "N":"Narcissus",
          "O":"Orchid", "P":"Peony", "Q":"Quamash", "R":"Rose", "S":"Sunflower", "T":"Tulip", "U":"Ursinia", "V":"Violet",
          "W":"Wisteria", "X":"Xeranthemum", "Y":"Yarrow", "Z":"Zinnia", " ":" ", ".":"."}

#defining the function
def get_word():
    #getting user input
    user_word=input("Please enter a word: ")
    for letter in user_word.upper(): #initializes loop and converts word to upper case
        print(alphabet.get(letter)) #iterates through word, searches for corrosponding keys, and prints the associated value

#calling get_word function
def main():
    get_word()

#calling main
main()