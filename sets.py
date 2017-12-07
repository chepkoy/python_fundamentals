# Unordered collection of unique immutable objects

p = {6, 28, 496, 93843, 39}

# empty set

e = set()

# Accepts  iterable series of values, duplicates are discarded, used to remove duplicates

s = set([2, 4, 16, 4096])

t = [1, 4, 2, 1, 7]

set(t)

# Arbitrary order

for x in {1, 2, 4, 8, 16, 32}:
    print(x)

# adding elements

k = {81, 108}

k.add(54)

# For multiple elements use update

k.update([37, 128, 97])

# Removing elements

k.remove(97)
k.discard(90)

# copying

j = k.copy()
m = set(j)

# Set algebra

s.union(t) # all elements are either or both set
s.intersection() # Element present in both sets
s.difference()# elements present First set not in the second set
s.symmetric_difference()# exclusitivity 1st or 2nd but not both
s.issubset() # if is subset of another
s.issuperset()
s.isdisjoint()# sets not members in common