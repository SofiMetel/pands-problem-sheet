# pands-problem-sheet

#week 01 - created helloworld.py and pushed to GitHub

#week 02 - bank.py

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

#week 03 - accounts.py
Weekly Task 03
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
```
$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
```

#week 03  EXTRA task - extraaccounts.py

TASK: Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

My assumption is that in some banks can exist bank accounts numbers with more than 10 digits (i.e. IBAN = 22 digits or 34 digits)
In any way we want to show only the last 4 characters. 



