#declaring global variables
global KG_PER_LBS, M_PER_IN
KG_PER_LBS=0.453592 #kilograms per pound
M_PER_IN=0.0254 #meters per inch

#calculating BMI based on height and weight
def calculate_bmi(weight_lbs, height_in):
    weight=weight_lbs*KG_PER_LBS
    height=height_in*M_PER_IN
    #double checking that the conversions are correct
    #print(f"Your weight in kilograms is {weight:,.2f}kg.")
    #print(f"Your height in meters is {height:,.2f}m.")
    bmi=weight/(height*height)
    return bmi

#getting weight and height data from user
weight_lbs=float(input("Please enter your weight in pounds: "))
height_in=float(input("Please enter you height in inches: "))

#displaying user's BMI
print(f"Your BMI is {calculate_bmi(weight_lbs, height_in):,.2f}")

#calculating and displaying the weight category of user
if calculate_bmi(weight_lbs, height_in)>=30:
    print("You are considered to be obese.")
elif 25<=calculate_bmi(weight_lbs, height_in)<29.9:
    print("You are considered to be overweight.")
elif 18.5<=calculate_bmi(weight_lbs, height_in)<24.9:
    print("You are considered to be of normal weight.")
else:
    print("You are considered to be underweight.")