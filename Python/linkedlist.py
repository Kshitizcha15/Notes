'''
Linked List 

1. Create a linked list with the values **10, 20, 30, 40, 50**. Display all the elements from the beginning to the end.

2. Given a linked list containing **5 → 10 → 15 → 20**, insert the value **12** after **10** and display the updated linked list.

3. Given a linked list containing **8 → 16 → 24 → 32**, delete the node containing **24** and display the remaining elements.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.ref:
            temp = temp.ref
        temp.ref = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.ref

ll = LinkedList()

for i in [10,20,30,40,50]:
    ll.add_end(i)

ll.display()