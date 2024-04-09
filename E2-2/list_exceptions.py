#defines main
def main():
    top_artists=["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    print(top_artists) #printing the list for the user

    try: #initializing a try/except statement
        number=int(input("Please enter the index for the artist you wish to replace: ")) #asks user for index of a given artist
        artist=top_artists[number] #converts the input idex to its assigned artist
        if artist in top_artists: #initializing an if statement to find the artist in the list
            print(f"The artist {artist} is currently assigned to that index.") #displays the current artist assigned to the input index
        
        new_artist=input("Please enter the name of the new artist: ") #getsuser input for new artist's name
        top_artists[number]=new_artist #replaces the old artist with the new one
        print(top_artists) #prints the new list
    except (ValueError, IndexError) as e: #using a tuple to check for both Index and Value errors
        print(f"Sorry! An input error occured: {e}") #displaying the error to the user

main()