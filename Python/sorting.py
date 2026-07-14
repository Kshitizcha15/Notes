'''
A cricket coach has the scores of 15 players.

Requirements:
    Accept scores of all players.
    Display the original list.
    Sort the scores using bubble sort.
    Display the sorted score.
    Ask the coach to enter a player's score.
    Search for the score using binary search.
    Display the player's rank based on the sorted list.
    Also display:
        Highest score
        Lowest score
        Total no. of players
'''
'''
storing the 15 players scores in a list
Data Structure Used: List
(taking the user input in the list and then sorting it using bubble sort and then searching for the score using binary search)
Algorithm Used: Bubble Sort, Binary Search
displaying the original list, sorted list
asking the coach to enter the scores to search and then displaying the rank based on the sorted list 
and also displaying the highest score, lowest score and total number of players
'''

scores = []

for i in range(15):
    score = int(input(f"Enter score of the player {i+1}: "))
    scores.append(score)


print("\nOriginal Scores:", scores)

n = len(scores)
for i in range(n - 1):
    for j in range(n - i - 1):
        if scores[j] > scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]


print("\nSorted Scores:", scores)

key = int(input("\nEnter score to search:"))
low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2
    if scores[mid] == key:
        print("Score Found!")
        break
    elif scores[mid] < key:
        low = mid + 1
    elif scores[mid] > key:
        high = mid - 1
    else:
        print("Score Not Found!")

print("Player Rank:", n - mid) 

print("\nHighest Score:", scores[-1])
print("Lowest Score:", scores[0])
print("Total Number of Players:", n)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Structure:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new
    