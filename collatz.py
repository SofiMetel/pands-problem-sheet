#WEEK 4 Task
#Author: Sofiia Meteliuk
'''Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.
'''

integer =int(input("Please enter a positive integer: ")) # asking for input

answer = [integer]

while integer!=1:  #the program will end if the current value =1
    if integer%2==0: #if current value is even ->
        integer=integer//2 #multiply it by two
        answer.append(integer) #add new value to list, so we will have nice looking output
    else : #if current value is odd
        integer=integer*3+1 # multiply it by three and add one
        answer.append(integer) #add new value to list, so we will have nice looking output
        
#print(answer)
print(*answer, sep = " ") #making output looks alike, no brackets, no commas