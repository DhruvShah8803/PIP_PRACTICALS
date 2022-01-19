
# @author
# Name : Dhruv Shah
# ID : 20CE125

# GitHUb repository link : https://github.com/DhruvShah8803/PIP_Practicals


# Aim :

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up.

# Input Format: 
# The first line contains. The second line contains an array A[]  of n integers each separated by a space.

# Output Format: 
# Print the runner-up score.

# Sample Input
# 5
# 2 3 6 6 5

# Sample Output
# 5

# Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. 
# Hence, we print 5 as the runner-up score.


print(f"\nName : Dhruv Shah\nID : 20CE125")

print(f"\nInput:")
K = int(input())

MyList = list(map(int,input().split(" ")))

# To remove repeated elements converted lint into set
MySet = set(MyList)

# To find maximum element of set
Max = max(MySet)

# To remove that maximum element from set.
MySet.remove(Max)

print(f"\nOutput:")
# To print maximum element of set.
print(f"{max(MySet)}\n")
