#creating the lists; days for days of the week and steps for the steps taken each day
days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps=[]

#initializing loop to get user input for steps
total=0
for day in days:
    steps_taken=int(input(f"How many steps did you take on {day}? "))
    steps.append(steps_taken)
    total+=steps_taken

index=0
for day in days:
    print(f"On {day} you took {steps[index]}")
    index+=1

average=total/len(steps)
print(f"You walked an average of {average:.1f} steps per day.")