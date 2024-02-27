#estabilshing the count
count=100

#initializing the while loop
while count<100:
    print(count, "bottles of beer on the wall")
    print(count, "bottles of beer")
    print("Take one down, pass it around")
    count+=1 #changing the count as ech bottle is removed
    print(count, "bottles of beer on the wall")

#changing the words to match the single remaining bottle
if count<2:
    print(count, "bottle of beer on the wall")
    print(count, "bottle of beer")
    print("Take it down, pass it around")
    print("No more bottles of beer on the wall")