# coding: utf-8
# http://learnpythonthehardway.org/book/ex39.html
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print("stuff[1] = %s" % stuff[1])   # stuff[1] = oranges, stuff[0] = Apples
print("stuff[-1] = %s" % stuff[-1]) # whoa! fancy
print("stuff.pop() = %s" % stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!
