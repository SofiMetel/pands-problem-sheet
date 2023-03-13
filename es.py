#Weekly task 07

#author: Sofiia Meteliuk

#Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
#The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

# copied three pages of moby dick from http://www.literaturepage.com/read.php?titleid=mobydick&abspage=13&changesize=3

import sys


with open({sys.argv[0]} , 'r') as f:   # open document as f
    mobydick = f.read()
    f.close ()

number = mobydick.count ('e')  
print (number)