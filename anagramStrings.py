# coding: utf-8
"""Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic
order.
All inputs will be in lower-case."""

def convertToList(s):
    input_list = s.split()
    input_list = [str(x) for x in input_list]
    return input_list

def anagram(str1,str2):
    if (len(str1) == len(str2)):
        list1, list2 = list(str1), list(str2)
        list1.sort()
        list2.sort()
        if (list1 == list2):
            return True
        else: return False
    else:
        return False

user_input = raw_input("Enter a list of strings:")
sorted_list = convertToList(user_input)
sorted_list.sort()

newdict = {}

newdict.setdefault(sorted_list[0], [])

for i in range(len(sorted_list)):
    done = 0
    for key, value in newdict.items():
        if (anagram(sorted_list[i],key) == True):
            value.append(sorted_list[i])
            #print newdict
            done = 1
            break
    if done == 0:
        newdict[sorted_list[i]]=[sorted_list[i]]
                
print newdict.values()


    



