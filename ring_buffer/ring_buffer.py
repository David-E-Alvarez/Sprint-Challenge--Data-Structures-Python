class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.old = 0

    def append(self, item):
        #old variable = 0
        #add item at old's location; arr[old]
        self.arr[self.old] = item
        #check to see if old + 1 is equal to capacity and if so set old to 0
        if self.old + 1 == self.capacity:
            self.old = 0
        else:
            self.old += 1
        # if not add 1 to old


    def get(self):
        arr2 = []
        for i in range(0, len(self.arr)):
            if(self.arr[i] is not None):
                arr2.append(self.arr[i])
        return arr2

#rb = RingBuffer(5)
# rb.append('a')
# rb.append('b')
# rb.append('c')

# rb.append('d')
# rb.append('e')



