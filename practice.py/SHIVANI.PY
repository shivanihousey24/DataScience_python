# 🔰Basic Loop Questions
# Write a program to print the first 10 natural numbers using a for loop. Each number should be printed on a new line.
# for i in range(11):
#     print(i)

# # Write a program to print numbers from 10 to 1 using a for loop. Each number should be printed on a new line.
# for count in range(10,0,-1):
#     print(count)

# # Write a program to print all even numbers between 1 and 50 using a for loop.
# for i in range(0,50,2):
#     print(i)

# # Write a program to print all odd numbers between 1 and 50 using a for loop.
# for i in range(1,50,2):
#     print(i)

# Write a program to calculate the sum of the first 10 natural numbers using a for loop.
# for i in range(10):
    
# Write a program to display the multiplication table of a given number using a for loop.
# num=int(input("enter your number :"))
# for i in range(1,11):
#     mul=num*i
#     print(num,"*",i,"=", mul)

# Write a program to print all numbers between 1 and 100 that are divisible by 5.
# for i in range(1,101):
#     if i % 5==0:
#         print(i)

# Write a program to count how many numbers between 1 and 100 are divisible by 3.
# sum=0
# for i in range(1,100):
#     if i%3 == 0:
#         sum += 1
# print(sum)
    
# Write a program to print the square of numbers from 1 to 10.
# for i in range(1,11):
#     print("square of :",i,"=",i**2)    
# Write a program to print the cube of numbers from 1 to 10.
# for i in range(1,11):
#     print("cube are :",i,"=",i**3) 
  
# 🔁 IF-ELSE with Loop

# Write a program to check whether each number in a given range is even or odd.
# start=int(input("Enter your number :"))
# end=int(input("enter youe number :"))
# for i in range(start, end):
#     if i%2==0:
#         print("number",i,"is even")
#     else:
#         print("number",i," is odd")

# Write a program to print only positive numbers from a list using a loop.
# myList=[1,-3,5,-7,-4,2,4,-8]
# for num in myList:
#     if num>0:
#         print(num,"number is positive")

# Write a program to print only negative numbers from a list using a loop.
# myList=[1,-3,5,-7,-4,2,4,-8]
# for num in myList:
#     if num<0:
#         print(num,"num is negative")

# Write a program to count even and odd numbers in a list.
# lst=[1,2,3,4,5,6,7,8,9,10,12]
# even_count=0
# odd_count=0
# for num in lst:
#    if num%2==0:
#        even_count+=1
#    else:
#        odd_count+=1
# print(even_count,"num is even")
# print(odd_count,"num is odd")
      
# Write a program to find the largest number in a list using a loop.
# lst=[1,2,3,56,78,234]
# largest=lst[5]
# for num in lst:
#     if num>largest:
#         largest=num
# print("largest number is :",largest)

# Write a program to find the smallest number in a list using a loop.
# lst=[23,4,56,78,2,1,89]
# smallest=lst[5]
# for num in lst:
#     if smallest>num:
#         smallest=num
# print("smallest number is :",smallest)

# Write a program to print numbers divisible by both 3 and 5 between 1 and 100.
# for i in range(1,101):
#     if i%3==0 and i%5 == 0:
#         print(i)
        
# Write a program to replace numbers divisible by 3 with "Fizz".
# for i in range(1,10):
#     if i%3==0:
#         i="Fizz"
#     print(i)

# Write a program to replace numbers divisible by 5 with "Buzz".
# for i in range(1,11):
#     if i%5==0:
#         i="Buzz"
#     print(i)

# Write a program to replace numbers divisible by both 3 and 5 with "FizzBuzz".
# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         i="FuzzBuzz"
#     print(i)

# 🔢 Number-Based Logic
# Write a program to check whether a number is prime or not.
# num=int(input("Enter your num :"))
# if num <=1:
#     print("NOT PRIME")
# else:
#     for i in range(2,num):
#         if num % i== 0:
#             print("NOT PRIME")
#             break
#     else:
#             print("PRIME")

