#WEEK 4 Task
#Author: Sofiia Meteliuk
#Write a program that asks the user to input any positive integer and outputs
# the successive values of the following calculation.
#At each step calculate the next value by taking the current value and,
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.

#first-raw-quick-idea
#should change print outs, so it will be one row not a column

integer =int(input("Please enter a positive integer: ")) #step 1

while integer!=1:
    if integer%2==0:
        integer=integer//2
        print(str(integer))
    else :
        integer=integer*3+1
        print(str(integer))
        