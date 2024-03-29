from LinkedList import LinkedList

def str_hash(s):
    """ Return a normal hash, unless it is a string. """
    if not isinstance(s, str):
        return hash(s) # not a string => use the normal hash function
    else:
        # Just use the first character of the string. (Not a good hash!)
        h = 0
        i = 0
        n = len(s)
        while i < n:
            h += ord(s[i])*(31**(n - (i+1) ))
            i += 1  # Get the ASCII value of the first char of the string as the hash
        return h

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity
        

    def add(self, item):
        # Find the hash code
        h = str_hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

    def __str__(self):
        """ Print out the hash table """
        s = ""
        for i in range(len(self.table)):
            s += "table[" + str(i) + "]"
            if self.table[i] != None:
                s += " Head " + str(self.table[i])
            s += "\n"

        return s