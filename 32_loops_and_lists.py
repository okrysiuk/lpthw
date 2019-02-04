numbers = [1, 2, 3, 4, 5, 6, 77, 88, 999]
toys = ["penis", "dildo", "chaines", "pump"]
for i in numbers:
    print("This is %d in numbers" % i)
for i in toys:
    print("I got: %r" % i)

girls = []

for i in range(1, 6):
    print("Add %d to the girls list." % i)
    girls.append(i)

for i in girls:
    print("This is %r-st" % i)

bitches = ["Natasha", "Lena", "Tanya", "Sveta", "Vera-Tripak"]

girls.append(bitches)

for i in girls:
    print("This is %r." % i)