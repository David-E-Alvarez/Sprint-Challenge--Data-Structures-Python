class RingBuffer:
    def __init__(self, capacity):
        self.capacity = 3
        self.arr = []

    def append(self, item):
        
        while len(self.arr) < self.capacity:
            self.arr.insert(tail,item)
            tracker += 1
            print("tracker 2: ", tracker)
            if tracker is self.capacity - 1:
                tracker = 0
            print("tracker 3: ", tracker)
            return self.arr

    def get(self):
        return self.arr

#try with a doubly link list
#other data structures e.g. singly linked list
rb = RingBuffer(3)
print(rb.arr)
rb.append('a')
print('--->',rb.get())
rb.append('b')
print('--->',rb.get())
rb.append('c')
print('--->',rb.get())
rb.append('d')
print('--->',rb.get())
rb.append('e')
print('--->',rb.get())



