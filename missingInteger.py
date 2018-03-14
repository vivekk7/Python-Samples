# coding: utf-8
"""Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2."""

def convertToList(s):
    input_list = s.split()
    input_list = [int(x) for x in input_list]
    #print type(input_list)
    #print input_list
    return input_list

def main():
    unsorted_array = raw_input("Enter an unsorted integer array:")
    sorted_array = convertToList(unsorted_array)
    print type(sorted_array)
    #print sorted_list
    sorted_array.sort()
    print sorted_array

    missing_number = 1
    
    #to capture cases when the list has only 1 integer and if it is a positive number
    if (len(sorted_array) == 1):
        if (sorted_array[0] > 0) :
            missing_number = sorted_array[0] + 1
     
    for i in range((len(sorted_array)-1)):
        if ((sorted_array[i] > 0)  and (sorted_array[i+1] > 0)):
            
            if ((i > 0) and (sorted_array[i] > missing_number)):
                break
            
            if (sorted_array[i+1] != (sorted_array[i]+1)):
                missing_number = sorted_array[i] + 1
                break
            else:
                missing_number = sorted_array[i+1] + 1      
    print missing_number
    
    print "Missing number is {0}".format(missing_number)

main()

            