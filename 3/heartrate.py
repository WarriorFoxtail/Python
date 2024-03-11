#collect heart rates
time_slots=["Morning", "Midday", "Afternoon", "Evening"]
heart_rates=[]

#generating loop to collect heart rate data
for time in time_slots:
    pulse=int(input(f"Please enter your heartrate, in BPM, for {time}: "))
    heart_rates.append([time, pulse])

#displaying the list of heart rates
print(heart_rates)

#accumlating the total
total=0
for rate in heart_rates:
    total+=rate[1]

#calculating the average
average=round(total/len(heart_rates))
print(f"Your average heart rate today is {average:,.2f}")