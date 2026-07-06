#GRAPH

DICT_GRAPH = {}

class Node:
    def __init__(self, data):
        self.data = data

class Structure:
    def create_node(self, data):
        node = Node(data)  
        return node   
    def create_relation(self, A, B):
            DICT_GRAPH [A] = [B]
            
struc = Structure()
A = struc.create_node(10)
B = struc.create_node(20)
struc.create_relation(A, B)

print(DICT_GRAPH)


'''
1. Create an undirected graph with the following connections:

   * A - B
   * A - C
   * B - D
   * C - D

   Display all the vertices and their connected neighbors.

'''

graph={

    "A":["B","C"],
    "B":["A","D"],
    "C":["A","D"],
    "D":["B","C"]

}

for vertex in graph:
    print(vertex,"->",graph[vertex])



'''
2. Given a graph, determine whether there is a direct connection (edge) between two given vertices.

'''


graph={

    "A":["B","C"],
    "B":["A","D"],
    "C":["A","D"],
    "D":["B","C"]

}

v1=input("Enter first vertex: ")
v2=input("Enter second vertex: ")

if v2 in graph[v1]:
    print("Connected")
else:
    print("Not Connected")


'''
3. Starting from vertex **A**, perform a **Breadth-First Search (BFS)** traversal and display the order in which the vertices are visited.

'''

