l = input("Enter a number:")
k = 1
for i in range(l):
    print " " * (l-1) + "#" *i + "#" *(k-1)
    k +=1
    l -=1