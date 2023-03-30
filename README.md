# pands-problem-sheet

# week 01 
created helloworld.py and pushed to GitHub

# week 02 
bank.py

The program should:

1.Prompt the user and read in two money amounts (in cent)
2.Add the two amounts
3.Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

```
$ python bank.py
Enter amount1(in cent): 65
Enter amount2(in cent): 180
The sum of these is €2.45
```

# week 03 
accounts.py

Weekly Task 03
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
```
$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
```

# week 03  EXTRA task 
extraaccounts.py

TASK: Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

My assumption is that in some banks can exist bank accounts numbers with more than 10 digits (i.e. IBAN = 22 digits or 34 digits)
In any way we want to show only the last 4 characters. 

I used len() and replace() because I`ve used them in DataCamp https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-3-functions-and-packages/


# week 04
collatz.py
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.

I used while and if\else loop in the first raw idea. The answer was printed out as a column that didn`t matched answer in the task brief. 
```
$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1
```
So I created empty list and added every new value to this list. The answer is list but without brackets or commas. 
```
print(*answer, sep = " ")
```


# week 05
weekday.py

Write a program that outputs whether or not today is a weekday. 

An example of running this program on a Thursday is given below.
```
$ python weekday.py
Yes, unfortunately today is a weekday.
```

An example of running it on a Saturday is as follows:
```
$ python weekday.py
It is the weekend, yay!
```
#main idea from https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/?ref=rp 

# week 06
squareroot.py

Task: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.
I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).I suggest that you look at the newton method at estimating square roots.
This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.


```
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.
```
The first google attempt lead me to https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d so I decided to try this code piece that worked perfectly. 
I added input\output + round function to make sure my print out is nice. 

Should I add input\output to the main function?


# weekly task 07

TASK: Write a program that reads in a text file and outputs the number of e's it contains. 
The program should take the filename from an argument on the command line.
```
$ python es.py moby-dick.txt
116960
```

moby-dick.txt is the first three pages of moby dick from http://www.literaturepage.com/read.php?titleid=mobydick&abspage=13&changesize=3


1.  What is command line argument? 
according to https://www.geeksforgeeks.org/python-sys-module/ 

> Command-line arguments are those which are passed during the calling of the program along with the calling statement. To achieve this >using the sys module, the sys module provides a variable called sys.argv. It’s main purpose are:
>1. It is a list of command-line arguments.
>2. len(sys.argv) provides the number of command-line arguments.
>3. sys.argv[0] is the name of the current Python script.

I used sys module to take the secong argument from command line (that should be text file)
then I open it and read
then use .count() to count number of e's
