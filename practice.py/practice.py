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

# camparison operation
# a=10
# b=5
# print("a=10 & b=5 a==b:",a==b)
# print("a=10 & b=5 a!=b:",a!=b)
# print("a=10 & b=5 a>=b:",a>=b)
# print("a=10 & b=5 a<=b:",a<=b)
# print("a=10 & b=5 a>b:",a>b)
# print("a=10 & b=5 a<b:",a<b)

# " and or not is a reservd keyword but used in operator "

# logical operators
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
# x=10
# y=20
# print(x is y)   # False

# print("BMW" in x)
# print("BMW" not in x)
# print("saloni" in x)

# bitwise operator
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

# a="shivani"
# print(a.encode())
# text="hello python world"
# print(text.replace('python','AI'))

# csv='shivani,23,indore,Engineer'
# parts=csv.split(',')
# print("parts :",parts)
# print(parts[0])
# rejoined=','.join(parts)
# print("rejoined :",rejoined)

# #check conteent
# print("hello123".isalnum())
# print("hello123*".isalnum())
# print("12345".isdigit())  #all digit print
# print("python".isalpha()) # all alphabet print and output True
# print(" ".isspace())        # space print 

# #staert/end check
# email="shivani@gmail.com"
# print(email.endswith("com"))
# print(email.startswith("shi"))

# name,marks,rank='Anita',56.89,2
# print(name,marks,rank)
# print(f'hello,{name}!')

# #format number
# print(f'marks:{marks:.2f}')
# print(f'marks:{marks:.0f}')
# print(f'count:{100000:,}')

# # padding and alignment
# print(f'{name:<2}|{marks:>8.2f}|Rank:{rank}')

# # expression inside {}
# price,gst=500,0.18
# print(f'price:RS.{price} |gst:RS.{price*gst:.2f}|total:rs.{price*(1+gst):.2f}')

# var=0
# print(var==0)
# var=2
# print(var==1)
# if else elif statement

# num1=int(input("enter your first number : "))
# num2=int(input("enter your second number : "))
# if num1>num2: 
#     larger_number=num1
# else:
#     larger_number=num2
    
# print("the largest number is : ", larger_number)

# num1=int(input("enter your first number : "))
# num2=int(input("enter your first number : "))
# num3=int(input("enter your first number : "))
# largest_number=num1
# if num2>largest_number:
#     largest_number=num2
# if num3>largest_number:
#     largest_number=num3
# print("largest number :",largest_number)

# largest_number=max(num1,num2)
# lowest_number=min(num1,num2)
# print("The largest_number is : ", largest_number)
# print("The lowest_number is : ", lowest_number)
#loop statement 
# while False:
#     print("Hiii i am shivani")
# largest_number=-999999999
# num=int(input("enter a num or tyupe -1 to stop :"))
# while num !=-1:
#     if num>largest_number:
#         largest_number=num
#     num=int(input("enter a num or tyupe -1 to stop :"))
# print("the largwest number is :",largest_number)

# num=int(input("Enter your number"))
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
 
    
# for counter in range(5,10):
#     print(counter)


# exit=1
# while exit !=0:
#     exit=int(input("Enter number :"))
#     print(exit)

# for counter in range(2,1):
#      print(counter)
# power=1
# for expo in range(16):
#     print("2 the power of",expo,"=",power)
#     power *=2
        
# power=1
# for expo in range(16):
#     print("2 the power of",expo,"=",power)
#     power *=2 
#     if expo==7:
#         break  
# print("---------NOW I AM OUT----------") 
# power=1
# for expo in range(16):
#     if expo ==7:
#         continue
#     print("2 the power of",expo,"=",power)
#     power *=2
# print("---------NOW I AM OUT----------") 

# for counter in range(1,6):
#     if counter==3:
#         break
#     print(counter)
    
# for counter in range(1,6):
#     if counter==3:
#         continue
#     print(counter)

