ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# Python does split(ten_things, ' ') here
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # Python does pop(more_stuff) here
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # Python does append(stuff, next_one)
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
# Python does join(' ', stuff)
print(' '.join(stuff))  # what? cool!
print(stuff)
# This is element 3 and 4. Meaning not include 5th.
print(stuff[3:5])
# Python does join('#', stuff[3:5])
print('#'.join(stuff[3:5]))  # super stellar!
