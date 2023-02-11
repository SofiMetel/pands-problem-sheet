#author: Sofiia Meteliuk

#week03 EXTRA task
#Please enter an 10 digit account number: 1234567890
#XXXXXX7890

#Extra:
#Modify the program to deal with account numbers of any length 

#My assumption is that in some banks can exist bank accounts numbers with more than 10 digits (i.e. IBAN = 22 digits or 34 digits)
# In any way we want to show only the last 4 characters

input1 = input("Please enter account number: ")

determine_to_hide = input1[:-4] #slicing to get the part of number we want to hide
number_of_x= len(determine_to_hide) # count number of digits that stand before the last 4 we will show
hide = input1.replace(determine_to_hide, 'X'*number_of_x) #replacing with x that many times as we need 
print(hide)