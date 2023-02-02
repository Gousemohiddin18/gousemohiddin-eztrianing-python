#dictionary comprahensions
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)

{'rice': 300, 'dhaal': 600, 'oil': 750}

real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items() if age>20}
print(now)

{'sam': 24, 'kumar': 35}


import random
cust=["ravi","shameer","teja","sai","zaheer","kiran","punith","deepak"]
cust_dict={names:random.randint(1,50) for names in cust}
print(cust_dict)

{'ravi': 20, 'shameer': 10, 'teja': 34, 'sai': 41, 'zaheer': 34, 'kiran': 49, 'punith': 23, 'deepak': 2}


#
L1={'a','b','c'}
L2=[1,2,3]
d={a:b for (a,b) in zip(L1,L2)}
print(d)

{'a': 1, 'b': 2, 'c': 3}

stud=["ravi","shameer","teja","sai","zaheer"]
marks=[250,300,350,400,450]
d={name:(percent/(500))*100  for (name,percent)in zip(stud,marks)}
print(d)


{'ravi': 50.0, 'shameer': 60.0, 'teja': 70.0, 'sai': 80.0, 'zaheer': 90.0}


#operations
s1="shameer"
s2="gouse"
s3="    sai    "
print(s1+s2)
print(s1*5)

#functions---> upper,lower,captalize,replace,split,center,count,endswith,find,index

print(s1.upper())
print(s2.lower())
print(s1.capitalize())
print(s1.replace("a","e"))
print(s3.split())
print(s2.center(50,'#'))

print(s1.count("e"))
print(s1.endswith("r"))
print(s1.find("a"))
print(s1.index("e"))



shameergouse
shameershameershameershameershameer
SHAMEER
gouse
Shameer
shemeer
['sai']
######################gouse#######################
2
True
2
4



#mutable and immutable :

mutable - can be changed after creation
immutable - cant be change after creation

immutable : int,float,string,bool,tuple
mutable : list,set,dictionary

#int
x=20
x
20
id(x)
140721172112776
x=40
x
40
id(x)
140721172113416

#list
l=[1,2,3]
l
[1, 2, 3]
id(l)
2740598130624
l.append(4)
l
[1, 2, 3, 4]
id(l)
2740598130624



#check whether a given string is apalindrome or not

#1
a=input("string:")
x=a[::-1]
print(x)
if a==x:
    print("palindrome")
else:
    print("not palindrome")


string:shameer
reemahs
not palindrome

#2
a=input("string:")
x=a[::-1]
print(x)
if a==x:
    print("palindrome")
else:
    print("not palindrome")

string:wow
wow
palindrome


#character present or not

a=input("sting:")
ch=input("chrt:")
if ch in a:
    print("present")
else:
    print("there is no such a character")


sting:shameer
chrt:i
there is no such a character

sting:shameer
chrt:a
present


#space present or not - count


s=input("enter:")
count=0
for i in s:
    if i==' ':
        count+=1
print(count)


enter:s h a m e e r
6

#count of ovels

L=['a','e','i','o','u','A','E','I','O','U']
s=input("enter a string :")
count=0
for i in s:
    if i in L:
        count=count+1
print(count)


enter a string :shameer
3

#math module

import math
print("CEIL 12.5:",math.ceil(12.5))
print("FLOOR 12.5:",math.floor(12.5))
print("SQRT 345:",math.sqrt(345))
print("Factoral 3:",math.factorial(3))
print("Power 2,3:",math.pow(2,3))
print("Remainder 10,3:",math.fmod(10,3))

a,b=divmod(10,3)
print(a,b)


CEIL 12.5: 13
FLOOR 12.5: 12
SQRT 345: 18.57417562100671
Factoral 3: 6
Power 2,3: 8.0
Remainder 10,3: 1.0
3 1




















