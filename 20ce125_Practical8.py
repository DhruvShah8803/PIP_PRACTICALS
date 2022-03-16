
# @author
# Name : Dhruv Shah
# ID : 20CE125


# Aim :
# Write a Program in Python to implement a Stack Data Structure using Class and Objects,
# with push, pop, and traversal method.

# GitHUb repository link: https://github.com/DhruvShah8803/PIP_Practicals

print(f"\nName : Dhruv Shah \nID : 20CE125\n")


class Stack_Implementation:

    def __init__(self):
        self.top = -1
        self.Stack = list([])

    def push(self, value):
        self.top += 1

        if len(self.Stack) > self.top :
            self.Stack[self.top] = value
        else:
            self.Stack.append(value)

        print(f"{value} is pushed into stack.")

    def pop(self):
        if self.top == -1:
            print("There is Underflow in stack")
        else:
            value = self.Stack[self.top]
            self.top -= 1
            print(f"{value} is pop out from the stack")

    def printmy_data(self):
        if self.top != -1:

            index = self.top
            Mylist = list([])

            i = index 
            while i >= 0 :
                Mylist.append(int(self.Stack[i]))
                i -= 1
    
            print("elements of stack from top to bottom is : ")
            print(*Mylist)

        else:
            print("There is no elements in Stack")


Stack1 = Stack_Implementation()

while(True):

    choice = input(
    f"\nEnter 1 for push, 2 for pop, 3 for print values and 4 for exit\n\nEnter your choice : ")

    if choice == '1':
        value = input("\nEnter value which you want to push : ")
        Stack1.push(value)
    elif choice == '2':
        Stack1.pop()
    elif choice == '3':
        Stack1.printmy_data()
    elif choice == '4':
        break
    else:
        print("\nEnter valid input")
