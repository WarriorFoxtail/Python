#defining the function
def custom_song(noun, disaster, body, environment, being, verb, direction, weather):
    print(f"Is this the real {noun}? Is this just fantasy?")
    print(f"Caught in a {disaster}, no escape from reality")
    print(f"Open your {body}, look up to the {environment} and see")
    print(f"I'm just a poor {being}, I need no sympathy")
    print(f"Because I'm easy {verb}, easy go, little {direction}, little low")
    print(f"Any way the {weather} blows, doesn't really matter to me")
    print(f"To me")

#getting user input
def user_input():
    noun=input("Please enter a noun: ")
    disaster=input("Please enter a natural disaster: ")
    body=input("Please enter a plural body part: ")
    environment=input("Please enter a type of environment: ")
    being=input("Please enter a type of living being: ")
    verb=input("Please enter a verb: ")
    direction=input("Please enter a direction: ")
    weather=input("Please enter a type of weather pattern: ")
    return noun, disaster, body, environment, being, verb, direction, weather

#calling the functions
def main():
    noun, disaster, body, environment, being, verb, direction, weather=user_input()
    custom_song(noun, disaster, body, environment, being, verb, direction, weather)

#calling main
main()