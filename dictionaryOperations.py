"""Print addition of all the integers from the following dict(), make sure you don't miss any integer value.
dict = {'first':'apple','second':'100','third':16,4:42,'six':(5,12,8),
'ten':['aaa','ball',34,01],'seven':'555','100':{1:10,2:20,'pop':5},'float':10.5}"""

dict = {'first':'apple','second':'100','third':16,4:42,'six':(5,12,8),'ten':['aaa','ball',34,01],'seven':'555','100':{1:10,2:20,'pop':5},'float':10.5}

dict1 = dict.values()[5]
list1 = dict.values()[3]
#tup = dict.values()[6]
#print dict.keys()
#print dict.values()

#Sum of keys values
total_keys = dict.keys()[2] + int (dict.keys()[5])
#print dict.values()

#Sum of values
total_values = int (dict.values()[0]) + dict.values()[2] + dict.values()[4] + int(dict.values()[7]) + dict.values()[1]

total = total_keys + total_values + (list1[2] + list1[3]) + sum(dict.values()[6]) + (dict1.keys()[0] + dict1.keys()[1]) + (dict1.values()[0] + dict1.values()[1] + dict1.values()[2])

print "Total = " + str(total)




