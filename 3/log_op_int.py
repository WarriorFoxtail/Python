# Program to compare two integers using basic logic operators

# Getting user input
a=int(input("Please enter an integer: "))
b=int(input("Please enter another integer: "))

# AND operator
if a>0 and b>0: #checking if both input numbers are greater than 0
    print("Both integers "+str(a)+" and "+str(b)+" are greater than zero? True")
elif a<0 and b>0:
    print("Both integers "+str(a)+" and "+str(b)+" are greater than zero? False")
elif a>0 and b<0:
    print("Both integers "+str(a)+" and "+str(b)+" are greater than zero? False")

if a>100 and b>100: #checking if both input numbers are greater than 100
    print("Both integers "+str(a)+" and "+str(b)+" are greater than one hundred? True")
else:
    print("Both integers "+str(a)+" and "+str(b)+" are greater than one hundred? False")

#OR operator
if a%2==0 or b%2==0: #checking if either input number is even
    print("Either integer "+str(a)+" or "+str(b)+" is even? True")
else:
    print("Either integer "+str(a)+" or "+str(b)+" is even? False")

if a<50 or b<50: #checking if either input number is less than 50
    print("Either integer "+str(a)+" or "+str(b)+" is less than fifty? True")
else:
    print("Either integer "+str(a)+" or "+str(b)+" is less than fifty? False")

#NOT operator
if not a==b: #checking if the input numbers are equal to each other
    print("Integer "+str(a)+" is not equal to integer "+str(b)+" ? True")
else:
    print("Integer "+str(a)+" is not equal to integer "+str(b)+" ? False")

if not a==100: #checking in input a is equal to 100
    print("Integer "+str(a)+" is not equal to one hundred? True")
else:
    print("Integer "+str(a)+" is not equal to one hundred? False")