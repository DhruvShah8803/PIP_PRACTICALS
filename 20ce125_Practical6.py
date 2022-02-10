
# @author
# Name : Dhruv Shah
# ID : 20CE125


# Aim :

# You are given n words. Some words may repeat. For each word, output its
# number of occurrences. The output order should correspond with the input order
# of appearance of the word. See the sample input/output for clarification.

# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output
# 3
# 2 1 1

# Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input
# at the first and last positions. The other words appear once each. The order of the
# first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the
# output.

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

# Make one set to remove occurence of words
MySet = set(MyList)

# print length of set ( Total number of distinct words )
print(f"\n{len(MySet)}")

# Make another list of only distinct words
MyList2 = list(MySet)

# Make third list
MyList3 = []

# Make one loop that will append number of occurence of all distinct words 
i = 0
while i < len(MyList2):
    MyList3.append(MyList.count(MyList2[i]))
    i += 1

# Make list in sorted form
MyList3.sort()

# Make list in reversed form to get appropriate output
MyList3.reverse()

# Print output
print(*MyList3)
