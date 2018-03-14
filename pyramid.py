"""A single integer, n , denoting the size of the staircase.
Print a staircase of size n using # symbols and spaces.
Input: 6 
Output:
          #
         ##
        ###
       ####
      #####
     ###### """

n = input("Enter any number for a pyramid:")
str1 = ''
for i in range(n):
    str1+=  "#"
    print(str1.rjust(n,' '))
    #print i
#print("End")
