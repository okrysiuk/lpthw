def make_list(list_lenght, increment):
    i = 0
    numbers = []
    while i < list_lenght:
        print("At the top number is: %d" % i)
        numbers.append(i)
        print("Numbers now: ", numbers)
        i += increment
        print("At the bottom number is: %d" % i)
    print("The numbers list is: ")
    for i in numbers:
        print(i)
    return numbers

#new_list = make_list(20, 2)

#print("Lenght of list is:", len(new_list), "elements.")

def make_list_2():
    numbers = []
    for i in range(0, 6):
        print("At the top number is: %d" % i)
        numbers.append(i)
        print("Numbers now is: " % numbers)
        i += 1
        print("At the bottom number is: %d" % i)
    print("The numbers list is: ")
    for i in numbers:
        print(i)
    return numbers

new_list_2 = make_list_2()

print("Lenght of list is:", len(new_list_2), "elements.")