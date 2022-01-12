
# @author
# Name : Dhruv Shah
# ID : 20CE125

# GitHUb repository link : https://github.com/DhruvShah8803/PIP_Practicals


# Set


# a. Write a Python program to add member(s) in a set and clear a set

MySet1 = {1, 2, 3, 4, 5}
print(f"\na.\n\nOld set : {MySet1}")

MySet1.add(6)
MySet1.add(9)
print(f"New set : {MySet1}")

MySet1.clear()
print(f"New set after clear : {MySet1}\n")



# b. Write a Python program to remove an item from a set if it is present in the set.

MySet2 = {"Goa", "Gujarat", "Aasam", "Bengal"}
print(f"\nb.\n\nSet : {MySet2}")

MyString2 = input("Which element do you want to remove ? \n")

if MySet2.__contains__(MyString2):
    MySet2.remove(MyString2)
    print(f"New set : {MySet2}\n")
else:
    print(f"{MyString2} is not present in the set.\n")


# c. Write a Python program to create an intersection, Union, difference of sets.


Set1 = {1,2,3,4,5}
Set2 = {3,4,5,6}

print(f"\nc.\n\nIntersection of {Set1} & {Set2} is {Set1.intersection(Set2)}.")
print(f"Union of {Set1} & {Set2} is {Set1.union(Set2)}.")
print(f"Difference of {Set1} & {Set2} is {Set1.difference(Set2)}.\n")


# d. Write a Python program to find maximum and the minimum value in a set.

MySet3 = {1,2,3,4,5}
print(f"\nd.\n\nSet : {MySet3}")
print(f"Maximum Value : {max(MySet3)}")
print(f"Minimum Value : {min(MySet3)}\n")


# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

# 1st. Most common elements from list

Mylist = [1,2,3,4,3,2]
Mylist2 = list(set(Mylist))

print(f"\ne.\n\nYour list is {Mylist}\n")
MaxNo = 0
Maxvalue = list([])

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) > MaxNo :
        MaxNo = Mylist.count(Mylist2[i])
    i += 1

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) == MaxNo :
        Maxvalue.append(Mylist2[i])
    i += 1

i = 0
while i < len(Maxvalue) :
    print(f"{Maxvalue[i]} is repeated {MaxNo} times in List")
    i += 1


# 2nd. Most common elements from tuple

MyTuple = (1,2,3,3,4,2,1)

print(f"\n\nYour Tuple is {MyTuple}\n")

Mylist = list(MyTuple)
Mylist2 = list(set(Mylist))

MaxNo = 0
Maxvalue = list([])

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) > MaxNo :
        MaxNo = Mylist.count(Mylist2[i])
    i += 1

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) == MaxNo :
        Maxvalue.append(Mylist2[i])
    i += 1


i = 0
while i < len(Maxvalue) :
    print(f"{Maxvalue[i]} is repeated {MaxNo} times in Tuple")
    i += 1


# 3rd. Most common elements from Dictionary

Dic = {1:"Dhruv" , 2:"Prutha" , 3:"Jiya" , 4:"Samarth" , 5:"Dhruv" , 6 : "Samarth"}

print(f"\n\nYour Dictionary is {Dic}\n")

Mylist = list(Dic.values())
Mylist2 = list(set(Mylist)) 

MaxNo = 0
Maxvalue = list([])

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) > MaxNo :
        MaxNo = Mylist.count(Mylist2[i])
    i += 1

i = 0
while i < len(Mylist2) :
    if Mylist.count(Mylist2[i]) == MaxNo :
        Maxvalue.append(Mylist2[i])
    i += 1


i = 0
while i < len(Maxvalue) :
    print(f"{Maxvalue[i]} is repeated {MaxNo} times in Dictionary")
    i += 1
print()
