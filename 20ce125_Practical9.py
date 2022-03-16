
# @author
# Name : Dhruv Shah
# ID : 20CE125


# Aim :
# Consider an example of declaring the examination result. Design three classes:
# Student, Exam, and Result. The Student class has data members such as those
# representing rollNumber, Name, etc. Create the class Exam by inheriting
# Student class. The Exam class adds fields representing the marks scored in
# six subjects. Derive Result from the Exam class, and it has its own fields
# such as total_marks. Write an interactive program to model this relationship.


# GitHUb repository link: https://github.com/DhruvShah8803/PIP_Practicals

print(f"\nName : Dhruv Shah \nID : 20CE125\n")

class Student :
    rollnumber = None
    Name = None

    def __init__(self) :
        Rollno = input("Enter Your Rollno : ")
        Name = input("Enter Your name : ")
        self.rollnumber = Rollno
        self.Name = Name


class Exam(Student) :
    Sub1 = None
    Sub2 = None
    Sub3 = None
    Sub4 = None
    Sub5 = None
    Sub6 = None

    def __init__(self) :
        Student.__init__(self)
        self.Sub1 = int(input("\nEnter your marks of first subject : "))
        self.Sub2 = int(input("Enter your marks of second subject : "))
        self.Sub3 = int(input("Enter your marks of third subject : "))
        self.Sub4 = int(input("Enter your marks of forth subject : "))
        self.Sub5 = int(input("Enter your marks of fifth subject : "))
        self.Sub6 = int(input("Enter your marks of sixth subject : "))


class Result(Exam):
    total_marks = None

    def __init__(self) :
        Exam.__init__(self)
        self.total_marks = self.Sub1 + self.Sub2 + self.Sub3 + self.Sub4 + self.Sub5 + self.Sub6 

    def print_data(self) :
        print(f"\nYour Details : \nRollNo : {self.rollnumber} \nName : {self.Name} \nTotal Marks : {self.total_marks}\n")
    

Person1 = Result()
Person1.print_data()