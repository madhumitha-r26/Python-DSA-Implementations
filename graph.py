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

    # Remove vertex
    def RemoveVertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key, value in self.graph.items():
                if vertex in value:
                    value.remove(vertex)
                    
    # Remove edge 
    def IsEdge(self, vertex1, vertex2):
        return vertex1 in self.graph[vertex2] or vertex2 in self.graph[vertex1]

    def RemoveEdge(self, vertex1, vertex2):
        if self.IsEdge(vertex1, vertex2):
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

g = Graph()
print("ADD VERTICES:")
g.AddVertex("A")
g.AddVertex("B")
g.AddVertex("C")
g.AddVertex("D")
g.Display()

print("ADD EDGES:")
g.AddEdge("A", "B")
g.AddEdge("B", "C")
g.AddEdge("B", "D")
g.AddEdge("C", "D")
g.Display()

print("GET VERTICES:")
g.GetVertices()

print("GET EDGES:")
g.GetEdges()

print("REMOVE VERTICES:")
g.RemoveVertex("C")
g.Display()

print("REMOVE EDGES:")
g.RemoveEdge("A", "B")
g.Display()