class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            self.cache.move_to_front(self.storage[key])
            return self.storage[key].value
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            self.cache.move_to_front(self.storage[key])
            if self.cache.head.value != value:
                self.cache.head.value = value
        else:
            if self.size == self.limit:
                self.cache.remove_from_head()
                self.size -= 1
                del self.storage[key]
            self.cache.add_to_head(ListNode(value))
            self.storage[key] = self.cache.head
            self.size += 1










class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_head = ListNode(value)
        self.length += 1
        if self.head == None:
            self.head = new_head
            self.tail = new_head
        else:
            old_head = self.head
            old_head.prev = new_head
            new_head.next = old_head
            self.head = new_head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        old_head = self.head
        if self.length == 1: # if there is only 1 node in DLL, set everythign to none
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value
        elif self.length > 1: # if there is more than 1, handle the pointer to the old head
            new_head = old_head.next
            new_head.prev = None
            self.head = new_head
            self.length -= 1
            return old_head.value
        else: # incase there is nothing in the DLL
            return None

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_tail = ListNode(value)
        self.length += 1
        if self.head == None and self.tail == None:
            self.head = new_tail
            self.tail = new_tail
        else:
            old_tail = self.tail
            old_tail.next = new_tail
            new_tail.prev = old_tail
            self.tail = new_tail
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length == 1:
            old_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return old_tail.value
        elif self.length > 1:
            old_tail = self.tail
            new_tail = self.tail.prev
            new_tail.next = None
            self.length -= 1
            return old_tail.value
        else:
            return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    ### handle cases where it is the head or the tail
    ### if not head/tail change the prev and next pointers to eachother
    ### call add_to_head method on node
    ### ^^^ won't work because it will add to the length, when the length isn't chaning
    def move_to_front(self, node):
        if node != self.head and node != self.tail:
            node.prev.next = node.next
            node.next.prev = node.prev
            old_head = self.head
            old_head.prev = node
            node.next = old_head
            self.head = node
        elif node == self.tail and node != self.head:
            node.prev.next = None
            self.tail = node.prev
            old_head = self.head
            old_head.prev = node
            node.next = old_head
            self.head = node
        elif node == self.head:
            print("this node is already in front!")

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node != self.head and node != self.tail:
            node.prev.next = node.next
            node.next.prev = node.prev
            old_tail = self.tail
            old_tail.next = node
            node.prev = old_tail
            node.next = None
            self.tail = node
        elif node == self.head and node != self.tail:
            self.head = node.next
            node.next.prev = None
            old_tail = self.tail
            old_tail.next = node
            node.next = None
            node.prev = old_tail
            self.tail = node
        else:
            print("This node is already the tail!")

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head == None:
            return None
        else:
            max_value = self.head.value
            current = self.head
            while True:
                if current.value > max_value:
                    max_value = current.value
                if current.next == None:
                    break
                else:
                    current = current.next
            return max_value
