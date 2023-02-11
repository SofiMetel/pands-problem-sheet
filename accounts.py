#author: Sofiia Meteliuk

#week03 task
#Please enter an 10 digit account number: 1234567890
#XXXXXX7890

input1 = input("Please enter an 10 digit account number: ")

determine_to_hide = input1[:-4] #slicing to get the part of number we want to hide
hide = input1.replace(determine_to_hide, 'X'*6) #replacing with x 6 times
#decided to use replace() becouse I`ve seen it in https://campus.datacamp.com/courses/intro-to-python-for-data-science/

print(hide)