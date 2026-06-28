'''Question number 1
Write a program that utilizes the concept of conditional execution, takes a string as input, and:
prints the sentence "Yes - Spathiphyllum is the best plant ever!" 
to the screen if the inputted string is "Spathiphyllum" (upper-case)prints "No, I want a big Spathiphyllum!" 
if the inputted string is "spathiphyllum" (lower-case)prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.'''
# solve:-
plants_name=input("enter a plants name : ")
if plants_name=="Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!" )
elif plants_name=="spathiphyllum":
    print("No, I want a big Spathiphyllum!" )
else:
    print("Spathiphyllum NOT",plants_name)
''' Quesytion number 2  
Once upon a time there was a land a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
if the citizen's income was not higher than 85,528 thalers, 
the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.
It should accept one floating-point value: the income.Next, 
it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for youNote: 
this happy country never returned any money to its citizens. If the calculated tax was less than zero, 
it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.'''
# solve:-
income=float(input("enter a income number :"))
if income<=85528:
    tax=(income*0.18)-556.02
else:
    tax=14839.02+(0.32(income-85528))
    if tax<0:
         tax=0
tax=round(tax)
print(tax)
'''Question number 3
As you surely know, due to some astronomical reasons, years may be leap or common. 
The former are 366 days long, while the latter are 365 days long.
Since the introduction of the Gregorian calendar (in 1582), 
the following rule is used to determine the kind of year:
if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.Look at the code in the editor it only reads a year number, 
and needs to be completed with the instructions implementing the test we've just described.
The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period.'''
# solve:-
blocks=int(input("enter your blocks :"))
counter=0
while(blocks-counter>0):
    counter+=1
    blocks=blocks-counter
    print(f'height of the pyramid :{counter}')
'''Practice Question number 4 
The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.'''
# solution:-
beatles=[] # step 1 
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Add 3 member of the band :",beatles) # step 2
for i in range(2):
    name=input("Enter your Name :")
    beatles.append(name)
print("Add 2 member of the band :",beatles) # step 3
del beatles[3]
print("Remove stu sutcliffe :",beatles)
del beatles[3]
print("Remove pete best :",beatles) # step 4
beatles.insert(0,"Ringo")
print("final list :",beatles) #  step 5