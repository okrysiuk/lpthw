ten_things = "Apples Oranges Pineapples Sugar Salt Sousages"
print("There is not 10 things in list, so let fix that.")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Penis", "Ball", "Snow", "Watches", "Car"]

while len(stuff) != 10:
    new_stuff = more_stuff.pop(0)
    stuff.append(new_stuff)
    print("Now lenght of stuff list is %d" % len(stuff))

print("So that is result: ", stuff)
print("Now let's do some things with stuff!")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print("#".join(stuff[3:5]))


