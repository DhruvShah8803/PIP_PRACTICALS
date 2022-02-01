
# @author
# Name : Dhruv Shah
# ID : 20CE125

# GitHUb repository link : https://github.com/DhruvShah8803/PIP_Practicals


# Aim : 

# You are given a string and your task is to swap cases. In other words, convert
# all lowercase letters to uppercase letters and vice versa.

# Sample Input: HackerRank.com presents "Pythonist 2".
# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

print(f"\nName : Dhruv Shah \nID : 20CE125\n")

# Make one string for input
MyString1 = input()

# Make Another string to store answer
MyString2 = ""

# Loop for swap cases
i = 0

while i < len(MyString1):

    # It will check whether character of string is in lowercase or not
    if MyString1[i].islower():
        # to convert charcter into uppercase
        MyString2 += MyString1[i].upper()

    # It will check whether character of string is in uppercase or not
    elif MyString1[i].isupper():
        # to convert charcter into lowercase
        MyString2 += MyString1[i].lower()

    # else condition for special characters & spaces
    else:
        # to add special characters & spaces as it is
        MyString2 += MyString1[i]

    i += 1

# to print Final Answer
print(f"\n{MyString2}\n")
