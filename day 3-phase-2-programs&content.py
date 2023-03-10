# while creating LL  we gonna do it in ascending order
# one prg multiple concept :
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        if not current:
            print('list is empty.')
        else:
            print('start:' , end=' ')
        while current:
            print(current.data, end =' -> ')
            current = current.next
        print('end.')

    def insert(self,data):
        new_node = Node(data)

        #if the linked list is empty
        if self.head is None:
            self.head = new_node

        # if the data is smaller than the head
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:
            # locate  node before the insertion point :
            current = self.head
            while current.next and new_node.data > current.next.data:
                current = current.next

            #insertion
                new_node.next =current.next
                current.next = new_node

    def delete(self,key):
        #if the list is empty
        if self.head is None:
            print('Delete error :the list is empty')
            return
        #if the key is in head
        if self.head.data == key:
            self.head = self.head.next
            return

        # find position of first occurrence of the
        current = self.head
        while current:
            if current.data == key:
                break
            previous = current
            current = current.next

# name is python special variable
if __name__=='__main__':
    # create an object
    LL = LinkedList()
    print('')
    #insert some nodes
    LL.insert(23)
    LL.insert(87)
    LL.insert(8)
    LL.insert(30)
    LL.insert(90)


    LL.printList()
    LL.delete(8)
    LL.delete(87)
    LL.delete(90)
    LL.printList()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CreateList:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    #Adding node at end of LL
    def add(self,data):
        newNode=Node(data)
        #Is empty?
        if self.head.data is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            #It is CLL so tail will point to head
            self.tail.next=self.head
        def display(self):
            current=self.head
            if self.head is None:
                print("List is empty")
                return
            else:
                print("Nodes of circular linkedlist: ")
                print(current.data,"-->")
                while(current.next!=self.head):
                    current=current.next
                    print(current.data,"-->")
class CircularLinkedList:
    c1=CreateList()
    c1.add("H")
    c1.add("E")
    c1.add("L")
    c1.add("L")
    c1.add("O")
    c1.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init_(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_end()
l.display()


#create node
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__ (self):
        self.head=None
    def display(self):
        if self.display is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.display()

#deleting node at bigginning in linkedlist

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init_(self):
        self.head=None
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_beginning()
l.display()

#inserting node at any position in double linkedlist

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init_(self):
        self.head=None
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            tem=temp.next
            n.prev=temp
            n.next=
            =None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_pos(2)
l.display()


#inserting node at end in double linkedlist

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init_(self):
        self.head=None
    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_end()
l.display()

#inserting node in double linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_start()
l.display()









            
        

        
