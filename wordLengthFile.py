# coding: utf-8
"""Write a program that will calculate the average word length of a text stored in a file 
(i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
Read the text file and get the length of the words. 
Read the file and calculate the sum of length of all the words. Find the average word length."""
from macerrors import afpItemNotFound

file_obj = open("file2.txt","r")
data = file_obj.readline()
print data
total = 0
while data:
    words = data.split()
    data = file_obj.readline()
    print words
    for i in range(len(words)):
        total += len(words[i])

print "Average word length is " + str(total/len(words))
file_obj.close()
