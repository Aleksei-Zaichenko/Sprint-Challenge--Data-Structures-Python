class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.oldest] = item
            self.oldest += 1
            if self.oldest == len(self.storage):
                self.oldest = 0
        else:
            self.storage.append(item)

    def get(self):
        return self.storage