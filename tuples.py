# Heterogeneous immutable sequence

t = ("Norway", 4.8683, 3)

# Accessing the element

element = t[0]

# Determine the number of elements
number = len(t)

# Iterating using the for loop
for item in t:
    print(item)

# Concatenate using the + operator

new = t + (338186.0, 2736)

# repeated using the multiplication operator

repeat = t * 3

# Nested tuples

nested = ((220, 284), (1184, 1210), (2620, 2924))
inner_element = nested[2][1]

# Single element tuple

single_element = (391,)

# Empty tuple
empty = ()

# Emmiting the parentheses
emmitted = 1, 1, 1, 4, 6, 19

# Returning multiple values from a function


def minmax(items):
    return min(items), max(items)


min_max = minmax([83,44,56,78,24,7,856,])

# Returning multiple values as tuples tuple unpacking
lower, upper = min_max

# Tuple unpacking with nested tuples
nested_tuple = (a, (b, (c, d))) = (4, (3, (2, 1)))
print(a, b, c)
print(lower, upper)

# Swapping idiom
a = "jelly"
b = "bean"
swap = a, b = b, a
print(a, b)

# Tuple constructor
construct = tuple([45, 56, 75, 2, 67])
print(construct)

# Containment

contain = 5 in (3, 54, 65, 5)
dont_contain = 5 not in (3, 7, 3)

print(contain, dont_contain)