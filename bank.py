#The program should:
#1. Prompt the user and read in two money amounts (in cent)
#2. Add the two amounts
#3. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#$ python bank.py
#Enter amount1(in cent): 65
#Enter amount2(in cent): 180
#The sum of these is €2.45

input1 = input("Enter amount1(in cent): ") #step 1.
input2 = input("Enter amount1(in cent): ") 

sum = int(input1) + int(input2) # step 2.


# to achive step 3 I use example from https://www.w3schools.com/python/python_string_formatting.asp
#price = 49
#txt = "The price is {:.2f} dollars"
#print(txt.format(price))


output = "The sum of these is €{:.2f}" 
print(output.format(sum/100))

#or one more way for step 3.
#print(f"The sum of these is €{sum/100}")