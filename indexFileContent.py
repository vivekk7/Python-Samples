# coding: utf-8
"""Write a program that given a text file will create a new text file in which all the lines 
from the original file are numbered from 1 to n (where n is the number of lines in the file).

Create a file with say 10 lines. Now create a new file, read info from file1, and print it. 
Create a new text file with all the same lines from the original file. Now in the second file, add line numbers to that.
Read thru the file, run thru an iterator and add one index to each line."""

file_obj = open("file1.txt","r")

new_file = open("file3.txt","a")
i = 0
line = file_obj.readline()
while line:
    new_file.write(str(i)+line),
    line = file_obj.readline()
    i += 1
file_obj.close(), new_file.close()
new_file = open("file3.txt","r")
for line in new_file:
    print line,

"""
old_file_obj = open("file1.txt","r")
lines = old_file_obj.readlines()
new_file_obj = open("file3.txt","w")
for i,line in enumerate(lines):
    new_file_obj.write(str(i) + line)
old_file_obj.close(), new_file_obj.close()
"""

