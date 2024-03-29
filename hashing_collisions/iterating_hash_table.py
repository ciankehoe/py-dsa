from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

    # Provide an iterator function
    def __iter__(self):
        i = 0
        #while self.table[i] != None and i < len(self.table):
        while i < len(self.table) and self.table[i] != None:
            ptr = self.table[i].head
            while ptr != None:
                yield ptr.item
                ptr = ptr.next
            i += 1