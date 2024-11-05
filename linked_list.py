# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:55:58 2024

@author: Madhumitha
"""

#creating node
class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
    
    def __str__(self): #base level of object
        return "Node Class"
    
#adding node
class LinkedList:
    def __init__(self):
        self.head=None
        
    def add(self,data):
        newNode=Node(data)  
        if(self.head is None):
            self.head=newNode
        else:
            cur=self.head
            while(cur.pointer is not None):
                cur=cur.pointer
            cur.pointer=newNode
    def print(self):
        cur=self.head
        while(cur is not None):
            print(cur.data,end="->")
            cur=cur.pointer
        print("null")

#removing node         
    def remove(self, data):
        if (self.head is None):
            print("Linked List is empty")
            return
        
        # If the head needs to be removed
        if (self.head.data == data):
            self.head = self.head.pointer
            return
        
        # Traverse the list to find the node to remove
        cur = self.head
        while (cur.pointer is not None):
            if (cur.pointer.data == data):
                cur.pointer = cur.pointer.pointer  # Remove the node
                return
            cur = cur.pointer
        
        # If we reach here, the data was not found
        print(data, "is not present in linked list")


print("node creation:")
node1=Node(10)
node2=Node("Hi")
print(node1.data)
print(node1.pointer) 
print(node2.data)
print(node2.pointer)


print("linking node:")
head=Node(1)
node3=Node(2)
node4=Node(3)
head.pointer=node3
node3.pointer=node4

print(head.data)
print(head.pointer) 
print(node4.data)

print("traversing:")
cur=head
while(cur is not None):
    print(cur.data,end="->")
    cur=cur.pointer
print(head.data)
print(cur)

print("adding node:")
ll=LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.print()

print("removing node:") #removing the 3rd node
ll.remove(6)
ll.print()
ll.remove(3)
ll.print()
