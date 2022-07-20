class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = next
class LinkedList :
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode :
            yield curNode
            curNode = curNode.next
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False   
    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        return  "great"
    def pop(self):
        if self.isEmpty():
            return "There is no any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    def peep(self):
        if self.isEmpty():
            return "There is no any element in the stack "
        return self.LinkedList.head.value   
    def delete(self):
        self.LinkedList.head = None
    
customstack = Stack()
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack)
print("---------")
customstack.pop()
print(customstack)