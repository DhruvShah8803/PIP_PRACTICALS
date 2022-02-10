
# @author
# Name : Dhruv Shah
# ID : 20CE125


# Aim :

# Lapindrome is defined as a string which when split in the middle, gives two
# halves having the same characters and same frequency of each character. If there
# are odd number of characters in the string, we ignore the middle character and
# check for lapindrome. For example gaga is a lapindrome, since the two halves ga
# and ga have the same characters with same frequency. Also, abccab, rotor and
# xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
# The two halves contain the same characters but their frequencies do not match.
# Your task is simple. Given a string, you need to tell if it is a lapindrome.

# Sample Input:
# 6
# gaga
# abcde
# rotor
# xyzxy
# abbaab
# ababc

# Sample Output:
# YES
# NO
# YES
# YES
# NO
# NO


# GitHUb repository link: https://github.com/DhruvShah8803/PIP_Practicals

print(f"\nName : Dhruv Shah \nID : 20CE125\n")

# Make a variable to take value of n (Total Numbers) as input from user
Length = int(input())

# Make one list
MyList = []

# Loop for append n items ( which will entered by user ) to the list
i = 0
while i < Length:
    MyList.append(input())
    i += 1

print(" ")


# Make one Function that will check two string (which is passed in arguments) 
# contains same number of same characters or not

def compare(j, k):

    # Convert string into list
    List1 = list(j)
    List2 = list(k)

    # Make list in sorted manner
    List1.sort()
    List2.sort()

    # If - else condition to check whether both list are same or not
    if List1 == List2:
        print("YES")
    else:
        print("NO")


# Make Function to slice a string into two same parts

def slicer(s):
    # If condition to check whether length of string is odd or even
    if len(s) % 2 == 0:
        var = int(len(s)/2)
        # Make a list
        List3 = []
        # append two same parts of string into list
        List3.append(s[:var])
        List3.append(s[var:])
        # Pass those two parts as arguments in compare function
        compare(List3[0], List3[1])
    else:
        var = int((len(s)+1)/2)
        # Make a list
        List4 = []
        # append two same parts of string into list
        List4.append(s[:(var-1)]) 
        List4.append(s[var:]) 
        # Pass those two parts as arguments in compare function
        compare(List4[0], List4[1])

# Loop to pass all element of Mylist as argument of slicer function
k = 0
while k < len(MyList):
    slicer(MyList[k])
    k += 1
