# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
output1=string1.capitalize()
print(output1)

# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> "  python  "
string2 = "python"
output2=string2.center(12, '^')
print(output2)

# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
output3=string3.endswith("on")
print(output3)

# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
output4=string4.find("th")
print(output4)

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
output5=string5.isalnum()
print(output5)

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
output6=string6.isalpha()
print(output6)

# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
output7=string7.islower()
print(output7)

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if "   " is all whitespace
string8 = "   "
output8=string8.isspace()
print(output8)

# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
output9=string9.isupper()
print(output9)

# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
outputi=separator.join(iterable1)
print(outputi)

# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
output10=string10.lower()
print(output10)

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from "  python"
string11 = "  python"
output11=string11.lstrip()
print(output11)

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python  "
string12 = "python  "
output12=string12.rstrip()
print(output12)

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
output13=string13.replace("python", "snake")
print(output13)

# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
output14=string14.rfind("n")
print(output14)

# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
output15=string15.split("-")
print(output15)

# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
output16=string16.startswith("py")
print(output16)

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from "  python  "
string17 = "  python  "
output17=string17.strip()
print(output17)

# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
output18=string18.swapcase()
print(output18)

# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
output19=string19.title()
print(output19)

# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
output20=string20.upper()
print(output20)