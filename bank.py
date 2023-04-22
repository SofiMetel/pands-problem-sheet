#The program should:
#1. Prompt the user and read in two money amounts (in cent)
#2. Add the two amounts
#3. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#$ python bank.py
#Enter amount1(in cent): 65
#Enter amount2(in cent): 180
#The sum of these is €2.45
from decimal import Decimal


input1 = input("Enter amount1(in cent): ") #step 1.
input2 = input("Enter amount1(in cent): ") 

#sum = int(input1) + int(input2) # step 2.


# to achive step 3 I use example from https://www.w3schools.com/python/python_string_formatting.asp
#price = 49
#txt = "The price is {:.2f} dollars"
#print(txt.format(price))


output = "The sum of these is €{:.2f}" 

#this piece of code was created to check data type
#a=sum/100
#print(type(a))
#print(output.format(sum/100))



'''
In feedback lecturer asked not to use floating point numbers. They always will appear if we do division like this (sum/100)
Main idea behind it is the fact that floating point numbers can create more errors. 
https://www.geeksforgeeks.org/floating-point-error-in-python/ 
They recommended "Check floating point section in python documentation for more such behaviours."

I read tutorial about floating point and found out that decimal package can help reduce rounding error changing number from float to decimal
https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues

'''

#this piece of code was created to check data type
#decimalnum=Decimal.from_float((sum/100))
#print(type(decimalnum))
#print(output.format(decimalnum))

#print(output.format(Decimal.from_float((sum/100))))

'''
But Later I started to hesitate because it looks like the number becomes at first float
after /100 and only then turns into decimal and from python docs it wasn`t clear for 
me if in this case floating-point-error would be a problems for us or not.
So I decided to turn integer into decimal and then perform division
'''

sum = Decimal(input1) + Decimal(input2) # step 2.
#print(type(sum))
#print(type(sum/100))
print(output.format(sum/100)) #step 3