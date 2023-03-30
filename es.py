#Weekly task 07
#author: Sofiia Meteliuk

'''
Write a program that reads in a text file and outputs the number of e's it contains. 
The program should take the filename from an argument on the command line.
 moby-dick.txt is the first three pages of moby dick from http://www.literaturepage.com/read.php?titleid=mobydick&abspage=13&changesize=3
'''


import sys #sys module

file = sys.argv[1] # sys.argv[0] is name of program file (es.py), so sys.argv[1] is the second argument that should be the name of file to read

with open(file,"r") as f:   # open document as f
    mobydick = f.read() 
    f.close ()

number = mobydick.count('e') #count number of letters 'e' in the text file
print(number) #print number of e`s