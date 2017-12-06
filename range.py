# Arithmetic progression of integers

progress = range(5)
print(progress)

# loop counters stop values is one-past the end
# Ranges are half-open start is included  but stop is not
for i in range(5, 10):
    print(i)

listt = list(range(5, 10))

# Stop value of a range used as start value of concecutive range

concecutive = list(range(10, 15))


# optional third step value

third = list(range(0, 10, 2))


# using the build in enumerate function
t = [6, 372, 8862, 148800, 823328]
for p in enumerate(t):
    print(p)

# combining with tuple unpacking

for i, v in enumerate(t):
    print("i={}, v = {}".format(i, v))