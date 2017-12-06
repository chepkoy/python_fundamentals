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

print(listed)