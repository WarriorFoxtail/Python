# Program to calculate bugeting amounts across various categories
print("Budget Breakdown Calculator.")

# Getting user data
total = float(input("Please enter your total budget: ")) # budget total
housing = float(input("Please enter your total housing cost: ")) # total spent on housing
utilities = float(input("Please enter your total utility cost: ")) #total spent on utilities
groceries = float(input("Please enter your total grocery cost: ")) #total spent on groceries
transportation = float(input("Please enter your total transportation cost: ")) # total spent on transportation
health = float(input("Please enter your total health care cost: ")) # total spent on health care
personal = float(input("Please enter your total personal care cost: ")) # total spent on personal care
clothing = float(input("Please enter your total clothing cost: ")) # total spent on clothing
debt = float(input("Please enter any outstanding debts: ")) # total of any debts owed

# Calculating percentages from the given data (% = section total / budget total * 100)
percent_housing = (housing / total) * 100 #percentage for housing
percent_util = (utilities / total) * 100 #percentage for utilities
percent_grocery = (groceries / total) * 100 #percentage for gorceries
percent_transport = (transportation / total) * 100 #percentage for transportation
percent_health = (health / total) * 100 #percentage for health
percent_personal = (personal / total) * 100 #percentage for personal care
percent_cloth = (clothing / total) * 100 #percentage for clothing
percent_debt = (debt / total) * 100 #percentage of debt

# Outputting results to user
print(f"The cost of housing is {percent_housing:.2f}% of your total budget.")
print(f"The cost of utilities is {percent_util:.2f}% of your total budget.")
print(f"The cost of groceries is {percent_grocery:.2f}% of your total budget.")
print(f"The cost of transportation is {percent_transport:.2f}% of your total budget.")
print(f"The cost of health care is {percent_health:.2f}% of your total budget.")
print(f"The cost of personal care is {percent_personal:.2f}% of your total budget.")
print(f"The cost of clothing is {percent_cloth:.2f}% of your total budget.")
print(f"Your remaining debts account for {percent_debt:.2f}% of your total budget.")