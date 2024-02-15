# Program to calculate a letter grade based off numeric grade value
# Input numerical grade value
grade = int(input("Please enter the numeric grade: "))

# Check if the grade is below 60
if grade < 60:
    letter = "F" # grade below 60 is an F

# Check if grade is between 60 and 69
elif grade < 69:
    letter = "D" # grade between 60 and 69 is a D

# Check if grade is between 70 and 79
elif grade < 79:
    letter = "C" # grade between 70 and 79 is a C

# Check if grade is between 80 and 89
elif grade < 89:
    letter = "B" # grade between 80 and 89 is a B

# Check if grade is between 90 and 100
elif grade < 100:
    letter = "A" # grade of 90-100 is an A

# Grade equals 100
else:
    letter = "A" # includes 100 as an A grade

# results
print(f"Your letter grade is: {letter}")