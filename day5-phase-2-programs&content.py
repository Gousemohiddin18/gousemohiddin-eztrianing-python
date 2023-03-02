#implementation of binary tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
node1=BinaryTreeNode(50)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(45)
node4=BinaryTreeNode(11)
node5=BinaryTreeNode(15)
node6=BinaryTreeNode(30)
node7=BinaryTreeNode(78)

node1.leftChild=node2
node1.rightChild=node3
node2.leftChild=node4
node2.rightChild=node5
node3.leftChild=node6
node3.rightChild=node7

print("Root Node is : ")
print(node1.data)

print("left child of the node is : ")
print(node1.leftChild.data)

print("right child of the node is : ")
print(node1.rightChild.data)

print("Root Node is : ")
print(node2.data)

print("left child of the node is : ")
print(node2.leftChild.data)

print("right child of the node is : ")
print(node2.rightChild.data)

print("Root Node is : ")
print(node3.data)

print("left child of the node is : ")
print(node3.leftChild.data)

print("right child of the node is : ")
print(node3.rightChild.data)

-->

Root Node is : 
50
left child of the node is : 
20
right child of the node is : 
45
Root Node is : 
20
left child of the node is : 
11
right child of the node is : 
15
Root Node is : 
45
left child of the node is : 
30
right child of the node is : 
78


#trees

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val,end=" ")
        printInorder(root.right)
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val,end=" ")
def printPreorder(root):
    if root:
        print(root.val,end=" ")
        printPreorder(root.left)
        printPreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("PRE-ORDER:")
printPreorder(root)
print()
print("\nIN-ORDER:")
printInorder(root)
print()
print("\nPOST-ORDER:")
printPostorder(root)

-->

PRE-ORDER:
1 2 4 5 3 

IN-ORDER:
4 2 5 1 3 

POST-ORDER:
4 5 2 3 1

#BST-INSERT

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)

-->

20
30
40
50
60
70
80

