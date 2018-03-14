"""List duplication
Take 2 list,
a= [1,2,2,3,4,13,18,26,38,66]
b= [1,1,2,5,13,16,26,33,43,49,59,66]
Write a program to print a new list which contains only common elements from both list. List a, and list b can be of different sizes."""

a = [1,2,2,3,4,13,18,26,38,66]
b= [1,1,2,5,13,16,26,33,43,49,59,66]
list1 = []
i = 0
x = 0

for i in range(len(b)):
    for x in range(len(a)):
        if a[x] == b[i]:
            list1.append(b[i])
print list1