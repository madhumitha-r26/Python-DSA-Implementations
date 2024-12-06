# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:37:38 2024

@author: Madhumitha
"""

class TreeNode:
    def __init__(self, value):  # node
        self.value = value
        self.children = []

class Tree:       
    def __init__(self):  # tree
        self.root = None
  
    def recursive(self):
        if self.root is None:
            return
        
        queue = [self.root]  # Initialize the queue with the root node
        
        while queue:
            current_node = queue.pop(0)  # Dequeue the first node
            print(current_node.value)  # Process the current node
            
            # Enqueue all children of the current node
            for child in current_node.children:
                queue.append(child)

tree = Tree()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

tree.root = node1
node1.children = [node2, node3]
node2.children = [node4, node5, node6]

tree.recursive()  