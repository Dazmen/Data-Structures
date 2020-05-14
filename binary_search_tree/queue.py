"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue: # passes tests
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value): # push
        self.storage.append(value)
        self.size += 1

    def dequeue(self): # pop
        if self.size >= 1:
            self.size -= 1
            return self.storage.pop(0)


### parts 2/3
# class Queue: # Passes tests
#     def __init__(self):
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value): # push
#         self.storage.add_to_end(value)

#     def dequeue(self): # pop
#         return self.storage.remove_from_head()


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