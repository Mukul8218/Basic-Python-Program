'''
                                                                                      #Functional Programming#
#------------------------------------------------------------------UDF:-User Define Functions---------------------------------------------------------#
#Function:-A function is a block of statements that perform a specific task and return a value.

#we will use def keyword to define a function.

Syntax:-
def function_name(argument):
          definition

function_name(parameter)          

#-----------------------------------------------------------
def func1():
    print("i am function1")

func1()
#-----------------------------------------------------------
def add():
    a=int(input("enter a number: "))
    b=int(input("enter b number: "))
    c=a+b
    print("addition:",c)
add()
#-------------------------------------------------------------
def add(x,y):
    c=x+y
    return c
    
a=int(input("enter a number: "))
b=int(input("enter b number: "))
print(add(a,b))    

#WAF to check an entered number is prime or not.

def checkprime(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        return "Prime"
    else:
        return "Not Prime"
    
print(checkprime(18))    

#---------------------------------------------------------------------

def checkprime(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False
    
for i in range(1,101):
    if(checkprime(i)):
        print(i,end=" ")

#--------------------------------------------------------------------
#WAF to calculate the sum of all elements in a list.
def addlist(li):
    return sum(li)

a=[2,3,4,5,6]

print(addlist(a))

#WAF to find factorial of a number.
import math

def Fact(num):
    return math.factorial(num)

print(Fact(5))

#WAF to find the maximum of three numbers.
def findmax(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3

print(findmax(5,6,8))

#WAF to reverse a string
def revstr(st):
    return st[::-1]

print(revstr("mukul"))

#WAF to check a number is perfect square
def checkperfect(num):
    i=1
    while(i*i<=num):
        if(i*i==num):
            return "Perfect Square"
        i+=1
    return "Not Perfect Square"

print(checkperfect(9))

#WAF to find GCD/HCF of two numbers.
def findhcf(num1,num2):
    hcf=1
    for i in range(2,num1+1):
        if(num1%i==0 and num2%i==0):
            hcf=i
    return hcf

print(findhcf(12,10))
#WAF to check if a number is palondrome or not.
'''
def palondrome(str):
    a=input("enter string: ")
    b=a[-1::1]
    if b==a:
        print("string is paliondrome")
    else:
        print("string is not paliondrame")
        return str
    
print(palondrome("mukul"))










