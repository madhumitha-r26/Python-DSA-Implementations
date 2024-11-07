# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:55:31 2024

@author: Madhumitha
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # insert
    def add(self, data):
        if(not self.root):
            self.root = Node(data)
            return
        self.recursiveAdd(data, self.root)
    
    def recursiveAdd(self, data, node):
        if node.left is None:
            node.left = Node(data)
        elif node.right is None:
            node.right = Node(data)
        else:
            # If both children exist, add to the left subtree
            self.recursiveAdd(data, node.left)

    # display
    def display(self, depth=0, node=None):
        if(node is None):
            node = self.root
        if(node is not None):  # Check if the node is not None before accessing data
            print(" " * depth, node.data)
            if node.left is not None:
                self.display(depth + 1, node.left)
            if node.right is not None:
                self.display(depth + 1, node.right)

    # remove
    def remove(self, data):
        if (not self.root):  # checks whether the root node is none
            print("binary tree is empty")
            return 
        if (self.root.data == data):
            self.root = None
            return
        self.recursiveRemove(data, self.root)
    
    def recursiveRemove(self, data, node):
        # if data matches
        if (node.left and node.left.data == data): 
            node.left = None
            return
        if (node.right and node.right.data == data):
            node.right = None
            return
        # if data does not match
        if (node.left):
            self.recursiveRemove(data, node.left)
        if (node.right):
            self.recursiveRemove(data, node.right)

    # search
    def search(self, data):
        node_found = self.recursiveSearch(data, self.root)
        if (node_found):
            print("true")
        else:
            print("false")
        
    def recursiveSearch(self, data, node):
        if (not node or node.data == data):
            return node
        return self.recursiveSearch(data, node.left) or self.recursiveSearch(data, node.right)

# Example usage
bt = BinaryTree()
print("inserting nodes and displaying the tree:")
bt.add(5)
bt.add(1)
bt.add(2)
bt.add(3)
bt.add(4)
bt.add(5)
bt.display()
print("deleting the node from tree:")
bt.remove(3)
bt.display()
print("searching for a node:")
bt.search(6)  