# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:56:21 2024

@author: Madhumitha
"""

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
 
    # Adding
    def add(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self.recursiveAdd(data, self.root)
    
    def recursiveAdd(self, data, node):
        if (data < node.data):
            if not node.left:
                node.left = BSTNode(data)
            else:
                self.recursiveAdd(data, node.left)
        elif (data > node.data):
            if not node.right:
                node.right = BSTNode(data)
            else:
                self.recursiveAdd(data, node.right)

    # Displaying                
    def display(self):
        print("Inorder traversal:")
        result1 = []
        self.inorderTraversal(self.root, result1)
        print(result1)

        print("Preorder traversal:")
        result2 = []
        self.preorderTraversal(self.root, result2)
        print(result2)

        print("Postorder traversal:")
        result3 = []
        self.postorderTraversal(self.root, result3)
        print(result3)
    
    def inorderTraversal(self, node, result1):
        if (not node):
            return
        self.inorderTraversal(node.left, result1)
        result1.append(node.data)
        self.inorderTraversal(node.right, result1)
    
    def preorderTraversal(self, node, result2):
        if (not node):
            return
        result2.append(node.data)
        self.preorderTraversal(node.left, result2)
        self.preorderTraversal(node.right, result2)
    
    def postorderTraversal(self, node, result3):
        if (not node):
            return
        self.postorderTraversal(node.left, result3)
        self.postorderTraversal(node.right, result3)
        result3.append(node.data)
    
    # Removing
    def remove(self, data):
        if (not self.root):  # checks whether the root node is none
            print("Binary tree is empty")
            return 
        self.root = self.recursiveRemove(data, self.root)
    
    def recursiveRemove(self, data, node):
        if (not node):
            return node
        
        if (data < node.data):
            node.left = self.recursiveRemove(data, node.left)
        elif (data > node.data):
            node.right = self.recursiveRemove(data, node.right)
        else:
            # Node with only one child or no child
            if (not node.left):
                return node.right
            elif (not node.right):
                return node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self.getMin(node.right)
            node.data = min_larger_node.data
            node.right = self.recursiveRemove(min_larger_node.data, node.right)
        
        return node

    def getMin(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Searching
    def search(self, data):
        node = self.recursiveSearch(data, self.root)
        if node:
            print("True")
        else:
            print("False")
        
    def recursiveSearch(self, data, node):
        if (not node):
            return None
        if (node.data == data):
            return node
        elif (data < node.data):
            return self.recursiveSearch(data, node.left)
        else:
            return self.recursiveSearch(data, node.right)

# Example usage
BST = BinarySearchTree()

print("displaying binary tree:")
BST.add(45)
BST.add(10)
BST.add(50)
BST.add(9)
BST.add(11)
BST.add(46)
BST.add(51)
BST.display()

print("after removal:")
BST.remove(11)
BST.display()