# Write a program to print all prime numbers between 1 and 50.
# for num in range(1,50):
#     for i in range(2,num):
#         if num % i ==0:
#             break
#     else:
#         print(num,end=" ")

# Write a program to find the factorial of a number using a loop.
# num = int(input("Enter a number: "))

# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print("Factorial of", num, "is", fact)

# Write a program to check whether a number is a palindrome.


# Write a program to reverse a number using a loop.
# my_list=[10,6,8,4,2]
# print(my_list)
# for i in range(len(my_list)//2):
#     my_list[i],my_list[-1*(i+1)]=my_list[-1*(i+1)],my_list[i]
# print(my_list)

# Write a program to find the sum of digits of a number.
# num = [1,1,45,55,34,23]
# sum=0
# for index in num:
#     sum +=index
# print(sum)

# Write a program to count the number of digits in a number.

# Write a program to check whether a number is an Armstrong number.
# Write a program to check whether a number is a perfect number.
# Write a program to generate Fibonacci series up to N terms.
# 🧠 List + Loop + IF-ELSE
# Write a program to print all elements of a list using a loop.

# Write a program to print elements at even index positions in a list.
# Write a program to print elements at odd index positions in a list.
# Write a program to count occurrences of a number in a list.
# Write a program to remove duplicate elements from a list without using set.
# Write a program to reverse a list using a loop.
# Write a program to find the sum of all elements in a list.
# Write a program to find the average of elements in a list.
# Write a program to merge two lists using a loop.
# Write a program to find common elements between two lists.

'''
# simple calculator
print("1 = Add     2 = Sub     3 = Mul     4 Div")
choice=int(input("enter select 1 to 4 choice : "))
a=int(input("Enter your num :"))
b=int(input("Enter your num :"))
if choice==1:
    print(a,"+",b,"=",a+b)
elif choice==2:
    print(a,"-",b,"=",a-b)
elif choice==3:
    print(a,"*",b,"=",a*b)
elif choice==4:
    print(a,"/",b,"=",a/b)
else:
    print("envalid error")'''
    
'''
here once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
Your task is to:
(Step 1) write a line of code that prints the length of the existing list 
(Step 2)write a line of code that removes the last element from the list 
(Step 3)write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user 
'''
# # program:-
# lst=[1,2,3,4,5]
# lengthOfList=len(lst)
# print(lengthOfList)     # step 1

# del lst[len(lst)-1]
# print(lst)               # step 2

# lst[2]=int(input("Enter your num :"))
# print(lst)               #step 3

