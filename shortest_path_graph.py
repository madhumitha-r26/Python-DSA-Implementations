# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:03:05 2024

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

    # Shortest path
    def shortest_path(self,start,end):
        AlreadyVisited={start}
        Queue=[(start,[start])]
        while (len(Queue)>0):
            current,path=Queue.pop(0)
            print(current,end="")
            for child in self.graph[current]:
                if(child==end):
                    return path+[child]
                if(child not in AlreadyVisited):
                    Queue.append((child,path+[child]))
                    AlreadyVisited.add(child)

g = Graph()
print("VERTICES:")
g.AddVertex("A")
g.AddVertex("B")
g.AddVertex("C")
g.AddVertex("D")
g.Display()

print("EDGES:")
g.AddEdge("A", "B")
g.AddEdge("B", "C")
g.AddEdge("B", "D")
g.AddEdge("C", "D")
g.Display()

print("SHORTEST PATH:")
g.shortest_path("A", "D")