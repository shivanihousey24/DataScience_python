# # print statement
# print("HELLO WORLD")


# # hello this is keyword python
# """HIIII
# hiii
# hello
# namaste"""

# # variable defined
# name="shivani"
# age=23
# print("i am ",name, "and my age is ",age, "year old")

# name="saloni"
# print(type(name))

# # declare data type
# a=5
# print(a,type(a))
# a=5.8
# print(a,type(a))
# a=5+10j
# print(a,type(a))
# a="shivani"
# print(a,type(a))
# a=["shivani","sumit","saloni"]
# print(a,type(a))
# a=("shivani","saloni","sumit")
# print(a,type(a))
# a={"name":"saloni","age": "18"}
# print(a,type(a))
# a=True
# print(a,type(a))
# a=None
# print(a,type(a))
# a=frozenset({"apple","banana","cherry","apple"})
# print(a,type(a))
# a=bytearray(5)
# print(a,type(a))

#  #operators 
# print("10+15 = ",10+15)
# print("10-15 = ",10-15)
# print("10*15 = ",10*15)
# print("10/15 = ",10/15)
# print("10%15 = ",10%15)
# print("10//15 = ",10//15)
# print("10**15 = ",10**15)
# print("10+18 = ",10+18)

# # assignment operators
# x=10
# print(x)
# x+=5
# print(x)
# x-=5
# print(x)
# x*=10
# print(x)
# x/=10
# print(x)
# x//3
# print(x)
# x**5
# print(x)
# x=5
# x%=3
# print(x)
# x|=2
# print(x)
# x^=3
# print(x)

# # camparison operation
# a=10
# b=5
# print("a==b:",a==b)
# print("a!=b:",a!=b)
# print("a>=b:",a>=b)
# print("a<=b:",a<=b)
# print("a>b:",a>b)
# print("a<b:",a<b)

# # logical operators
# x=5
# print(x<10 and x<15)
# print(x<5 or x<10)
# print(not(x<5 and x<10 ))

# # identity operators
# y=10
# print(x is y)
# print(x is not y)

# x=["maruti","BMW"]
# y=["maruti","BMW"]
# z=x
# print(x is y)
# print(x is not y)
# print(y is x)
# print(y is not x)

# print("BMW" in x)
# print("BMW" not in x)
# print("saloni" in x)
# x=10
# y=20
# print(x & y)
# print(x | y)
# print(x ^ y)
# print(~x)
# print( ~y)
# print(x << 2)
# print(x >> 2)
# print(y << 2)
# print(y >> 2)

# name=input("enter your name ")
# age=input("enter your age ")
# email=input("enter your email ")
# mo_no=input("enter your mo_no ")
# print("hii my name is",name,"and i am currently", age, "year old and my email is",email, "then my contact number is",mo_no)
# a="12"
# b=int(a)
# print(b,type(b))

# a=10
# b="hello"
# print(a+b)

# p=5
# b=6
# h = (p**2) + (b**2) ** 0.5
# print(h)
# basic code
# print("+-------+")
# print("|       |")
# print("|       |")
# print("|       |")
# print("|       |")
# print("|       |")
# print("+-------+")

# print("+" + "-"*10 +"+")
# print(("|" + " " * 10+ "|\n") * 5, end="")
# print("+" + "-"*10 +"+")
# multiple code covert single line code
# print(("+" + "-"*10 +"+\n")+(("|" + " " * 10 + "|\n") * 5)+("+" + "-"*10 +"+"))
# name="shivani"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[-1]) # negative slicing
# print(name[-2])
# print(name[-3])
# print(name[-4])
# print(name[-5])
# print(name[-6])
# print(name[-7])

# var=0
# print(var==0)
# var=2
# print(var==1)
# if else elif statement
# num1=int(input("enter your first number : "))
# num2=int(input("enter your second number : "))
# # if num1>num2: larger_number=num1
# # else:
# #     larger_number=num2
    
# # print("the largest number is : ", larger_number)
# largest_number=max(num1,num2)
# lowest_number=min(num1,num2)
# print("The largest_number is : ",largest_number)
# print("The lowest_number is : ",lowest_number)
# #loop statement 
# while False:
#     print("Hiii i am shivani")

# num=int(input("enter your number"))
# even_num=0
# odd_num=0 
# while num!=0:
#     if num%2==0:
#         even_num+=1
#     else:
#         odd_num+=1
#     num=int(input("enter your number"))
# print ("Even numver : ",even_num)
# print("odd number : ",odd_num)

# for counter in range(100):
#     print("counter :",counter)
    
# for counter in range(5,-9):
#     print(counter)


# conditon false hone ke bad else print hoga 
# counter=1
# while counter>-5:
#     print(counter)
#     counter-=1
# else:
#     print("else:",counter)

# list started
# num=[1,4,7,5,"shivani",True,(1,2,3)]
# print(type(num))
# print("original list content : ",num)
# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# print(num[4])
# print(num[5])
# print(num[-1]) # list index negative 
# print(num[-2])
# print(num[-3])
# print(num[-4])
# num[1]=num[5]
# print("new list conntent : ",num)
# print(len(num))
# del num[2] #delete a array in list
# print(num)
# print(len(num))
# num1=""
# print(num1)

# my_list= [1,2,3,4,5]
# print("current list :",my_list)
# print(len(my_list))
# my_list[len(my_list/2)]
# print(my_list)
# # my_list[2]=int(input("enter by user"))
# # print(my_list)

hat_list=[1,2,3,4,5]
var=int(input("enter an integer to the middle element"))
hat_list[int(len(hat_list)//2)]=var
print(hat_list)
print(hat_list.pop())

print("hii")