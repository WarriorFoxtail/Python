#estabilshing the count
count=100

#initializing the while loop
while count>1: #iterates the loop as long as the count is greater than 1
    print(count, "bottles of beer on the wall,")
    print(count, "bottles of beer!")
    print("Take one down, pass it around,")
    count-=1 #decreasing the count as each bottle is removed
    if count>1: #initializing an if loop to change the lyrics to singular in second to last stanza
        print(count, "bottles of beer on the wall!\n")
    elif count==1:
        print(count, "bottle of beer on the wall!\n")
        print(count, "bottle of beer on the wall,")
        print(count, "bottle of beer!")
        print("Take it down, pass it around,")
        print("No more bottles of beer on the wall!")