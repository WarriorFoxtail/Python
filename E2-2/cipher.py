#Caesar cipher
#get input from user
text = input("Enter your message: ")
#stores ecrpyted message to an empty string
cipher = ''
#initializes for loop to iterate through each character of input message
for char in text:
    #skips character if it isn't an alphabet letter
    if not char.isalpha():
        continue
    #converts characters to uppercase
    char = char.upper()
    #finds ascii code and shifts it by one
    code = ord(char) + 1
    #loops back to A if ascii code exceeds Z
    if code > ord('Z'):
        code = ord('A')
    #coverts new ascii code back to alphabet character and adds it to cipher string
    cipher += chr(code)

#displays encrypted message
print(cipher)