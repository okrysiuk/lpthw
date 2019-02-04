def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" %(a, b))
    return a / b


age = add(30, 2)
height = subtract(213, 15)
weight = multiply(42, 2)
iq = divide(120, 3)

print("Age: %d, height: %d, weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle for extra credit, type it anyway


print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("Thats becomes: ", what, "Can you do it by hand?")

