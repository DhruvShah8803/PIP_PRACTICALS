
# @author
# Name : Dhruv Shah
# ID : 20CE125

# GitHUb repository link : https://github.com/DhruvShah8803/PIP_Practicals


# Tuple


# a. Write a Python program to create a tuple with different data types.

MyTuple = ("Dhruv",1,1.92)
print(f"\na.\n\nYour Tuple with different datatypes is {MyTuple}\n")



# b. Write a Python program to create a tuple with numbers and print one item.

MyTuple = (1, 2, 3, 4, 5)
print(f"\nb.\n\nYour tuple is {MyTuple}")
print(f"first element of your tuple is : {MyTuple[0]}\n")



# c. Write a Python program to add an item in a tuple.

MyTuple = (1, 2, 3, 4, 5)
print(f"\nc.\n\nOld tuple : {MyTuple}")

MyList = list(MyTuple)
MyList.append(6)

MyTuple3 = tuple(MyList)
print(f"New tuple : {MyTuple}\n")



# d. Write a Python program to convert a tuple to a string.

MyTuple4 = ("Dhruv", "Shubham", "Yukta", "Vishal", "Gargi")
print(f"\nd.\n\nOld type : {type(MyTuple4)}")

MyString1 = str(MyTuple4)
print(f"New type : {type(MyString1)}\n")



# e. Write a Python program to find the length of a tuple.

MyTuple5 = (1,2,3,4)
print(f"\ne.\n\nYour tuple is {MyTuple5}")
print(f"Length of your tuple is {len(MyTuple5)}\n")
