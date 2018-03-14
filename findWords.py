# coding: utf-8
"""We have define a word as any sequence of one or more lower-case letters(no numbers or punctuationa) where words are seprated by white space.
Write a program to read all the words (on every line) for standard input, and to produce, in order, on separate lines:
1. the count of words in input
2. the word "words"
3. each unique word, and the count of times it occurs in the input (listed in alphabetical order, each on its own line, with a space between the word and count)
4. the word "letters"
5. for every letter from a to z, the letter, and the count of times that letter occurred IN A WORD in the input (listed in a alphabetical order, each on its own line, with a space between the letter and count)

There must be "whitespace" separating valid words in the input -- actual spaces, and newlines. If your program finds something that in not whitespace, and not a word it should skip until it comes to a valid word (or the end of the input). Finding a non-word character next-character makes the while sequence a non-word.
Expected Input: 'a to the four where supers i be the other four'
Output:
11
words
a 1
be 1
four 2
i 1
other 1
supers 1
the 2
to 1
where 1
letters
a 1
b 1
c 0
d 0
e 7
f 2
g 0
h 4
i 1
j 0
k 0
l 0
m 0
n 0
o 4
p 1
q 0
r 5
s 2
t 4
u 3
v 0
w 1
x 0
y 0
z 0
"""

def numberOfWords(str1):
    list = str1.split()
    
    
    
