#stack implementation using array or list
#stack is LIFO - last in first out
#-->
stack=[]
def push():
    element=int(input("enter the element : "))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element :",e)
        print(stack)
while True:
    print("select operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("enter the current operation")

-->

select operation 1.push 2.pop 3.quit
1
enter the element : 111
[111]
select operation 1.push 2.pop 3.quit
1
enter the element : 222
[111, 222]
select operation 1.push 2.pop 3.quit
1
enter the element : 333
[111, 222, 333]
select operation 1.push 2.pop 3.quit
2
removed element : 333
[111, 222]
select operation 1.push 2.pop 3.quit
2
removed element : 222
[111]
select operation 1.push 2.pop 3.quit
2
removed element : 111
[]
select operation 1.push 2.pop 3.quit
2
stack is empty
select operation 1.push 2.pop 3.quit
3

#-->
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode=self.head
            self.head=self.head.next
            poppednode.next=None
            return poppednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(t!=None):
                print(t.data,end=" ")
                t=t.next
                if(t!=None):
                    print(" --> ",end=" ")
            return
if __name__=="__main__":
    S=Stack()
    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.display()
    print(S.peek())
    S.pop()
    S.pop()
    S.display()
    
-->

4  -->  3  -->  2  -->  1 4
2  -->  1

#checking blanced parantheis

s=input()
st=[]
balanced=True
for char in s:
    if(char=='{' or char=='['or char=='('):
        st.append(char)
    elif(char=='}'):
        if(len(st) and st.pop()!='{'):
            balanced=False
            break
    elif(char==']'):
        if(len(st) and st.pop()!='['):
            balanced=False
            break
    elif(char==')'):
        if(len(st) and st.pop()!='('):
            balanced=False
            break
    else:
        balanced=False
        break
if(balanced==False or len(st)):
    print("not Balanced")
else:
    print("Balanced")
    

-->

[()]
Balanced

[}
not Balanced

(([]))
Balanced

#queue
queue=[]
def enqueue():
    elements=input("enter the element")
    queue.append(elements)
    print(elements,"is added in q")
def dequeue():
    if not queue:
        print("Q is empty")
    else:
        e=queue.pop(0)
        print("removed element",e)
def display():
    print(queue)
while True:
    print("select operation 1.add 2.remove 3.show 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("pls enter correct operation")

#implementing stack in Queue module
from queue import LifoQueue
s=LifoQueue(maxsize=3)
print(s.qsize())
s.put('a')
s.put('b')
s.put('c')
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())

-->

0
True
3
c
b
a
True

#implementing queue in Queue module

import queue
L=queue.Queue(maxsize=5)
L.put(10)
L.put(20)
print(L.get())
print(L.get())

-->

10
20

#queue implement using linkedlist

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
a_queue=Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do=input('what would like to do?').split()
    operation=do[0].strip().lower()
    if operation=='enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation=='dequeue':
        dequeued=a_queue.dequeue()
        if dequeued is None:
            print('queue is empty')
        else:
            print('dequeu element: ',int(dequeued))
    elif operation=='quit':
        break

-->

enqueue <value>
dequeue
quit
what would like to do?enqueue 100
enqueue <value>
dequeue
quit
what would like to do?enqueue 200
enqueue <value>
dequeue
quit
what would like to do?dequeue
dequeu element:  100
enqueue <value>
dequeue
quit
what would like to do?dequeue
dequeu element:  200
enqueue <value>
dequeue
quit
what would like to do?quit

#creating linklist removing duplicates


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
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
    def get_prev_node(self,ref_node):
        current=self.head
        while(current and current.next !=ref_node):
            current=current.next
        return current
    def remove(self,node):
        prev_node=self.get_prev_node(node)
        if prev_node is None:
            self.head=self.head.next
        else:
            prev_node.next=node.next
    def display(self):
        current=self.head
        while current:
            print(current.data,end=' ')
            current=current.next
    def remove_duplicates(llist):
        current1=llist.head
        while current1:
            data=current1.data
            current2=current1.next
            while current2:
                if current2.data==data:
                    llist.remove(current2)
                current2=current2.next
a_llist=LinkedList()
data_list=input('please enter the element in the linked list').split()
for data in data_list:
    a_llist.append(int(data))
    remove_duplicates(a_llist)
print('the list with duplicates removed: ')
a_llist.display()






        
