def main():
    emoji={"duck":"🐥", "python":"🐍", "monkey":"🐵", "dog":"🐶", "cat":"🐱", "fish":"🐟", "bird":"🐦"}
    print(emoji)

    #two methods for accessing items by key
    print(emoji["duck"])
    animal=emoji.get("cat")
    print(animal)

    #getting keys
    print(emoji.keys())

    #getting values
    print('\n\n')
    print(emoji.values())

    #getting key-value pair
    print('\n\n')
    print(emoji.items())

    if "duck" in emoji:
        print(emoji["duck"])

    #changing the value for an existing key
    emoji["duck"]="🦆"
    print(emoji["duck"])

    #adding a new key-value
    emoji.update({"raccoon":"🦝"})

    #removing a key-value
    emoji.pop("cat")
    print(emoji)
    del emoji["duck"]
    print(emoji)

    #looping a dictionary
    for x in emoji: #prints values
        print(emoji[x])

    for x in emoji: #prints keys
        print(x)

main()