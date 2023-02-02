#basics

#operators ----> +, -, /, //(floor), %,
print(10/2)  #returns float
print(10//2)  # floor ---> returns integer

#relational operator --> <, >, <=, >= , !=
print(10>2)
print(10<2)
print(10>=2)
print(10<=2)
print(10==2)
print(10!=2)
print("\n")
print("LOGICAL OPERATORS")
print(10>2 and 3<10)
print(10>2 or 3>10)
print(10<2 and 3<10)
print(10<2 and 3<10)
print(not(10>2))
print("\n")
print("MULTIPLE INPUTS")
'''a,b = int(input("enter a value")), int(input("enter b value"))
print(a)
print(b)
#separate by comma
c,d = input("enter two values split with ,  operator ").split(",")
print(c)
print(d)
sum = a+b
print(sum)  #by default input() is string --> concatenation occur
e,f = input("enter two values split with ,  operator ").split(",")
print(e)
print(f)'''
print("\n")
print("BITWISE OPERATORS")
#BITWISE and, bitwise or, ~ ,exor, left shift ,
print(10&4)  # & ---> perform and operation
print(12&7)
print(10|4)  # | ---> perform or operation
'''print(12|7)
print(~10)   # ~ --> perform 1's complementory  (-(10+1))
print(5^6)  # ^ --> perform Exor operation  ---> identical gives 0
print(9^8)
print(10<<2)  # << --> 2bits shifted left
print(5<<2)
print(7>>3)'''

print("\n")
print("Conditional Statements") # --->if,ifelse, elseif, elseifladder, nestedif
print("\n")

print("Control Statements")  #---> while or for loop

i=1
while i<=5:
    print(i)
    i+=1

#range(1,10) ----> genarate sequence of numbers
#in ---> membership operator(from that range)


#print("hello world")
print("Hello"+" "+chr(3114)+chr(3125)+chr(3112)+chr(3149))
#print(chr(3098)+chr(3144)+chr(3108)+chr(3119))
#3117
#print(chr(3117)+chr(3120)+chr(3110)+chr(3134)+chr(3125)+chr(3100)+chr(3149))

#variable name
x=100
x
print(x)
_x=200
print(_x)
#4x=300  
#print(4x)
print(type(10+5j))
print(type(True))
print(type("pavan"))   #no chare datatype
#sequence of datatype : list, tuple , dict, string 
print(type([10,20,30]))

#Typecasting
print(int(383.34676))
#print(int("p"))

#finding address
print(id(345))


print(isinstance(5837467,int))
print(bool(1))



#operator precedence & associativity
x = 45+ 2**2 +(56+6)  #BODMAS ---> O --> Order ,
                         # "="  ---> has right to left order 
print(x)


# input statements

n = input(" enter the number ")
print(n)

print(n)   # by default input() ---> is string

#nested if

t=int(input("enter temperature"))
if t>26:
    if t==50:
        print("yes")
    else:
        print("not 50")
else:
    print("not >26")

	
#operators

#operators ----> +, -, /, //(floor), %,
print(10/2)  #returns float
print(10//2)  # floor ---> returns integer

#relational operator --> <, >, <=, >= , !=
print(10>2)
print(10<2)
print(10>=2)
print(10<=2)
print(10==2)

#precedence

x=3*36.32
y=x+56.19
z=y-10
res=print("final result",z)

#print even numbers amoung 2 to 20

'''i=2
while i<=20:
    if i%2==0:
        print(i)
    i+=1 '''

for i in range(2,20,2):    # step =2 (with jump)
    print(i)
	
	
#print odd numbers from 1 to 30

'''i=1
while i<=30:
    if i%2!=0:
        print(i)
    i+=1  '''



'''for n in range(1,30):
    if n%2!=0:
        print(n) '''

for i in range(1,30,2):
    print(i)

	
#product of numbers

n=list(map(int,input("enter numbers").split()))  #take  multiple numbers 
prod=1
a=n*prod
print(a)

n1 = int(input("enter the number 1 "))
print("first number :",n1)
n2 = int(input("enter the number 2 "))
print("second number :",n2)
n3 = int(input("enter the number 3 "))
print("third number :",n3)
f1 = float(input("enter the float number 1 "))
print("first float number :",f1)
f2 = float(input("enter the float number 1 "))
print("first float number :",f2)
s1 = str(input("enter the string 1 "))
print("first string : ",s1)
s2 = str(input("enter the string 2 "))
print("second string :",s2)
c = complex(input("enter the complex number "))
print("complex number is :",c)


print("its","a","good","day",end=" ")  # eliminate the new line
print("all","is","good")

#every word separate weith "#"
print("I","Pavan","satya","sai",sep="#")

#sep & end

'''print("he","satya","sai",end=" ")
print("I"," am",'cse'.sep="*")
print("congralation")'''


#simple multiplication

p = int(input("enter positive number"))
n = float(input("enter negative number"))
res = p*n
print("final result is ",res)

#traiangle

print(".",".",".",".",".")
print(" ",".",".",".",sep=" ")
print(" "," ","."," "," ")

print("\n")

print(" ","(","\","/",")","")
print("","","\","."," /")
print("","","  \"," /")

#guessing number games

import random
n=random.randrange(1,50)
guess=int(input("guess the number"))
while n!=guess:
    if guess<n:
        print("LOW")  
        guess=int(input("guess the number"))
    elif guess>n:
        print("HIGH")  # guess is high according to system  gues : 33--->20 system --> print high
        guess=int(input("guess the number"))
    else:
        break
print("guess is correct")


#find which number is biggest

n1=int(input("enter number 1 : "))
n2=int(input("enter number 2 : "))
if n1>n2:
    print("n1 is biggest number")
else:
    print("n2 is biggest number")

	
	
#elif ladder

t=int(input("enter temperature"))
if t>26:
    print("yes")
elif t==26:
    print("equals to 26")
elif t<26:
    print("it is less")
	
	
#elif condition

t=int(input("enter temperature"))
if t>26:
    print("yes")
elif t==26:                        # check another statement
    print("equals to 26")
else:
    print("not >26 and =26")

	
#conditional statement

t=int(input("enter temperature"))
if t>30:
    print("yes")
else:
    print("No")

	
	
#candy program

k = int(input("enter kumar candy"))
sam = k/2
k1 = sam/2
print("candy has",k1)
print("sam has",sam)

#bitwise operators

n1,n2= map(int,input("enter the number 1").split())
n3=n1 & n2
print(n3)


