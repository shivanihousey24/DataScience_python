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
for i in range(1,101):
    if i%3==0 and i%5 == 0:
        print(i)
        
# Write a program to replace numbers divisible by 3 with "Fizz".

# Write a program to replace numbers divisible by 5 with "Buzz".
# Write a program to replace numbers divisible by both 3 and 5 with "FizzBuzz".
# 🔢 Number-Based Logic
# Write a program to check whether a number is prime or not.
# Write a program to print all prime numbers between 1 and 50.
# Write a program to find the factorial of a number using a loop.
# Write a program to check whether a number is a palindrome.
# Write a program to reverse a number using a loop.
# Write a program to find the sum of digits of a number.
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