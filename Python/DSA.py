# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def insert(head):
#   currentNode = head
#   while currentNode:
#     print(currentNode.data)
#     currentNode = currentNode.next
#   print("null")

# first creating first node first node  
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None  # reference value None 
# this my second where i have to add my new node created
class DS:
    def __init__(self):
        self.head = None
        
    def insert_new(self, data ):
        node1 = Node(data)
        node1.ref = self.head
        self.head = node1
        
    # here i am inserting new node and between two nodes 
    def insert_btw(self, data, prev):
        node1 = Node(data)
        node1.ref = prev.ref
        prev.ref = node1
    def insert_end(self, data):
        node1 = Node(data)
        node1.ref = None
        # node1.head = None(data)

    #devlop a code find node using the data
    # finding nodes 
    def find_node(self, data):
        current = self.head
        while current:  # while loop using 
            if current.data == data:
                print("value found")
                return current   # here found data then going to while loop 
            current = current.ref
            print("value Not")
        # Data not found
        return None



    # delete first node
    def delete_first(self):
            if self.head is None:
                print("Linked List is Empty")
                return
    
            temp = self.head        # Store the first node
            self.head = self.head.ref   # Head moves to the second node
            temp.ref = None         # Remove the reference of the first node

    def delete_last(self):
                if self.head is None:
                    print("Linked List is Empty")
                    return
        
                temp = self.head 
                while temp.ref.ref:
                    temp = temp.ref
                temp.ref = None  


    def delete_btw(self, prev):
                if prev is None or prev.ref is None:
                    return

                temp = prev.ref
                prev.ref = temp.ref
                temp.ref = None              








    