# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:54:36 2024

@author: Madhumitha
"""

class Weighted_Graph:
    def __init__(self):
        self.graph={}
    
#add vertex
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]={}
    
#add edge
    def add_edge(self,from_vertex,to_vertex,weight,isDirected=False):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.graph[from_vertex][to_vertex]=weight
        if(isDirected==False):
            self.graph[to_vertex][from_vertex]=weight
    
#remove edge
    def remove_edge(self,from_vertex,to_vertex):
        if(from_vertex in self.graph) and (self.graph[from_vertex]):
            del self.graph[from_vertex][to_vertex]
        if(to_vertex in self.graph) and (self.graph[to_vertex]):
            del self.graph[to_vertex][from_vertex]

#remove vertex
    def remove_vertex(self,vertex1):
        if vertex1 in self.graph:
            del self.graph[vertex1]
        for vertex2 in self.graph:
            if vertex1 in self.graph[vertex2]:
                del self.graph[vertex2][vertex1]


wg=Weighted_Graph()

print("WEIGHTED GRAPH:")
wg.add_edge("C","B",300)
wg.add_edge("C","M",700)
wg.add_edge("C","D",1000)
wg.add_edge("M","D",400)
print(wg.graph)

print("REMOVING ONE VERTEX:")
wg.remove_vertex("M")
print(wg.graph)