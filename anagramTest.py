def anagram(str1,str2):
    if (len(str1) == len(str2)):
        list1, list2 = list(str1), list(str2)
        list1.sort()
        list2.sort()
        if (list1 == list2):
            #print "in Loop"
            print True
        else: print False
    else:
        print False
        
str1 = raw_input("Enter 1st string:")
str2 = raw_input("Enter 2nd string:")

anagram(str1,str2)