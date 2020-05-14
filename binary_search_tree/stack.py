"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack: # Implementation using lists pass all tests
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size >= 1:
            self.size -= 1
            return self.storage.pop(-1) # This missing return statment for the Test tripped me up for a while....



### For parts 2/3
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.add_to_end(value)

#     def pop(self):
#         if len(self.storage) >= 1:
#             return self.storage.remove_from_end()

class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def add_to_end(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            self.size += 1

    def remove_from_head(self):
        if self.head == None:
            return None
        else:
            value_removed = self.head.value
            self.size -= 1
            self.head = self.head.get_next()
            return value_removed
            
    def remove_from_end(self):
        if self.head == None:
            return None
        elif self.head.get_next() == None: # incase method is used when there is only 1 node
            popped = self.head.value # value to return for test
            self.head == None
            self.tail == None
            self.size -= 1
            return popped # return for test
        else: 
            current = self.head
            while current.get_next() != None: # sort of a replacement for a for loop
                # setting data to move down the LL chain
                previous = current
                current = current.get_next()
                #if it reaches the end of the chain, it removes the last node by pointing the previous node to None
                if current.get_next() == None:
                    previous.next_node = None
                    self.size -= 1
                    return current.value #this is the node "popped" for the test
