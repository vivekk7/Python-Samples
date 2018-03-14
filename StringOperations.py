"""If you are given 2 strings, perform concatenation operation while 
omitting the fist character of each word. O/P: 'java', 'code' → ‘avaode'"""

str1 = raw_input("Enter 1st string:")
str2 = raw_input("Enter 2nd string:")
print (str1[1:] + str2[1:])