# largest_num=-99999
# counter=0
# while True:
#     num=int(input("Enter your num :"))
#     if num==-1:
#         break
#     counter+=1
#     if num>largest_num:
#         largest_num=num
# if counter!=0:
#     print(largest_num)
# else:
#     print("you haven't enter any num :")
    
# counter=1
# while counter>-5:
#     print(counter)
#     counter-=1
# else:
#     print("else:",counter)
'''
truthy : 1,2,3,-1,-20,"a","hello",[1,2,3],{1,2}
falsy : 0,{},[],(),none,NULL
list adress are refrence number 
'''

# i=1
# j=not not i
# print(i)
# print(j)

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

# a=10
# print(id(a))
# print(hex(id(a)))

# my_list= [10,20,30,40,50,60,70,80,90,100]
# sum_list=(sum(my_list))
# print(sum_list)

# my_list=[10,20,30,40,50,60,70,80,90,100]
# sum=0
# for index in range(len(my_list)):
#     sum += my_list[index]
# print("sum : " ,sum)

#  a variable copy with use third variable
# a=10
# b=100
# print(a)
# print(b)
# temp=b
# b=a
# a=temp
# print(a)
# print(b)

# a variable copy without use third variable
# a=10
# b=20
# a,b=b,a
# print("a :",a)
# print("b :",b)

# list swap
# my_list=[1,2,3,4]
# print(my_list)
# my_list[0],my_list[1]=my_list[1],my_list[0]
# my_list[2],my_list[3]=my_list[3],my_list[2]
# print(my_list)

# lst=[1,2,3,4,5]
# lst2=[]
# add=0
# for number in lst:
#     add += number
#     lst2.append(add)
# print(lst2)
# print(lst)

# lst=[]
# del lst
# print(lst)
'''
is called dry run
'''

# bubble  sort best case
''' DRY RUN
index       index_inner     current list  
0               0           [8,10,6,2,4]
                1           [8,6,10,2,4]
                2           [8,6,2,10,4]
                3           [8,6,2,4,10]
                .
                .
                .
4                           [2,4,6,8,10]
'''

#arr=[8,10,6,2,4]
# arr=[1,2,3,4,5]
# print(arr)
# count=0
# swapped=False
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1-i):
#         count += 1
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#             swapped=True
#     if not swapped:
#         break
# print(arr)
# print(count)

# while loop implement
# my_list=[8,10,6,2,4]
# swapped=True
# count=0
# while swapped:
#     swapped=False
#     for i in range(len(my_list)-1):
#         count += 1
#         if my_list[i]>my_list[i+1]:
#             swapped=True
#             my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
# print(my_list)
# print(count)

# merge sort 
# arr2=[2,4,7,0,9,3,8,1,5,6]
# for i in range(len(arr)-1):
# insertion sort
# selction sort
# quick sort
# radix sort
# heap sort
# shall sort

# its a reverse method
# my_list=[10,6,8,4,2]
# print(my_list)
# for i in range(len(my_list)//2):
#     my_list[i],my_list[-1*(i+1)]=my_list[-1*(i+1)],my_list[i]
# print(my_list)

# my_list=[10,6,8,4,2]
# my_list.reverse()
# print(my_list)
# my_list.sort()
# print(my_list)

# lst=["a","b","G","B"]
# lst.sort()
# print(lst)

# a=45
# b=56
# lst=[a,b]
# lst.sort()
# print(lst)
# a="A"
# b="B"
# c=" "
# lst=[a,b,c]
# lst.reverse()
# print(lst)

# list_1=[1]
# list_2=list_1
# list_1[0]=2
# print(list_2)

# list_1=[1,2,3,4,5]
# list_2=list_1[1:]
# list_1[0]=2
# print(list_2)
# print(list_1)

# list_2=[1,2,3]
# a=list_2[2:4]
# print(a)
# lst=list_2[-1:1]
# print(lst)

# myList=[10,4,6]
# del myList
# print(myList)

# myList=[1,2,2,4]
# print(5 in myList)
# print(5 not in myList)

