# use of list tuple set dictionary

# List
l = []

# adding element in to list
l.append(5)
l.append(7)
print("Adding 5 and 10 in list ", l)

# popping element from list
l.pop()
print("Popped one element from list ", l)
print()

# Set

s = set()
# Adding element in to set

s.add(10)
s.add(12)
print("Add element in set ", s)

# Removing elements from set
s.remove(10)
s.remove(12)
print("Removed element 10 and 12 from set ", s)
print()

# Tuple
t = tuple(l)

# tuple are immutable
print("Tuple", t)
print()

# Dictionary
d = {}
# adding key value pair
d[5] = "five"
d[10] = "Ten"
print("Dictionary ", d)

# Removing value from dictionary
del d[10]
print("Dictionary ", d)
