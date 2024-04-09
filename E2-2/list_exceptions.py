#defines main
def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    print(top_artists) #printing the list for the user

    artist=int(input("Please enter the index for an artist in the list")) #asks user for index of a given artist
    if artist in top_artists: #initializing an if statement to see if the index is correct
        try: #initializing a try/except statement
            print(f"The artist {top_artists[artist]} is currently assigned to that index.")
        except (ValueError, IndexError) as e: #using a tuple to check for both Index and Value errors
            print("Sorry! An input error occured: {e}") #displaying the error to the user
    
    

main()