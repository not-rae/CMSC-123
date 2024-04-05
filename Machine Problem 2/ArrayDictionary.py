class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

class Array:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.contents = [None] * capacity
        self.size = 0

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity

    def isEmpty(self):
        return self.size == 0

class ArrayDictionary(Array):
    def insert(self, key, value):
        entry = Entry(key, value)																			
		# Check if the array is empty
        if self.size == 0:
            self.contents[0] = entry
            self.size += 1					
            return None

        # Check if the key is less than the first element
        if key < self.contents[0].getKey():						
            i = self.size									
            while i > 0:									 
                self.contents[i] = self.contents[i - 1]
                i -= 1
            self.contents[0] = entry						
            self.size += 1
            return None

        # Find the position to insert the new entry
        i = 0
        while i < self.size:
            if self.contents[i].getKey() == key:
                # If the key already exists, create a new entry with the same key
                new_entry = Entry(key, value)						
                j = self.size		
                while j > i:
                    self.contents[j] = self.contents[j - 1]			
                    j -= 1
                self.contents[i] = new_entry						
                self.size += 1
                return None
            
			# if the key falls between two existing entries
            elif i + 1 < self.size and self.contents[i].getKey() < key < self.contents[i + 1].getKey():
                j = self.size
                while j > i + 1:
                    self.contents[j] = self.contents[j - 1]								 
                    j-= 1
                self.contents[i + 1] = entry									
                self.size += 1
                return None
            
			# key is greater than the key of the last element
            elif i + 1 == self.size and self.contents[i].getKey() < key:
                self.contents[i + 1] = entry				
                self.size += 1
                return None
            i += 1																											# counter to move to the next position 

    def remove(self, entry):
        # removes the specified entry, and returns the entry that was removed
        if self.isEmpty():
            raise Exception("Empty")
        i = 0							
        while i < self.size:				
            current = self.contents[i]
            if current is not None and current.getKey() == entry.getKey() and current.getValue() == entry.getValue():
                removed_entry = current						
                j = i													
                while j < self.size - 1:					
                    self.contents[j] = self.contents[j + 1]
                    j += 1
                self.contents[self.size - 1] = None																			# sets the last position to None (since the size has decreased)
                self.size -= 1
                return removed_entry
            i += 1							
        return None

    def find(self, key):
        # finds and returns the entry that matches the specified key
        if self.isEmpty():
            raise Exception("Empty")
        i = 0
        while i < self.size:				
            if self.contents[i] is not None and self.contents[i].getKey() == key: 
                return self.contents[i]									
            i += 1
        return None

    def find_all(self, key):
        # used to find and print all entries in the array that matches a specified key				        
        for entry in self.contents:
            if entry is not None and entry.getKey() == key:				
                print(f"({entry.getKey()}:{entry.getValue()})")
        print()

    def entries(self):	
        # used to iterate thru the array and print all entries in the specified format					
        for entry in self.contents:						
            if entry is not None:
                print(f"{entry.getKey()}:{entry.getValue()}")