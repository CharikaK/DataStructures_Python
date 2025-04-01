# create nodes
# Create Linked List
# Add nodes to Linked List
# Print Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # at start Head Node is empty
    def __init__(self):
        self.head = None

    # function insertNode
    def insertNode(self, newNode):
        # headNode is John->None(pointing to)
        if self.head is None:
            self.head = newNode
        else:
            # head=>John->Ben->None
            # node.data = John
            # node.next = Node Ben
            # when it is trying to insert the third node, the LinkedList head is still John, and John.next is Ben
            # Then this will place the Nodes incorrectly
            ## self.head.next = newNode

            # so lets take the latest Head Node as the lastNode
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break # means we found the Node with empty next value
                lastNode = lastNode.next # lastNode should be the Node with empty next value
            lastNode.next = newNode # so we can assign the newNode as next value
    
    def printList(self):
        if self.head is None:
            print("List is Empty")
            return # get out of the function

        currentNode = self.head
        while True:
            if currentNode is None: # if self.head was None then the currentNode is None 
                break
            print(currentNode.data)
            currentNode = currentNode.next



# Create the first Node
# Node => data, next
firstNode = Node("John")

# Create LinkedList
linkedList = LinkedList()
linkedList.insertNode(firstNode)

secondNode = Node("Ben")
linkedList.insertNode(secondNode)

thirdNode = Node("Matthew")
linkedList.insertNode(thirdNode)

linkedList.printList()