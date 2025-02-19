'''                                                           #CONDITIONAL STATEMENT#

#WAP to calculate gross salary of an employ where hra is 20% da is 30% of basic
bs=float(input("enter basic salary: "))
if (bs>25000):
    hra=bs*20/100
    da=bs*30/100
else:
    hra=bs*25/100
    da=bs*35/100
gs=bs+hra+da
print("GROSS SALARY:",int(gs))

#WAP to check a number is ABSTRACT or not.
#hint:- a number which is fully divisible by 7 or a number which has last digit is 7
num=int(input("enter number: "))
if(num%7==0)or(num%7==7):
    print("ABSTRACT")
else:
    print("not abstract")

#WAP a programe that check if a number is even or odd.
num=int(input("enter number: "))
if(num%2==0):
    print("even")
else:
    print("odd")
    
#WAP to determine whether a person is eligible to vote (age >=18)or not.
age=int(input("enter age: "))
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")

#WAP that asks for a user's score and prints "pass" if score is 40 or above, otherwise prints "fail".
score=int(input("enter score: "))
if(score>=40):
    print("pass")
else:
    print("fail")
    
#WAP to check whether a given year is a leap year or not.
num=int(input("enter number: "))
if(num%4==0):
    print("leap year")
else:
    print("normal year")

a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
if(a>b):
    print("a is larger")
else:
    print("b is larger")

#WAP that takes a temperature as input and prints whether its cold (<=15c)warm(16-30c)or hot(>30c)
whether=int(input("enter the temperature: "))
if(whether<=15):
    print("its cold ")
elif(whether<=30):
    print("its warm")
else:
    print("its hot")

# write a program that calculates a person income tax based on these conditions:
#income<=50000 no tax,income 50001-100000:10%tax,income>100000:20%tax
income=int(input("enter the income: "))
if(income<=50000):
    print("NO TAX")
elif(income<=100000):
    print(income*10/100)
else:
    print(income*20/100)
                                                                                           #looping question FOR &WHILE#
for s in range(1,101):
    count=0
    for a in range(1,s+1):
        if (s%a==0):
            count=count+1
    if(count==2):
        print(s)
#WAP to find factors.
num=int(input("enter the number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

num=int(input("enter the number: "))
a=0
b=1
for i in range(1,num+1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
#WAP to find hcf.
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
HCF=1
for i in range(1,num1+1):
    if(num1%i==0 and num2%i==0):
        HCF=i
print(HCF)
#WAP find the sum.
num=int(input("enter the number: "))
sums=0
for i in range(1,num+1):
    sums=sums+i
print(sums)

num=int(input("enter the number: "))
sums=0
mul=1
while(num>0):
    rem=num%10
    sums=sums+rem
    mul=mul*rem
    num=num//10
if(sums==mul):
    print("ARMSTRONG")
else:
    print("NOT ARMSTRONG")
#WAP number is armstrong.
num=int(input("enter the number: "))
copy=num
sums=0
while(num>0):
    rem=num%10
    sums=sums+rem**3

    num=num//10
if(sums==copy):
    print("ARMSTRONG")
else:
    print("NOT ARMSTRONG")

num=145
copy=num
sums=0
while(num>0):
    rem=num%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sums=sums+fact
    num=num//10
if(sums==copy):
    print("armstrong")
else:
    print("not arm")

#WAP to find prime.
num=int(input("enter the number"))
for i in range(1,num+1):
    if(i%2==0):
        print(i,end=" ")
        
                                                                                          #WAP use nested loop.
for a in range(1,6):
    for b in range(5,a,-1):
        print(" ",end="")
    for b in range(1,a+1):
        print("% ",end="")
    print("")


for a in range(65,70):
    for b in range(65,a+1):
        print(chr(a),end="")
    print("")

c=65

for a in range(65,70):
    for b in range(65,a+1):
        print(chr(c),end="")
        c+=1
    print("")

c=1
for a in range(1,6):
    for b in range(1,a+1):
        print(c%2,end="")
        c+=1
    print("")
    

c=1
m=-1
for a in range(1,6):
    for b in range(1,a+1):
        print(c,end="")
        c=c+m
        m=m*-1
    print("")

ch=""
for a in range(1,6):
    ch=ch+str(a)
    print(ch)

s="0"
for a in range(10,0,-1):
    if(a!=10):
        s=str(a)+s+str(a)
    print(s)

                                                                                      #"*" pattern programming question.
for a in range(4,0,-1):
    for b in range(1,a+1):
        print(b,end="")
        
    print("*"*(4-a))
    
for a in range(4,0,-1):
    s=""
    for b in range(1,a+1):
        s=s+str(b)
    s=s+("*"*(4-a))
    print(s+s[::-1])
    
                                                                                           #list & tuple question# & "FOR_EACH Loop"
li=[32,45,67,8,89,35,57,87,51,46,34,24]
sums=0
for x in li:
    if(x%2==0):
        sums=sums+x
print(sums)

t=(2,3,5,7,8,9,8,76,54,3)
max=t[0]
for i in t:
    if(max<i):
         max=i
print(max)

#WAP to print only unique value from a list.
li=[2,45,7,8,6,5,4,3,2,4,5,7,8,9,3]
li2=[]
for i in li:
    if(i not in li2):
        li2.append(i)
print(li2)    

#wap to find max min num in a list.
li=[1,2,3,4,5]
max=0
for i in li:
    if(max<i):
        max=i
print(max)

#wap to reverse a list.
li=[1,2,3,4,5]
print(li[::-1])

#sum of all elements.
li=[12,34,56,32,34]
sums=0
for i in li:
    sums=sums+i
print(sums)

#count
li=[1,2,3,4,5]
count=0
for i in li:
    count+=1
print(count)

#merge to list.
li1=[1,2,3,4,5]
li2=[34,45,67,78]
li1.extend(li2)
print(li1)

#
li=[12,32,56,66,54]
li.sort(reverse=True)
print(li[1])

#WAP to check if an element exists in a list.
li=[2,4,5,6,7]
n=int(input("enter the number: "))
for i in li:
    if(i==n):
        print("exists")
        break
else:
    print("not exists")

#WAP to find the intersection of two list.
li1=[1,2,3,4,5,6]
li2=[3,43,4,65]
com=[]
for i in li1:
    if(i not in com):
        if(i in li2):
            com.append(i)
print(com)

#WAP to convert a list of tuples into a dictionary.
li=[("mukul",1),("priyanshu",2),("atul",3)]
dic=dict()
for t in li:
    dic.update({t[0]:t[1]})
print(dic)

                                                                                      #DICTIONARY Question#

#WAP to create a dictionary from two list.
li1=[12,23,45,56,67]
li2=[13,53,75,87,54]
dic=dict()
for i in range(0,len(li1)):
    dic.update({li1[i]:li2[i]})
print(dic)

#WAP to merge to dict.
dic1={"m":1,"r":2,"l":3}
dic2={"p":6,"a":8,"q":9}
dic1.update(dic2)
print(dic1)

#WAP to get a keys of a dictionary.
dic={"m":1,"r":2,"l":3,"p":4}
for keys in dic.keys():
    print(keys,end=" ")
    
#WAP to get a values of a dictionary.
dic={"m":1,"r":2,"l":3,"p":4}
for keys in dic.values():
    print(keys,end=" ")

#WAP to check if a key exists in a dictionary.
dic={"m":15,"r":27,"l":33,"p":40}
key=int(input("enter any key to find: "))
if(dic.get(key)!=None):
    print("found!")
else:
    print("not found!")

#WAP to check if a value exists in a dictionary.
dic={"m":15,"r":27,"l":33,"p":40}
value=int(input("enter any value to find: "))
if(dic.get(value)!=None):
    print("found!")
else:
    print("not found!")

# Write a Python program to remove a key from a dictionary.
dic = {'A':46,'B':89,'C':37,'D':26}
print("Your Dic : ",dic)
key = input("Enter Any Key To Delete : ")
if(dic.get(key)!=None):
    del dic[key]
    print("Your Updated Dic : ",dic)
else:
    print("Key Not Found!")

#WAP to find the max value in dic.
dic={"W":356,"M":3456,"R":325}
max=max(dic,key=dic.get)
print(max)

#WAP to sort a dict by its keys

                                                                                                   #SETS Question#
#WAP to create a set and add elements to it.
s={"mukul","ritika","atul","priyanshu"}
print(s)
s.add("prateek")
s.add("arjun")
s.add("vikas")
print("\nUpdated set= ",s)

#WAP to find the union of two sets.
s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1|s2)

#WAP to find the intersection of two sets.
s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1&s2)

#WAP to find the difference between two sets.
s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1-s2)
print(s2-s1)

#WAP to check if a set is a subset of another set.
s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1.issubset(s2))

#WAP to remove an element from a set.
s={"mukul",1,"mukku",2,3,4,"don"}
print(s)
s.remove("mukku")
print(s)

#WAP to check if an elements exists in a set.
s={'arjun', 'prateek', 'ritika', 'atul', 'vikas', 'priyanshu', 'mukul'}
value=chr("enter the sets: ")
if(s.get(value)!=None):
    print("found!")
else:
    print("not found!")

#WAP to convert a list into a set.
li=[1,2,4,56,78,65,44]
print(set(li))

#WAP to clear all elements from a set.
s1={'arjun', 'prateek', 'ritika', 'atul', 'vikas', 'priyanshu', 'mukul'}
print(s1)
s1.clear()
print(s1)

#WAP to find the symmetric diff between two sets.
s1={'arjun', 'prateek', 'ritika', 'atul', 'vikas', 'priyanshu', 'mukul'}
s2={"mukul",1,"mukku",2,3,4,"don"}
s1.symmetric_difference_update(s2)
print(s1)
'''












    
