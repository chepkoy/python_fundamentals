import math
# Homogeneous immutable sequence of Unicode codepoints(characters

# length of the string
length = len("dvkdvjvpjpavjvjrpjavpjvvjajr")

# Concatenation
join = "new" + "found" + "land"

# Using join
colors = ";".join(['#45ff23','#23434','#73638'])

# Split Method
split = colors.split(";")

# concatenating together a collection of strings

concat = ''.join(['high', 'way', 'man'])

# Partition

partition = "unforgetable".partition("forget")

route = depature, separator, arrival = "london:Edinburgh".partition(':')

# if no need of separator

no_need = origin, _, destination = "seattle-boston".partition("-")

# Format

age = "The age of {0} is {1}".format('jim', 32)

# Name fields are matched with keyword arguments
position = "Current position {latitude} {longitude}".format(latitude="60N",
                                                            longitude="5E")

# Access values through keys or indexes with square brackets in the replacement field
pos = (65.2, 23.1, 82.2)

galaxy_position = "Galactic position x = {pos[0]} y = {pos[1]}, z = {pos[2]}".format(pos=pos)
print(galaxy_position)

# Accessing attributes using dot in the replacement field

mathematics = "Math constatants: pi={m.pi}, e= {m.e}".format(m=math)

# The replacement field mini-language provides many value and alignment formatting

math_thematics = "Math constatants: pi={m.pi:.3f}, e= {m.e:.3f}".format(m=math)
