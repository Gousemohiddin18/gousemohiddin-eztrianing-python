#check num is even(+ or -) or odd(+ or -)

n=int(input("enter number"))
if n%2==0:
    print("even")
    if(n>0):
        print("positive")
    else:
        print("negative")
else:
    print("odd")
    if(n>0):
        print("positive")
    else:
        print("negative")

#check biggest number amoung three numbers

n1= int(input("enter number 1: "))
n2= int(input("enter number 2: "))
n3= int(input("enter number 3: "))
if n1>n2 and n1>n3:
    print("n1 is greater")
elif n2>n1 and n2>n3:
    print("n2 is greater")
else:
    print("n3 is greater")


#check number is integer or float

n=10.45
#logic 1
'''if n==int(n):
    print("integer")
else:
    print("float")'''
'''
#logic 2
if isinstance(n,int)==True:
    print("integer")
else:
    print("float")  '''
'''
#logic 3
if n%1==0:
    print("integer")
else:
    print("float") '''
'''
#logic 4
if type(n)==int:
    print("integer")
else:
    print("float") '''
#logic 5
res = n- int(n)
if res>0 or res != 0:
    print("float")
else:
    print("integer")

#check number is divisible by 11

n= int(input("enter number : "))
if n%11==0:
    print("it is divisible by 11")
else:
    print("NOT divisible by 11")


#check the number is 500 or not

n=int(input("enter number  : "))
if n==500:
    print("it is 500")
else:
    print("not a 500")

#check divisible by 2 and 5

n= int(input("enter number : "))
if n%2==0 and n%5==0:
    print("num is dividible by 2 and 5")
else:
    print("NOT dividible by 2 and 5")