# list comprehension.
# 1.Create a list of numbers from 1 to 10 using list comprehension.
lst=[x for x in range(1,10)]
print(lst)
# 2.Create a list of squares of numbers from 1 to 10.
squares=[x ** 2 for x in range(1,11)]
print(squares)
# Output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 3.Create a list of cubes of numbers from 1 to 10.
cube=[x ** 3 for x in range(1,11)]
print(cube)
# 4.Create a list of all even numbers between 1 and 50.
even=[x for x in range(1,51) if x % 2 ==0]
print(even)
# 5.Create a list of all odd numbers between 1 and 50.
odd=[x for x in range(1,51) if x % 2 !=0]
print(odd)
# 6.Create a list containing numbers divisible by 3 een 1 and 100.
divBy3=[x for x in range(1,101) if x % 3 ==0]
print(divBy3)
# 7.Create a list containing numbers divisible by 5 between 1 and 100.
divBy5=[x for x in range(1,101) if x % 5 ==0]
print(divBy5)
# 8.Given: numbers = [10, 15, 20, 25, 30] Create a new list by adding 5 to every element.
numbers = [10, 15, 20, 25, 30]
num=[x + 5 for x in numbers]
print(num)
# 9.Given: numbers = [1,2,3,4,5] Multiply every element by 10.
numbers = [1,2,3,4,5]
num=[x + 10 for x in numbers]
print(num)
# 10.Given:names = ["ram", "shyam", "mohan"] Convert all names to uppercase.
names = ["ram", "shyam", "mohan"]
name=[names.upper() for names in names]
print(name)
# 11.Given:words = ["Python","Java","C","HTML"] Convert all words to lowercase.
words = ["Python","Java","C","HTML"]
worlds=[words.lower() for words in words]
print(worlds)
# 12.Given:numbers = [2,5,8,11,14,17] Create a list containing only even numbers.
numbers = [2,5,8,11,14,17]
num=[x for x in numbers if x % 2 ==0]
print(num)
# 13.Given:numbers = [2,5,8,11,14,17] Create a list containing only odd numbers.
numbers = [2,5,8,11,14,17]
num=[x for x in numbers if x % 2 !=0]
print(num)
# 14.Given:numbers = [10,-5,6,-2,9,-7] Create a list containing only positive numbers.
numbers = [10,-5,6,-2,9,-7]
num=[x for x in numbers if x>0]
print(num)
# 15.Given:numbers = [10,-5,6,-2,9,-7] Create a list containing only negative numbers.
numbers = [10,-5,6,-2,9,-7]
num=[x for x in numbers if x<0]
print(num)
# 16.Create a list of all prime numbers between 1 and 100 using list comprehension.
#primeNum=[x for x in range(1,101) if x % ]
# 17.Given:sentence = "Python Programming" Create a list of all characters except spaces.
sentence = "Python Programming"
str=[ch for ch in sentence if ch !=" "]
print(str)
# 18.Given:words = ["apple","banana","cat","dog","elephant"] Create a list containing only words whose length is greater than 3.
words = ["apple","banana","cat","dog","elephant"]
word=[ch for ch in words if len(ch)> 3 ]
print(word) 
# 19.Given:numbers = [1,2,3,4,5,6,7,8,9,10] Create a new list where:
# Even numbers → Square
# Odd numbers → Cube
numbers = [1,2,3,4,5,6,7,8,9,10]
squares=[x**2 for x in numbers if x % 2==0]
cube=[x**3 for x in numbers if x % 2 !=0]
print(squares,cube)
# Example: [1,4,27,16,125,36,343,64,729,100]
# 20.Given:names = ["ram","shyam","mohan","sohan"]
# Create a list like:
# ['Hello Ram',
#  'Hello Shyam',
#  'Hello Mohan',
#  'Hello Sohan']
names = ["ram","shyam","mohan","sohan"]
name=["Hello" + name.capitalize() for name in names ]
print(name)

# FUNCTION
# 1.Write a function to print "Hello World".
# 2.Write a function to print your name.
# 3.Write a function that takes a number as an argument and prints its square.
# Example:
# Input: 5
# Output: 25
# 4.Write a function to print the sum of two numbers.
# 5.Write a function to print the maximum of two numbers.
# 6.Write a function to check whether a number is even or odd.
# 7.Write a function to check whether a number is positive, negative, or zero.
# 8.Write a function to check whether a number is prime or not.
# 9.Write a function to print all prime numbers between 1 and N.
# 10.Write a function to calculate the factorial of a number.
# 11.Write a function to calculate the sum of digits of a number.
# Example:
# Input: 1234
# Output: 10
# 12.Write a function to count the number of digits in a number.
# 13.Write a function to reverse a number.
# Example:
# Input: 1234
# Output: 4321
# 14.Write a function to check whether a number is a palindrome.
# Example:
# 121 → Palindrome
# 123 → Not Palindrome
# 15.Write a function that takes a list and returns the largest element.
# 16.Write a function that takes a list and returns the smallest element.
# 17.Write a function that takes a list and returns the sum of all elements.
# 18.Write a function that counts the number of vowels in a string.
# Example:
# Input: "Python Programming"
# Output: 4
# 19.Write a function that returns the second largest element in a list.
# Example:
# Input: [10, 20, 5, 40, 30]
# Output: 30
# 20.Write a function that checks whether a string is an anagram of another string.
# Example:
# Input:
# listen
# silent
# Output:
# Anagram