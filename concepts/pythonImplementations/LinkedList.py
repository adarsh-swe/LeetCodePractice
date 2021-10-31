class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList():
    def __init__(self):
        self.head = None 

    # intuitive representation of the Linked List
    def __repr__(self):
        currNode = self.head
        nodes = []

        while(currNode != None):
            nodes.append(currNode.data)
            currNode = currNode.next
        nodes.append("None")
        return "->".join(nodes)

    # makes LinkedList Iterable (for i in LList)
    def __iter__(self):
        currNode = self.head
        while currNode != None:
            yield currNode
            currNode = currNode.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_end(self, node):
        if self.head == None:
            self.head = node
            return

        for currNode in self:
            pass
        currNode.next = node

    def add_after(self, target, newNode):
        if(self.head == None):
            print("LL is empty")
            raise Exception("List is empty")
        
        currNode = self.head
        while currNode != None:
            if currNode.data == target:
                newNode.next = currNode.next
                currNode.next = newNode
                return 
            currNode = currNode.next
        raise Exception("Node with data '%s' not found" % target)
        
    def add_before(self,target,newNode):
        if(self.head == None):
            print("LL is empty")
            raise Exception("List is empty")

        if(self.head.data == target):
            newNode.next = self.head
            self.head = newNode
            return

        prevNode = self.head
        currNode= self.head
        while currNode != None:
            if(currNode.data == target):
                prevNode.next = newNode
                newNode.next = currNode
                return
            prevNode = currNode
            currNode = currNode.next

    def remove(self,target):
        if(self.head == None):
            print("LL is empty")
            raise Exception("List is empty")

        if(self.head.data == target):
            self.head = self.head.next
            return

        prevNode = self.head
        currNode= self.head
        while currNode != None:
            if(currNode.data == target):
                prevNode.next = currNode.next
                return
            prevNode = currNode
            currNode = currNode.next
        
        
            

LL = LinkedList()
LL.add_first(Node("1"))
LL.add_end(Node("2"))
LL.add_first(Node("3"))
print(LL)
LL.remove("3")
print(LL)
LL.add_after("1",Node("2.5"))
print(LL)
LL.add_before("1",Node("3"))
print(LL)
