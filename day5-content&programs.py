#Random

import random as r
x="i love bikes"
print(r.sample(x,5))

[' ', 's', 'l', 'i', 'k']


#every time it gives different output

a=[1,2,3,4,5]
r.shuffle(a)
print(a)

[4, 2, 5, 3, 1]

#-->
a=[1,2,3,4,5,6]
print(r.choice(a))

3
#-->
b="spiderman far from home"
print(r.choice(b))

d
#-->
a=r.random()
print(a)

0.7260172292441901

#will return random numbers between 0.0 to 1.0
#0.0 includes 1.0 excludes

print(r.randint(20,30))

25
#-->
a=[10,20,30,40,50]
print(r.choices(a,k=10))

[20, 20, 20, 30, 20, 40, 10, 30, 20, 40]

#-->
s="spiderman home coming"
print(r.choices(s,k=15))

['r', 'm', 'm', 'i', 'p', 'p', 'm', ' ', 'a', 'a', 'e', 'h', 'p', 'p', 'a']

#-->
print(r.uniform(5,10)) #float values

5.3587041488314355

#to find out all the functions in a module

z=dir(r)
print(z)

['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']


#display whole year calender

import calendar
print("full calendar")
print(calendar.calendar(2024))


full calendar
                                  2024

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                   1  2  3
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       4  5  6  7  8  9 10
15 16 17 18 19 20 21      12 13 14 15 16 17 18      11 12 13 14 15 16 17
22 23 24 25 26 27 28      19 20 21 22 23 24 25      18 19 20 21 22 23 24
29 30 31                  26 27 28 29               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31


#-->
print("particular month")
print(calendar.month(2023,9))

particular month
   September 2023
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30

#-->
print("set first day of the week")
calendar.setfirstweekday(calendar.TUESDAY)
print(calendar.month(2023,9))

set first day of the week
   September 2023
Tu We Th Fr Sa Su Mo
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30

#-->

#DATE TIME MODULE

import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y") #LOWER CASE
fv=a.strftime("%Y") #UPPER CASE
print("year short version",sv)
print("year full version",fv)

2023-02-03 10:13:08.978323
year short version 23
year full version 2023

#-->
#functioms
# 1)functions without arguments,without return value

def sample():
    print("love you 3000 times")
    print("iron man")
sample()

love you 3000 times
iron man
#-->
def sample():
    print("love you 3000 times")
    print("iron man")
sample()
print("marvel")
sample()

love you 3000 times
iron man
marvel
love you 3000 times
iron man

#-->
def multi():
    n1=int(input("Number :"))
    n2=int(input("Number :"))
    n3=int(input("Number :"))
    prod=n1*n2*n3
    print(prod)
multi()

Number :1
Number :3
Number :5
15

# 2)functions without argument,with return value

def multi():
    n1=int(input("Number :"))
    n2=int(input("Number :"))
    n3=int(input("Number :"))
    prod=n1*n2*n3
    return prod
res=multi()
print(res)

Number :2
Number :4
Number :6
48

# 3)functions with argument,without return value

def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)
multi(3,5,7)

105

#-->
#user input
def multi(a,b,c):
    prod=a*b*c
    print(prod)
a=int(input("Enter a number 1:"))
b=int(input("Enter a number 2:"))
c=int(input("Enter a number 3:"))
multi(a,b,c)

Enter a number 1:2
Enter a number 2:4
Enter a number 3:6
48

# 4) functions with argument,with return value

def multi(n1,n2,n3):
    prod=n1*n2*n3
    return prod
res=multi(3,5,8)
print(res)

120

#-->
#user input

def multi(a,b,c):
    prod=a*b*c
    return prod
a=int(input("Enter a number 1:"))
b=int(input("Enter a number 2:"))
c=int(input("Enter a number 3:"))
res1=multi(a,b,c)
print(res1)

Enter a number 1:22
Enter a number 2:33
Enter a number 3:44
31944



# print multiplication table of the given number using functions with argument,without return value
#-->
def num(n):
    for i in range(1,12):
        print(n,"X",i,"=",i*n)
n=int(input("which table? :"))
num(n)

which table? :5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
5 X 11 = 55


#factors of given numbers 
#-->
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
n=int(input("enter a number :"))
factors(n)

enter a number :10
1
2
5
10

#sum of digits of a given number using functions with argument,with return value
#-->
def sum_digit(n):
    sum_=0
    while (n!=0):
        x=n%10
        sum_=sum_+x
        n=n//10
    return sum_
n=int(input("Enter a number :"))
res=sum_digit(n)
print(res)

Enter a number :222
6

#recursive function
#---> a function which calls itself is called as recursive function
#---> this concept is called as recursion
#--->
def display():
    n=int(input("enter a number :"))
    if n==1:
        display()
    else:
        print("over")
display()


enter a number :1
enter a number :1
enter a number :1
enter a number :1
enter a number :2
over

#recursive function
#--->
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
result=fact(4)
print(result)

24
'''
4!
4*fact(3)
4*3*fact(2)
4*3*2*fact(1)
4*3*2*1*fact(0)
hence output is 24
'''

#fabinociseries
#--->
n=int(input("enter number : "))
a=0
b=1
sum=0
count=1
while(count<=n):
    print(sum, end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b

enter number : 8
0 1 1 2 3 5 8 13

#neon number
#--->
def neon(n):
    sum=0
    sq=n*n
    while (sq!=0)
         s=sq%10
         sum=sum+s
         sq=sq//10
    if sum==n:
        print("neon")
    else:
        print("not a neon")
a=int(input("enter a:"))
neon(a)


enter a:9
neon

#fuction returns more values:
#addition and subtraction of 2 numbers in one fumction
#--->
def add_sub(x,y):
    sub=x-y
    add=x+y
    return sub,add
res1,res2=add_sub(20,10)
print(res1)
print(res2)

10
30

#variable length method
def summ(*a):
 c=0
 for i in a:
     c=c+i   
 print(c)
summ(10,2,3,1,2)

18













