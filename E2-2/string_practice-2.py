def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string: #iterating through each character in the string
        print(char, end=" ") #displaying each character separated by spaces

    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    minimum=min(example_string) #finding the character with the smallest ascii value
    print("\'"+minimum+"\'") #displaying the character
    #NOTE: THE LOWEST ASCII VALUE CHARACTER IS A SPACE, SO IT MUST BE SURROUNDED BY QUOTES TO SHOW UP IN TERMINAL

    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    print(max(example_string)) #finding and displaying the character with the largest ascii value

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    print(example_string.index("o")) #searches for and displays the index of the first instance of the character

    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    my_list=list(example_string) #converting the string to a list
    print(my_list) #displaying the list

    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    print(example_string.count("o")) #searches for each instance of the specified character and displays the number of ocurrences

main()