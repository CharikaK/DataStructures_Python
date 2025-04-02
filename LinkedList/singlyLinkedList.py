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

    # function to decide the length of the LinkedList
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode.next is not None:
            length += 1
            currentNode = currentNode.next
        return length
    
    # function to check the List is empty
    def isListEmpty(self):        
        if self.head is None:
            return True
        else:            
            return False

    # function insertNode
    def insertNodeEnd(self, newNode):
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

    def insertNodeHead(self, newNode):
        # assign the head node to a temporary so we do not break the list
        # then assign the newNode to the head
        # then assign temporary node to newNode.next
        # delete the temporary node
        temporaryHeadNode = self.head
        self.head = newNode
        self.head.next = temporaryHeadNode
        
        del temporaryHeadNode

    def insertNodeAt(self, newNode, position):
        # if the position is invalid
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return

        # if the new insertion is to the position 0; that means calling insertNodeHead
        if position == 0:
            self.insertNodeHead(newNode)
            return # return from the function

        # traveling trough nodes > mark the currentNode + mark their positions
        # record previousNode and currentNode until we find the position to insert the newNode
        # assign it into a previousNode
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break # break the loop - remember!
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousNode = self.head
            
            
            self.head = self.head.next
            previousNode.next = None
        else:
            print("Linked list is empty")

    def deleteEnd(self):
        # this is to make previousNode.next to point to None
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = previousNode.next

        # Soon the lastNode.next is None; which means that is the endNode
        # So now we make our previous node to the last node's next as None(unlink the last node)
        previousNode.next = None # Matthew should be gone now

    def deleteNodeAt(self, position):
        if position < 0 or position <= self.listLength():
            print("Invalid Position")
            return
        
        currentPosition = 0
        currentNode = self.head

        while True:
            # Assume we are removing Ben 2
            # Ben 2 position is 3
            # previous node is Ben
            # current node is Ben2 (which we are going to delete)
            # currentnode.next is Matthew
            
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1


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



linkedList.insertNodeEnd(firstNode)

secondNode = Node("Ben")
linkedList.insertNodeEnd(secondNode)

thirdNode = Node("Matthew")
linkedList.insertNodeEnd(thirdNode)

forthNode = Node("Shreya")
linkedList.insertNodeHead(forthNode) # Shreya becomes head

# adding a Node into a position
positionNode = Node("Ben 2")
linkedList.insertNodeAt(positionNode, 3) # try with position < 0 , large position value 

linkedList.printList() # Shreya->John->Ben->Ben 2->Matthew

# uncomment below to test deleteEnd
#linkedList.deleteEnd() # remove Matthew

#linkedList.deleteNodeAt(3)
linkedList.deleteHead() # remove Shreya
print("****** Removing head ******")
linkedList.printList() # John->Ben->Ben 2->Matthew

