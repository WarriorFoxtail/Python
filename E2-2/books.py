def main():
    books=[]
    i=0
    while i<len(books):
        title=input("Please enter a book title. Once you have entered 10 titles, enter 'Done': ")
        if title=='Done':
            break
        books.append(title)

main()