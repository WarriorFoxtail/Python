#creating the list of times for prompt
days=[]
test_times=["Breakfast", "Lunch", "Dinner", "Bedtime"]
for i in range(3):
    sugars=[]
    for time in test_times:
        level=int(input(f"Enter your blood sugar level for {time}: "))
        sugars.append([time, level])

    print(sugars)
    #how to access a single value
    days.append(sugars)
#print(days)
    
for i in range(len(days)):
    print(f"Day {i+1}: ")
    for c in range(4): #4 test times
        print(days[i][c])

#total=0 #accumulator
#for sugar in sugars:
#    total+=sugar[1]

#average=round(total/len(sugars))
#print("Your average blood sugar level is ", average)