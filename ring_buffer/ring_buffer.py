class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.old = None
    def append(self, item):
        """
        Add when it not full!
        add to the end of the lsit

        When it is full for the first time: set a old object as the [0] index
    
        Check if it is full for the nth time after first
        move the old object index and overite the old object

        """
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            
        elif len(self.storage) == self.capacity and self.old == None:
            self.old = 0
            self.storage[self.old] = item
            self.old = (self.old + 1) % self.capacity

        elif len(self.storage) == self.capacity and self.old != None:
            self.storage[self.old] = item
            self.old = (self.old + 1) % self.capacity

    def get(self):
            return self.storage
      