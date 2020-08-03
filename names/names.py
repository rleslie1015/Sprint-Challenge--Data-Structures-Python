import time
from binary_search_tree import BSTNode
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# solution using BST 
# first create bst starting with the first name in first list
bst = BSTNode(names_1[0]) 

# insert all of the name except the name which is already the root node
for i in range(1,len(names_2)):
    bst.insert(names_1[i])

# loop through the second list and use the bst contains method to find duplicate names
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

#  runtime varies slightly each time; example runtimes recorded:

# runtime: 0.11457705497741699 seconds
# runtime: 0.10380697250366211 seconds
# runtime: 0.13980579376220703 seconds
# runtime: 0.11453890800476074 seconds
# runtime: 0.11601901054382324 seconds
# runtime: 0.11406302452087402 seconds
# runtime: 0.12554717063903809 seconds
# runtime: 0.13164591789245605 seconds
# runtime: 0.11376214027404785 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
