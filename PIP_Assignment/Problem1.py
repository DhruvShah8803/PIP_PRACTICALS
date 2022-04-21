Mylist1 = list(input())

Mylist2 = list(set(Mylist1))
Mylist3 = []

i = 0
while i < len(Mylist2):
    Mylist3.append(Mylist1.count(Mylist2[i]))
    i += 1

for step in range(len(Mylist2)):
        max_idx = step

        for i in range(step + 1, len(Mylist2)):
            # select the maximum element in each loop
            if Mylist3[i] > Mylist3[max_idx]:
                max_idx = i
         
        # put max at the correct position
        (Mylist2[step], Mylist2[max_idx]) = (Mylist2[max_idx], Mylist2[step])
        (Mylist3[step], Mylist3[max_idx]) = (Mylist3[max_idx], Mylist3[step])

j = 0
while j < len(Mylist2):
    print(Mylist2[j], Mylist3[j])
    j += 1