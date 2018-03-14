# coding: utf-8
"""Write a program that given a text file will create a new text file 
in which all the lines from the original file are numbered 
from 1 to n (where n is the number of lines in the file)."""

#file1 = open("file1.txt", "w+")
#file1.write("Hey sunshine! \nHow are you doing?")
#file1.close()

file2 = open("file1.txt","r+")
str1 = file2.read()
list1 = file2.readlines()
print str1
print list1
