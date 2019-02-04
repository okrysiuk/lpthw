states = {'Oregon':'OR','Florida':'FL', 'California':'CA','New York':'NY', 'Michigan':'MI'}
cities = {'CA':'San Francisco', 'MI':'Detroit', 'FL':'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
# Print out some cities
print('-' * 10)
print("NY State has", cities['NY'])
print("OR State has", cities['OR'])
# Print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
# Do it by using the state than the cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
# Print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("%s state has %s abbreviation." % (state, abbrev))
# Print every city in state
for abbrev, city in cities.items():
    print("%s has %s city." % (abbrev, city))
# Now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))
# Safely get abbreviation by state that might not be there
print('-' * 10)
state = states.get('Texas', None)
if not state:
    print("Sorry there is no Texas.")
# Get a city with a default value
city = cities.get('TX', 'Does not exist')
print("The city for the state 'TX' is: %s" % city)
