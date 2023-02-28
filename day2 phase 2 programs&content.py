#happy number
#-->
def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
            r=n%10
            s=s+r**2
            n=n//10
        return s
n=int(input("enter a number:"))
res=n
while (res!=1 and res!=4):
    res=happy(res)
if res==1:
    print("happy number ")
else:
    print("not a happy number")

-->
enter a number:133
happy number 

#protected_
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("encap function-accessing protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)

-->
10
encap function-accessing protected
20
20

#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)#it will throw error
#because a is private cant be accesed

-->
10
encap function
10
Traceback (most recent call last):
  File "C:/Users/Mahendra J/Desktop/programs.py", line 42, in <module>
    print(obj.__a)#it will throw error
AttributeError: 'encap' object has no attribute '__a'
#pholimophisam :
-->one item or same item used for different  purposes
#types :
#1.overloading
   a)operator overloading
   b)method overloading
#2.overwriting
   
#-->
#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("without arguments")
obj.display()

print("with all arguments")
obj.display(20,30)

print("with one argument")
obj.display(10)

-->
without arguments
None None
with all arguments
20 30
with one argument
10 None


#overwriting :
#if a method is difective or cannot be used inside derived class it will take it from base class or parents class
#-->
class vijayawada():
    def placename(self):
        print("vijayawada place name is KLU")
    def student(self):
        print("yes - vijayawada")
    def which_year(self):
        print("3rd year")
class hyd():
    def placename(self):
        print("Hyd place name is Hyd-KLU")
    def student(self):
        print("yes - HYD")
    def which_year(self):
        print("3rd year-HYD")
obj_vij=vijayawada()
obj_hyd=hyd()
for details in (obj_vij,obj_hyd):
    details.placename()
    details.student()
    details.which_year()

-->
vijayawada place name is KLU
yes - vijayawada
3rd year
Hyd place name is Hyd-KLU
yes - HYD
3rd year-HYD

#Data structures :
-->helps to write efficient programs
   #1.linear : array/linkked list/stack/queue/matrix
        a)static : array
        b)dynamic : list,stack,queue
   #2.non linear : binnary tree/heap/hash table/graph

#linked list :
--> As the name says list of items which are linked with one another

#types :
  1)singly
  2)doubly
  3)circular

#-->creating linklist
    step-1 : create the node
    step-2 : partisan the node with two segments data and none
    step-3 : add values into the blank node
    step-4 : mark the node as head
    step-5 : create the next node by following the above step
    step-6 : astablish link betweeen 1 node and 2 node

#displaying link list :
-->traversal is required from first node till tail node in order to display existing link list

#creating a link list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
obj.display()

-->
10 --> 20 --> 30 -->

#-->

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("w")
obj.head=n
n1=Node("i")
obj.head.next=n1
n2=Node("n")
n1.next=n2
n3=Node("n")
n2.next=n3
n4=Node("e")
n3.next=n4
n5=Node("r")
n4.next=n5
obj.display()

-->
w --> i --> n --> n --> e --> r -->

#operations :

1)insert
  a)beginning
  b)end
  c)position
2)delete
3)search

#insert_beginning

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")
obj.insert_beginning(100)
obj.display()
print("")
print("after inserting 555")
obj.insert_beginning(555)
obj.display()

-->
before inserting 100
10 --> 20 --> 30 --> 40 --> 50 --> 
after inserting 100
100 --> 10 --> 20 --> 30 --> 40 --> 50 --> 
after inserting 555
555 --> 100 --> 10 --> 20 --> 30 --> 40 --> 50 -->

#insert_end :

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")
obj.insert_end(100)
obj.display()
print("")
print("after inserting 555")
obj.insert_end(555)
obj.display()

-->

before inserting 100
10 --> 20 --> 30 --> 40 --> 50 --> 
after inserting 100
10 --> 20 --> 30 --> 40 --> 50 --> 100 --> 
after inserting 555
10 --> 20 --> 30 --> 40 --> 50 --> 100 --> 555 --> 

#insert_position :

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print("")
obj.insert_position(2,1000)
obj.display()

-->
10 --> 20 --> 30 --> 40 --> 50 --> 
10 --> 20 --> 1000 --> 30 --> 40 --> 50 --> 

-->

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next
a_llist=LinkedList()
n=int(input('how many elements would you like to add :'))
for i in range(n):
    data=int(input('enter data item:'))
    a_llist.append(data)
print('the linked list:',end='')
a_llist.display()







