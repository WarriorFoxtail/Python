#defining main
def main():
    #setting up an empty list for book titles
    books=[]
    #initializing while loop
    while len(books)<4: #will iterate until 10 titles are entered
        #getting book titles from user
        titles=input("Please enter a book title: ").title() #esures the titles are properly capitalized
        books.append(titles) #appends titles to empty list
    #print(books) #ensuring the titles are being saved to the list correctly
    sorted=books #creating a separate list for the sorted books
    sorted.sort() #sorting the new list
    #print(sorted) #checking the new list prints correctly
    for book in sorted: #initializing for loop to print each book
        print(book) #prints each book on a new line

#calling main
main()