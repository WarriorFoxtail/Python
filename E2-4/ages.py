#calcuating a person's age in years, months, weeks, and days
from datetime import datetime

def main():
    print("\n")
    now=datetime.now()
    print(f"now: {now}")
    #timestamp=datetime.now().time()
    #print(f"timestamp: {timestamp}")
    print("\n")
    try:
        birth_year=int(input("Please enter the year you were born: "))
        month=int(input("Please enter the month you were born as a number (e.g. May would be 5): "))
        day=int(input("Please enter the day of the month you were born: "))
        birthday=datetime(birth_year, month, day)
        print(f"Your birthday is {birthday}")
    except Exception as e:
        print(f"Whoops! {e}") 
        main()


main()