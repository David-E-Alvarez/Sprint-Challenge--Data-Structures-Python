import time

start_time = time.time()

f = open('/home/david/sprintChallenges/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('/home/david/sprintChallenges/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
        #check to see if value being passed in is less than the root's value
        if value < self.value:
            #if so check to see if roots left child doesn't have any children because 
            #if it doesnt this is where you add this value
            if self.left is None:
                self.left = BSTNode(value)
            #if there IS a left child recursively try to insert value
            else:
                self.left.insert(value)
        #if value > self.value
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                #there is child so run insert again
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


bst_inst = BSTNode()

for name in names_1:#iterate over list and insert each of the elements into BST
    bst_inst.insert(name)#

for name in names_2:
    #print("name: ", name)
    if bst_inst.contains(name):
        duplicates.append(name)
        #print("dups: ", duplicates)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
