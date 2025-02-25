                                                                                              #STRING#
#string behave like a tuple, indexing,slicing,-:(forword&backword)
#replication-:(a*3)
#string/character works on ASCII value.
#infact every character has its own ASCII value.
#to find ASCII value ord()-> ord("a")- chr()->chr(65)
#lower() upper() split()

#1 WAP to count the number of vowels  in a srting.
s="aman is a good boy"
count=0
for i in s:
    if(i in "AEIOUaeiou"):
        count+=1
print(count)

#2 WAP to check if a string is a palondrome
s="mukul"
temp=" "
for i in range(len(s)-1,-1,-1):
    temp=temp+s[i]
print(temp)
if(s==temp):
    print("palondrome")
else:
    print(" NOT palondrome")

#3 WAP to count the frequency of character in a  string.
s="werttyuiiytrew"
dic=dict()
for target in s:
   count=0
   for i in s:
         if(i==target):
             count+=1
             dic.update({target:count})
print(dic)

#4 WAP remove all spaces in the string.
s="data science and machine learning"
temp=" "
for i in s:
    if(i!=" "):
        temp=temp+i
print(temp)

#5 WAP to check two string are anagram.(listen,silent)
s1="LISTEN"
s2="SILENT"
if(sorted(s2)==sorted(s1)):
    print("ANAGRAM")
else:
    print("NOT ANAGRAM")

##
s1="mukul"
s2="priyanshu"
list1=list(s1)
list2=list(s2)
if(len(list1)==len(list2)):
    count=0
    for i in list1:
        if(i in li2 ):
            count+=1
            li2.remove(i)
    if(count==len(li1)):
        print("ANAGRAM")
    else:
        print("NOT ANAGRAM")
            
            
        
        


#6 WAP to capitalize the each letter in a string.
s="data science and machine learning"
li=s.split(" ")
st=""
for i in li:
    st=st+i[0].upper()+i[1:]+" "
print(st)

#7 WAP to reverse a each word in a string.
s="data science and machine learning"
li=s.split()
st=""
for i in li:
    st=st+i[::-1]+" "
print(st)

#8 WAP to find the longest word in a sentence.
s="data science and machine learning"
li=s.split()
st=""
maxs=li[0]
for i in li:
    if(len(i)>len(maxs)):
        maxs=i
print(maxs)

#WAP to replace all occurence of a substring in a string.
s="Data Science And Machine Learning"
st=""
for i in s:
    if(i!="e" ):
        st=st+i
    else:
        st=st+"$"
print(st)

#WAP to count a number of a string.
s="Data Science And Machine Learning"
li=s.split()
print(len(li))













    