# myList=[17,3,11,5,1,9,7,15,13]
# largestNumber=17
# for i in range(myList):
#     if largestNumber>i:
#         print(myList)

# find largest number
# myList=[17,3,11,5,1,9,7,15,13]
# max_value=myList[0]
# for num in myList:
#     if num>max_value:
#         max_value=num
# print(max_value)

# even number
# lst=[1,2,3,4,5,6,7,8,8,10]
# for i in range(len(lst)):
#     if i%2==0:
#         print("even number",i)
        
#  search 5
# mylst=[17,3,11,5,1,9,7,15,13]
# findElement=mylst[3]
# for num in mylst:
#     if num==findElement:
#         findElement=num
# print(findElement)
# 2nd method
# for index in range(len(mylst)):
#     if mylst[index]==5:
#         print(index)
#         break

# list=[1,2,3,4]
# print(list)
# list.append(6)
# print(list)
# print("length of list :",len(list))
# list.insert(2,7)
# print(list)
# print("length of list :",len(list))


# lst=[10,20,30,40,50,60,70,80,90,100]
# for index in range(len(lst)):
#     lst[index]=lst[index] + 1
# print(lst)

# lst=[10,20,30,40,50,60,70,80,90,100]
# sum=0
# for index in range(len(lst)):
#     sum += lst[index]
# print(sum)

# lst=[10,20,30,40,50,60,70,80,90,100]
# index=0
# for i in lst:
#     print("lst [",index,"] = ",i)
#     index+=1



# lst=[1,2,3,5,6,7,5,4]
# index=0
# while index<len(lst):
#     print(lst[index])
#     index+=1

#Empty list insert 1 to 10 
# list=[]
# for i in range(81,101):
#     list.append(i)
# print(list)


# list comprehesion
# row=[] # basic method
# for i in range(8):
#     row.append("WHITE_PAWN")
# print(row)

# #  list comprehesion use
# row=["WHITE_POWN" for i in range(8)]
# print(row)

# squares=[x ** 2 for x in range(11)]
# print(squares)

# twos=[2 **i for i in range(11)]
# print(twos)

# odds=[x for x in squares if x % 2 != 0]
# print(odds)

# even=[x for x in squares if x % 2 == 0]
# print(even)

# board=[]
# for i in range(8):
#     row=["EMPTY" for i in range(8)]
#     board.append(row)
# print(board)

# board[0][0]="Rook"
# board[0][7]="Rook"
# board[7][0]="Rook"
# board[7][7]="Rook"

# board[0][1]= "Knight"
# board[0][6]= "Knight"
# board[7][1]= "Knight"
# board[7][6]= "Knight"

# for i in range(len(board)):
#     print(board[i])


# temps=[[0.0 for i in range(24)] for j in range(31)]

# random=[20, 34,56,20,66,20, 34,56,20,66,20, 34,56,20,66,20, 34,56,20,66,-6, 34,56,20,66,20, 34,56,20,66,10]
# print(len(random))

# for index in range(len(temps)):
#     temps[index][11]=random[index]
    
# for index in range(len(temps)):
#     print(temps[index])
    
# sum=0
# for index in range(len(temps)):
#     sum += temps[index][11]
    
# print(sum/31) 

# highest=0
# for index in range(len(temps)):
#     for inner_index in range(len(temps[index])):
#         if highest < temps[index][inner_index]:
#             highest= temps[index][inner_index]
# print(highest)

# lowest=0
# for index in range(len(temps)):
#     for inner_index in range(len(temps[index])):
#         if lowest > temps[index][inner_index]:
#             lowest= temps[index][inner_index]
# print(lowest)


rooms=[[[False for r in range(20)] for f in range(15)] for t in range(3)]
for building_index in range(len(rooms)):
    print("Bulding" , building_index +1)
    for floor_index in range(len(rooms[building_index])):
        print("floor :" , floor_index +1)
        for rooms_index in range(len(rooms[building_index][floor_index])):
            print("rooms :" , rooms_index +1)
print(rooms[building_index][floor_index][rooms_index])