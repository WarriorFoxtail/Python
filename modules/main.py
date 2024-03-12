from math_operations import calculator
from math_operations import geometry

result = calculator.add(5, 3)
print("Addition result: ", result)

result = calculator.subtract(10, 4)
print("Subtraction result: ", result)

result=geometry.rectangle(4, 6)
print("Area of Rectangle result: ", result, " square units.")

result=geometry.triangle(7, 9)
print("Area of Triangle result: ", result, " square units.")

result=geometry.circle(12)
print("Area of Circle result: ", result, " square units.")