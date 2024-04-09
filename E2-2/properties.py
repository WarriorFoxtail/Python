class Student:
    # Class variable
    school_name = "McHenry County College"

    def __init__(self, first_name, last_name, student_id, grade_level="Freshman"):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__grade_level = grade_level

    #Getters for first_name, last_name, student_id, grade_level
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
        
    def get_student_id(self):
        return self.__student_id
    
    def get_grade_level(self):
        return self.__grade_level

    #Setters for first_name, last_name, student_id, grade_level
    def set_first_name(self, value):
        self.__first_name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_student_id(self, value):
        self.__student_id = value
    
    def set_grade_level(self, value):
        self.__grade_level = value

    #Similarly, create getters and setters for last_name, student_id, and grade_level

    def print_student_details(self):
        print("Student Details:", vars(self))

    def print_info(self):
        print(self.__first_name + " " + self.__last_name)
        print(self.__student_id)
        print(self.__grade_level)

def check_property(studentObject):
    print(hasattr(studentObject, "first_name"))

def main():
    ducktor_quacks = Student("Meri", "Quacksalot", '009234', "Super Senior")
    print("\n")
    print(ducktor_quacks.get_first_name())
    ducktor_quacks.print_student_details()
    ducktor_quacks.print_info()

    print("\n")
    ducktor_quacks.set_grade_level("Ducktorate")
    ducktor_quacks.print_info()

    print("\n")
    print(hasattr(ducktor_quacks, "first_name"))
    check_property(ducktor_quacks)

main()