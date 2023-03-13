#weekly task 05

#author: Sofiia Meteliuk

#TASK: Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
#$ python weekday.py
#Yes, unfortunately today is a weekday.
#An example of running it on a Saturday is as follows:
#$ python weekday.py
#It is the weekend, yay!

#main idea from https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/?ref=rp 

from datetime import datetime

# create datetime
x = datetime.now()

#weekday() function is used to get the week number based on given DateTime. It will return the number in the range of 0-6
if x.weekday() >4:  #if x.weekday is equil to 5 or 6 - it is Saturday or Sunday
    print("It is the weekend, yay!")
else: 
    print("Yes, unfortunately today is a weekday.")
