#exception handling
#-->
a=100
b=0
try: #u r telling u may have errors
    print(a/b)
except Exception as e:
    print("please note , number cant be divided by zero",e)
print("bye")

please note , number cant be divided by zero division by zero
bye

#2)--->

a=100
b=0
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("dont give second no. has zero",e)
finally:
    print("resources closed")

resource open
dont give second no. has zero division by zero
resources closed

#3)--->

a=10
try:
    b=int(input("Enter a number :"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note , number cant be divided by zero",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("other error",e)
finally:
    print("resources closed")


Enter a number :20
resource open
0.5
resources closed


Enter a number :0
resource open
please note , number cant be divided by zero division by zero
resources closed

#4)--->

x=12
if x%2!=0:
    raise Exception("x should be even number")
else:
    print("x is even number...correct ")

x is even number...correct

#-->
#oops (object oriented programming structure)
#its an efficient concept use in all object oriented programming language like java and python.
#for multiple reasons we use oops concepts for example code reusability,data security,hidding data.
#class : its a blue print. example : birds,laptops
#objects : its a thing created based on the class
#note : class can have multiple objects example : 1)class-birds objects-parrats,peacock 2)class-laptop object:lenova,hp,dell
#--->

class computer:
    def config(self):
        print("YES")
lenovo=computer()
lenovo.config()
dell=computer()
dell.config()

YES
YES

#constructor
#-->

class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID : %d \nName : %s" %(self.id,self.name))
emp1=Employee("teja",420)
emp2=Employee("deepak",220)
emp1.display()
emp2.display()

ID : 420 
Name : teja
ID : 220 
Name : deepak

#class variable
#--->
class computer():
    a=10
    b=20
    print("class variable inside a class",a)
    def config(self):
        c=100
        print("YES")
        print("instance access",self.b)
lenova=computer()
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)
lenova.config()

class variable inside a class 10
10
30
dell 10
YES
instance access 20

#--->























