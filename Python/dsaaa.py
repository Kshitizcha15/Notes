class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class TreeStructure:
    def createRoot(self, data):
        self.root = Node(data)

    def insertNode(self, data):
        self.new_node = Node(data)

        # Logic Approach 1
        if self.root.left is None:
            self.root.left = self.new_node

        elif self.root.right is None:
            self.root.right = self.new_node

        else:
            print("Move to the next level as the root is connected to two nodes.")

    # Logic Approach 2
    def left(self, root_node, node):
        self.root.left = node

    def right(self, root_node, node):
        self.root.right = node
        
         