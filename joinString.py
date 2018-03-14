"""You are given a string.  Split the string on a " " (space) delimiter and join using a - hyphen.
Sample Input
this is a string   
Sample Output
this-is-a-string"""

string = raw_input("Enter a string:")
string1 = string.split(' ')
print "-".join(string1)
