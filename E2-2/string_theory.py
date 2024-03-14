def main():
    cool="Bowties are cool. Python is cool. Ducks are cool."

    #capitalize
    print(cool.capitalize())
    
    #alphanumeric
    alphanum="hello-123".isalnum()
    print(alphanum)

    #find and replace
    findnrep=cool.replace("cool", "epic")
    print(findnrep)

    #splitting strings
    spliting=cool.split(".")
    print(spliting)

main()