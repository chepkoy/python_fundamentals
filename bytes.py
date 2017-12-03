# Immutable sequences of bytes
data = b'some bytes'
split = data.split()
print(data, split)

# Encoding
best = "abcdefghijklmnopqrstuvwxyz"
data = best.encode('utf-8')
print(data)