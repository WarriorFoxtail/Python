# collecting names from user
name_1 = input("Please enter a name: ")
name_2 = input("Please enter a second name: ")
name_3 = input("Please enter a third name: ")
name_4 = input("Please enter a fourth name: ")
name_5 = input("Please enter a fifth name: ")

# generating initial list of names
names = [name_1, name_2, name_3, name_4, name_5]

# initialize swapping
swapped = True

# loop until there's no more swaps
while swapped:
    swapped = False # resets flag at the start of each iteration
    for i in range(len(names) - 1):
        # compares adjacent elements
        if names[i] > names[i + 1]:
            swapped = True # swap is needed
            # swaps elements
            names[i], names[i + 1] = names[i + 1], names[i]

# print sorted list
print(names)

# reverse the list
names.reverse()

# print reversed list
print(names)
