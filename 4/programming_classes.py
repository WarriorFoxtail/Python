#defining the function
def programming_classes():
    classes=("Intro to Python", "Advanced Python", "Database Essentials", 
             "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")
    
    for lesson in classes:
        print(lesson, end=" ")

    print(f"\nThere are {len(classes)} classes in the Programming Certificate curriculum.")

programming_classes()