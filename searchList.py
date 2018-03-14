# coding: utf-8
"""Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns 
(then prints) an appropriate boolean."""

def split_list(s):
    input_list = s.split()
    input_list = [int(x) for x in input_list]
    print type(input_list)
    print input_list
    return input_list


def search_list(string_input, n):    
    result = "False"
    for i in range(len(string_input)):
        if n == string_input[i]:
            result = "True"
            break
    print result

string_input = raw_input("Enter a list of numbers in ascending order:")
list_input = split_list(string_input)

number = input("Enter a number to search in the list:")
search_list(list_input,number)

