#weekly task 06

#author: Sofiia Meteliuk

#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#You should create a function called sqrt that does this.
# main code for newton_method from https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d 
#I added input and output

def newton_method(number, number_iters = 500):
    a = float(number) # number to get square root of
    for i in range(number_iters): # iteration number
        number = 0.5 * (number + a / number) # update
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
    return round(number,1) 


input1 = float(input("Please enter a positive number: "))
print(f"The square root of {input1} is approx.  {newton_method(input1)}.")
