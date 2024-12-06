# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:22:58 2024

@author: Madhumitha
"""

class TreeNode:
    def __init__(self,value):  #node
        self.value=value
        self.children=[]

class Tree:       
    def __init__(self): #tree
        self.root=None
    
    def recursive(self,node):
        if(node is None):
            return
        print(node.value)
        for child in node.children:
            self.recursive(child)

tree=Tree()
node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
node6=TreeNode(6)

#directly inserting the node
tree.root=node1
node1.children=[node2,node3]
node2.children=[node4,node5,node6]
tree.recursive(tree.root)
