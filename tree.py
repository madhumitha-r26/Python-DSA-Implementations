# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:55:33 2024

@author: Madhumitha
"""

# node creation
class treenode:
    def __init__(self, data):
        self.data = data
        self.children = []

class tree:
    def __init__(self):
        self.root = None
        
# insert
    def add(self, data, parentdata=None):
        node = treenode(data)
        if self.root is None: 
            self.root = node  # making the current node as root node
            return
        parentNode = self.findNode(parentdata, self.root)
        if not parentNode:
            print("parent node not found")
            return 
        parentNode.children.append(node)   
    
# searching child node
    def findNode(self, data, node):
        if node is None:
            return None
        if(node.data == data):
            return node
        for child in node.children:
            nodefound = self.findNode(data, child)
            if nodefound is not None:  
                return nodefound
        return None  
   
# display
    def display(self, depth=0, node=None):
        if node is None:
            node = self.root
        print(" " * depth,node.data)  # moved this line outside of the if block
        for child in node.children:
            self.display(depth + 1, child)

#remove
    def remove(self,data): 
        #it checks for the root node and then it will print the data
        if(not self.root):
            print("tree is empty")
            return
        if(self.root.data==data):
            self.root=None
            return
        parentNode=self.findParentNode(data,self.root)
        if(parentNode):
            for child in parentNode.children:
                if(child.data==data):
                    parentNode.children.remove(child)
                    return
        print("node not found")
    
# searching parent node    
    def findParentNode(self, data, node):
        for child in node.children:      
            if(child.data == data):
                return node
            nodefound = self.findNode(data, child)
            if nodefound:
                return nodefound
        return None  
        

tree = tree()
print("inserting nodes and displaying the tree:")
tree.add(5)     #root node      
tree.add(6,5)   #printing (child,parent)     
tree.add(7,5)           
tree.add(1,7)          
tree.add(2,6)          
tree.add('a',1)          
tree.display() 
print("deleting the node from tree:")     #deleting th parent node     
tree.remove(6) 
tree.display()