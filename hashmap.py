class Hashmap:
    def __init__(self):
        self.size = 10
        self.hashlist = [None] * self.size
    
    def GetIndex(self, key):
        return hash(key) % self.size
    
    def __setitem__(self, key, value):
        index = self.GetIndex(key)
        if self.hashlist[index] is None:
            self.hashlist[index] = []  # Initialize a new list if None
        
        # Check if the key already exists and update it
        for i, pairs in enumerate(self.hashlist[index]):
            if pairs[0] == key:
                self.hashlist[index][i] = (key, value)  # Update existing key
                return
        
        # If key does not exist, append the new key-value pair
        self.hashlist[index].append((key, value))
    
    def __getitem__(self, key):
        index = self.GetIndex(key)
        if self.hashlist[index] is not None:
            for pairs in self.hashlist[index]:
                if pairs[0] == key:
                    return pairs[1]
        raise KeyError("Key not found")  # Raise an error if key is not found
        
    def __delitem__(self, key):
        index = self.GetIndex(key)
        if self.hashlist[index] is not None:
            for i, pairs in enumerate(self.hashlist[index]):
                if pairs[0] == key:
                    del self.hashlist[index][i]  # Delete the key-value pair
                    return
        raise KeyError("Key not found")  # Raise an error if key is not found

# Example usage
d = Hashmap()
d["Name"] = "ABCD"
print(d.hashlist)
print(d["Name"])  # Should print "ABCD"
del d["Name"]  # Should delete the key "Name"
print(d.hashlist)