# Heterogeneous mutable sequence

texts = "show how to index into sequences".split()

# Zero and positive integers for indexing from the front
position = texts[4]

# Negative integers index from the end
negative = texts[-5]

# slicing extracts part of a list
# Slice range is half -open stop not included

sliced = texts[1:4]

# slicing works with negative indexes

slice_negative = texts[1:-1]

# Ommiting the stop index slices to the end

stop_index = texts[3:]

# Omitting the start index slices from the beginning

start_index = texts[:3]

# half open ranges  give complementary slices

combined = start_index + stop_index

# omitting the start and stop indexes slices from the beginning to end
# full slice
# Important idiom for copying lists

full_slice = texts[:]

# using the copy method

copy = texts.copy()

# Using the list constructor

listed = list(texts)

# Repeating lists using the * operator
# Mostly used for initializing a list of known size with a conststant
# Multiple refs to one instance of the constant in product list

repeat = [21, 37]
product = repeat * 4

repeat_two = [0] * 9

# Finding Elements
# ValueError if not found

w = "the quick brown fox jumps over the lazy dog".split()
i = w.index('fox')

# count returns the number of matching elements

match = w.count('the')

# The in and not in operators test for membership

test = 37 in [1, 44, 54, 634, 37]
test_two = 37 not in [1, 44, 54, 634, 37]

# del [index] to remove by index

u = "jackdaws love my big sphinx of quartz".split()
del u[3]

# remove to remove by value raises ValueError if not present
u.remove('jackdaws')

# remove  equivalent to
#del seq[seq.index(item)]

# inserting elements to a list

a = "i accidentally the whole universe".split()
two = a.insert(2, "destroyed")

# Concatenation with the + operator

m = [2, 1, 3]
n = [4, 7, 11]

k = m + n

# in -place extension with += operator or extend() method

k += [18, 29, 47]
k.extend([23, 45, 65, 8])

# Reverse in place

g = [1, 11, 21, 1211]
g.reverse()

# sorting using the sort method
g.sort()
g.sort(reverse=True)

# key argument to sort() method accepts a function for producing a sort key from an item

h = " not surprising at all"
h.sort(key=len)

# using the sorted function
x = [4, 9, 2, 1]
y = sorted(x)

# using the reverse function returns an iterator

p = [9, 3, 1, 0]
q = reversed(p)