
# @author
# Name : Dhruv Shah
# ID : 20CE125

# GitHUb repository link : https://github.com/DhruvShah8803/PIP_Practicals


# Dictionary


# a. Write a Python script to check whether a given key already exists in a dictionary.


MyDictionary = {1:"Rabbit",2:"is",3:"very",4:"Cute"}

# To convert Dictionary of all keys into list
Mylist = list(MyDictionary.keys())

print(f"\na.\n\nYour Dictionary : {MyDictionary}")

Key = int(input(f"Enter Your key : "))

# To check whether Key is contained by list or not
if Mylist.__contains__(Key) :
    print("Key already exists in a dictionary.\n")
else :
    print("Key does not exists in a dictionary.\n")




# b. Write a Python script to merge two Python dictionaries.


MyDictionary1 = {1:"Rabbit",2:"is",3:"very",4:"Cute"}
MyDictionary2 = {5:"Dog"}

print(f"\nb.\n\nYour two dictionarys are {MyDictionary1} and {MyDictionary2}.")

# To merge both Dictionary into MyDictionary1
MyDictionary1.update(MyDictionary2)

print(f"After merge your dictionary is {MyDictionary1}\n")




# c. Write a Python program to sum all the items in a dictionary.


MyDictionary = {1:100,2:200,3:300,4:400}

print(f"\nc.\n\nYour Dictionary is {MyDictionary}")

# To convert Dictionary of all values into list
Mylist = list(MyDictionary.values())
print(f"List of values is {Mylist}")

sum = 0
# To do sum of all values
i = 0
while i < len(Mylist):
    sum += Mylist[i]
    i += 1

print(f"\nSum of all value is {sum}\n")




# d. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}


MyDictionary = {0:10,1:20}

print(f"\nd.\n\nYour Dictionary is {MyDictionary}")

Key = int(input("Enter Your key : "))

Value = input(f"Enter value at {Key} : ")

# To add a value at entered key
MyDictionary[Key] = Value

print(f"Now, your updated dictionary is {MyDictionary}")




# e. Write a Python script to concatenate following dictionaries to create a new one.


# # Sample Dictionary :

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

print(f"\ne.\n\nYour three dictionarys are {dic1} , {dic2} and {dic3}.")

# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# To concatenate all dictionary 

dic4 = dic1 | dic2 | dic3

print(f"After concatenation your dictionary is {dic4}\n")
