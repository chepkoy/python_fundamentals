# Python while loops

count = 5
while count != 0:
    print(count)
    count -= 1  #  Augmented assignment operator

while True:
    print("Looping")

# Breaking Out

while True:
    response = input()
    if int(response) % 7 == 0:
        break