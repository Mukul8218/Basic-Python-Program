                                                                                 #FILE_HANDLING#
#FILE=two type
#1=text_file  |  2=binary_file

#----Syntax:>TEXT_FILE----------------------------------------
file=open("file_name.extension","mode")
file.write(data)
file.read()
file.close()
#Mode->r,w,a,r+,w+,a+
#---------------------------------------------------------

file=open("addition.txt","a")
file.write("hello india\n")

file.close()


file=open("addition.txt","r")
print(file.read())
file.close()

#NOTE-> they are use [.read , .readlines]


#--------------Binary File------------------------
import pickle
file=open("std.dat","ab")
pickle.dump("hello india",file)
file.close()

import pickle

file=open("std.dat","rb")
data=pickle.load(file)
print(data)
file.close()

#------------------Exception /Error-----------------------------

1-Syntax Error(compile time error [can not be handled])
2-Logical Exception / Error(Runtime error[can be handled])

#-------------------Exception Handling---------------------
#_____try,except____                           <[Exception]>

a=10
b=0
li=[23,34,55]
print("total")
try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)
print("hello")   

#WAP to open a file and read its contents.
file=open("file.txt","r")
data=file.read()
print(data)
file.close()

#WAP to count the number of lines in a text file.
file=open("temp.txt","a")
file.write("data science and machine learning")
file.close()

file=open("temp.txt","r")
data=file.readlines()
print("Total Lines in This Text File: ",len(data))
file.close()

#WAP to append text to a file
file=open("temp.txt","a")
file.write("\nThis text is append by question on 53\n")
print("Text Append Successfully!")
file.close()

# Write a Python program to read a file line by line.
file = open("temp.txt","r")
for line in file.readlines():
    print(line)
file.close()

# Write a program to copy the contents of one file to another.
file1 = open("temp.txt","r")
file2 = open("copy.txt","w")
data = file1.read()
file2.write(data)
print("Content Copied Successfully!")
file1.close()
file2.close()

#Write a program to write a list of numbers to a text file.
file=open("43.txt","w")
st=""
for a in range(1,101):
    st=st+str(a)+"\n"
    file.write(st)
    print("fille written successfully!")
file.close()    

file=open("43.txt","r")
print(file.read(file))
file.close()

# Write a Python program to read a CSV file.
file = open("58.csv","w")
data = file.write("my world")
print(data)
file.close()

file = open("58.csv","r")
data = file.read()
print(data)
file.close()

# Write a Python program to count the occurrences of a word in a text file.
myFile = open("temp.txt","r")
target = "file"
data = myFile.read()
data = data.lower()
target = target.lower()
count = data.split().count(target)
print(f"{target} is exist {count} times in This file!")
myFile.close()

#WAP to check if a file exists.

import os
file = "temp.txt"
if(os.path.exists(file)):
    print("File Exist")
else:
    print("File Doesn't Exist")








