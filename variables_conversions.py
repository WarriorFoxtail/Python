# Defining the variables for kilogram values
kg_value_1 = 20.0
kg_value_2 = 43.6
kg_value_3 = 96.5
kg_value_4 = 32.8

# Defining the conversion factor
conversion_factor = 2.20462

# calculating pounds for each kilogram value
pounds_1 = kg_value_1 * conversion_factor
pounds_2 = kg_value_2 * conversion_factor
pounds_3 = kg_value_3 * conversion_factor
pounds_4 = kg_value_4 * conversion_factor

# outputting the results
print(f"{kg_value_1} kilograms is equal to {pounds_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {pounds_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {pounds_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {pounds_4:.2f} pounds.")