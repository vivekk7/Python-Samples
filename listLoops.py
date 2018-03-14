"""2.Take a list, for example
a=[1,2,2,3,4,55,65,76,78]
Write a program to return list with numbers less than 10.
Step 2:
Take the number x from user and print a new list with elements less than number x."""

a = [1,2,2,3,4,55,65,76,78]
new_list1 = []
new_list2 = []

for index in range(len(a)):
    #print 'Current: ', a[index]
    if (a[index] < 10):
        new_list1.append(a[index])
        
print new_list1
x = input("\nStep 2: Enter a number:")
for index in range(len(a)):
    if (a[index] < x):
        new_list2.append(a[index])
print new_list2
        
