"""1.Perform the below using operators:
Level 1:
Write a program asking user to enter a number, depending on whether the number is even or odd, print out an appropriate message to the user.

Level 2:
If the number is a multiple of 4, print out a different message.

Level 3:
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
If check number is divisible, tell that. Then give a different number to the user. """

a = input("Enter a number:")
#Level 1
if (a % 2 == 0):
    print "\nLevel 1: Entered number is an even number"
else: 
    print "\n Level 1: Entered number is an odd number"

#Level 2
if (a % 4 == 0):
    print "\nLevel 2: Entered number is a multiple of 4"
else:
    print "\nLevel 2: Entered number is not a multiple of 4"

#Level 3
num = input("Level 3: Enter a number num:")
check = input("Enter a number to divide by num:")
if (num % check == 0):
    print "Num divides evenly by check"
else:
    print "Num is not divisible by check"
