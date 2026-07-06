graph = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['B'],
    'D': ['A', 'C'],
    'E': ['B', 'C']
}

print(graph)

graph = {
    'A': {'B': 10, 'E': 25},
    'B': {'D': 2, 'C': 8},
    'C': {'B': 40},
    'D': {'A': 1, 'C': 13},
    'E': {'B': 9, 'C': 101}
}

print(graph)


GLOBAL_DICT = {}

class Node:
    def __init__(self, data):
        self.data = data

class Structure:       
    def gen_node(self, data):
        node = Node(data) #  we are creating the node for the structure 
        return node   
    def generate_relation(self, node1, node2):
            GLOBAL_DICT [node1] = [node2] 


struc = Structure()

node_1 = struc.gen_node(10)
node_2 = struc.gen_node(20)

struc.generate_relation(node_1, node_2)

print(GLOBAL_DICT)

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