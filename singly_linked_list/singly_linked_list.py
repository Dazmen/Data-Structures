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
        self.max = None

    def __len__(self):
        return self.size

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            self.size += 1

    def remove_tail(self):
        if self.head == None:
            return None
        elif self.head.get_next() == None: # incase method is used when there is only 1 node
            popped = self.head.value # value to return for test
            self.head == None
            self.tail == None
            self.max == None
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

    def get_max(self):
        if self.head != None:
            current = self.head
            while current != None:
                if self.max == None or current.value > self.max:
                    self.max = current.value
                current = current.get_next()
            return self.max
        else:
            return None

    def remove_head(self):
        current = self.head
        next_head = current.get_next()
        current.set_next(None)
        self.head = next_head
        return current.value

    def contains(self, value):
        current = self.head
        does_contain = False

        while current != None:
            if current.value == value:
                does_contain = True
            else:
                current = current.get_next()

        return does_contain