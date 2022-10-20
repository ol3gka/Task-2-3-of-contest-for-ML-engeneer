import networkx as nx
import matplotlib.pyplot as plt
import random

class Graph:
    def __init__(self):
        self.edges = [] # the set of edges
        self.nodes = [] # the set of nodes
        
    def add(self, a, b): # MULTITASK function to add edge if a!=b, and to add node if a==b;  А, Б mini tasks
        if a != b:
            self.edges.append([a, b])
            if a not in self.nodes: self.nodes.append(a)
            if b not in self.nodes: self.nodes.append(b)
        else: 
            self.nodes.append(a)
            
    def visualize(self): # plt.show() - display the graph with matplotlib as required; Г mini task
        graph = nx.Graph()
        graph.add_edges_from(self.edges)
        graph.add_nodes_from(self.nodes)
        nx.draw_networkx(graph)
        plt.show
        
class random_Graph: # В mini task
    def __init__(self):
        self.edges = [] # the set of edges
        self.nodes = [] # the set of nodes
        
    def gen(self, n=random.randint(10, 20), X='ABCDEFJ'): # function to add edge if a!=b, and to add node if a==b 
        for i in range(n):
            a,b = random.choice(X),random.choice(X)
            if a != b:
                self.edges.append([a, b])
                if a not in self.nodes: self.nodes.append(a)
                if b not in self.nodes: self.nodes.append(b)
            else: 
                self.nodes.append(a)
            
    def visualize(self): # plt.show() - display the graph with matplotlib as required
        graph = nx.Graph()
        graph.add_edges_from(self.edges)
        graph.add_nodes_from(self.nodes)
        nx.draw_networkx(graph)
        plt.show()
