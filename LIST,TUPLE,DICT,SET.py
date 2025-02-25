    
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










