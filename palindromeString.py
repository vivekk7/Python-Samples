"""Take a string input from the user and check if its Palindrome or not."""

string1 = raw_input("Enter a string:")

if string1 == string1[::-1]:
    print "%s is a Palindrome string" % (string1)
else:
    print "%s is not a Palindrome string" % (string1)

