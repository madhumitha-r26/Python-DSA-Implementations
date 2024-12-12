# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:54:03 2024

@author: Madhumitha
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:48:13 2024

@author: Madhumitha
"""

class Graph:
    def __init__(self):
        self.graph = {}

    # Add vertex
    def AddVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print("Vertex already exists")
     
    # Add edge
    def AddEdge(self, vertex1, vertex2, isDirected=False):
        if vertex1 not in self.graph:
            self.AddVertex(vertex1)  
        if vertex2 not in self.graph:
            self.AddVertex(vertex2)  
        self.graph[vertex1].append(vertex2)
        if not isDirected:
            self.graph[vertex2].append(vertex1)

    # Display graph    
    def Display(self):
        for key, value in self.graph.items():
            print(f"{key} => {value}")

    # Get vertices    
    def GetVertices(self):
        for i in self.graph:
            print(i)

    # Get edges            
    def GetEdges(self):
        edges = set()  # Use a set to avoid duplicate edges
        for key, value in self.graph.items():
            for vertex in value:
                edges.add((key, vertex))
        for edge in edges:
            print(edge)
            
            
    #dfs traversal
    def DFS_traversal(self,start,AlreadyVisited=set()):
        if(start not in AlreadyVisited):
            AlreadyVisited.add(start)
            print(start,end="")
            for child in self.graph[start]:
                self.DFS_traversal(child,AlreadyVisited)

g = Graph()

g.AddEdge("A", "B")
g.AddEdge("B", "C")
g.AddEdge("B", "D")
g.AddEdge("C", "D")
g.AddEdge("D", "E")
g.AddEdge("E", "B")
g.Display()


print("DFS TRAVERASAL:")
g.DFS_traversal('A')
