def calculate_interest(principle_ammount, interest_rate, time):
    result=(principle_ammount*interest_rate*time)/100
    return result

def main():
    principle_amount=float(input("Please enter the principle amount: "))
    interest_rate=float(input("Please enter the interest rate as a whole number (5% would be 5): "))
    time=float(input("Please enter the investment time in whole years: "))
    calculated_interest=calculate_interest(principle_amount, interest_rate, time)
    print(f"The simple interest for a principle amount of ${principle_amount:,.2f} at an interest rate of {interest_rate}% over a period of {time} years is ${calculated_interest:,.2f}")
    
main()