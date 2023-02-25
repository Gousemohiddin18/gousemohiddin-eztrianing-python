#lambda functions
when we wnt to use function concept without using function there we apply concept of lambda concept

#-->
L=[1,2,3]
r=map(lambda x:x+x,L)
print(list(r))

[2, 4, 6]

#-->
res=map(lambda n:pow(n,2),L)
print(list(res))

[1, 4, 9]

#-->
name="sam"
(lambda name:print(name))(name)

sam
#--> 4 pillers of oops
#1.abstraction
#2.encapsulation
#3.inheritance
#4.pholimophism

#1.abtraction:
--> hiding the implementation part showing the what is required for the user
ex: EXE file
--> we can make class or method has abstract opposite to extract is concrete
#-->
import abc abstractmethod (ABC)
class abstractdemo(ABC):
    @abstractmethod
    def display(self):
        none
    @abstractmethod
    def show(self):
        none
class demo(abstractdemo):
    def display(self):
        print("abstracttion method")
    def show(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()

#2.encapsulation:
--> binding data and function into single entity
 public : one class info can be accesed by any other class,low level data protection,a
 private : can used where it is declared/no in inheritacted class,medium level data protection,__c
 protector : can be accessed only where it got declared which ever class inrited from this class there also we can use,high level data protection,_b

#3.inheritence :
 bases class and derived class
 derived class will inherit properties of base class
 base class-parent class
 derived class-child class
 
#-->types of inheritance
1.single inheritance
2.multiple inheritance
3.multilevel inheritance
4.hierarchical inheritance 
5.hybrid inheritance

#1.single inheritance :
#-->
class parent:
    def display(self):
        print("parent class")
class child(parent):
    def show(self):
        print("child class")
c=child()
c.display()
c.show()
-->
parent class
child class

#-->
class A:
    n=30
class B(A):
    def calc(self):
        c=self.n+70
        print(c)
obj=B()
obj.calc()

-->
100


#2.multiple inheritance :
#-->
class mom:
    def mdisplay(self):
        print("mom class")
class dad:
    def ddisplay(self):
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.ddisplay()

-->
child class
mom class
dad class

#3.multilevel inheritance :
#-->
class grandparent:
    def display(self):
        print("grand parent class")
class parent(grandparent):
    def show(self):
        print("parent class")
class child(parent):
    def printing(self):
        print("child class")
c=child()
c.display()
c.show()
c.printing()

-->
grand parent class
parent class
child class


#4.hierarchical inheritance :
#-->
class parent:
    def pdisplay(self):
        print("parent class")
class child1(parent):
    def c1show(self):
        print("child1 class")
class child2(parent):
    def c2show(self):
        print("child2 class")
c1=child1()
c1.c1show()
c1.pdisplay()
c2=child2()
c2.c2show()
c1.pdisplay()

-->
child1 class
parent class
child2 class
parent class

#5.hybrid inheritance :
#-->
class parent:
    def pdisplay(self):
        print("parent class")
class child1(parent):
    def c1show(self):
        print("child1")
class child2(parent):
    def c2show(self):
        print("child2")
class kid1(child1):
    def k1display(self):
        print("kid1 class")
class kid2(child1):
    def k2display(self):
        print("kid2 class")
class kidd1(child2):
    def k1show(self):
        print("kidd1 class")
class kidd2(child2):
    def k2show(self):
        print("kidd2 class")
c1=kid1()
c1.k1display()
c1.c1show()
c1.pdisplay()
c2=kid2()
c2.k2display()
c2.c1show()
c2.pdisplay()
c3=kidd1()
c3.k1show()
c3.c2show()
c3.pdisplay()
c4=kidd2()
c4.k2show()
c4.c2show()
c4.pdisplay()

-->
kid1 class
child1
parent class
kid2 class
child1
parent class
kidd1 class
child2
parent class
kidd2 class
child2
parent class


#happy number
#--->







