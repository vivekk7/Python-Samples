string1 = raw_input("Enter any string:")
i = 0
old_list = list(string1)
#new_list = []
new_string =''
for i in range(len(old_list)):
    e = old_list.pop()
    #new_list.append(e)
    new_string += e
#print str(new_list)
#str1 = ''.join(str(x) for x in new_list)
#print str1
#print new_string

if new_string == string1:
    print "Entered string is a palindrome"
else:
    print "Entered string is not a palindrome"    