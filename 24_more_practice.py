print("Let's practice everything.")
print('You\'d need to know \'both escapes with \\ that do \n and \t tabs.')


poem = """
\tThe lovely world
with logic sp firmly planted
cannot discern \n the needs of love
not comprehend passion from intuition
and requires an explanayion
\n\t\twhere there is none.
"""

print("--------------------")
print (poem)
print("--------------------")


five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beams = started * 500
    jars = jelly_beams / 1000
    crates = jars / 100
    return jelly_beams, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We have %d beans, %d jars and %d crates." % (beans, jars, crates))


start_point = start_point / 10

print("We can also do that this way:")
print("We have %d beans, %d jars and %d crates." % secret_formula(start_point))

