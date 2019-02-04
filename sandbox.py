
#GLOBAL VARIABLE
#____________________________________________
original_sin = 0

def sin():
    global original_sin
    original_sin += 1

print(original_sin)

sin()
sin()

print(original_sin)
#____________________________________________

# YIELD
#____________________________________________
def cube_numbers(nums):  
    cube_list = []
    for i in nums:
        cube_list.append(i**3)
    return cube_list

cubes = cube_numbers([1, 2, 3, 4, 5])

print(cubes)

def cube_numbers_y(nums):  
    for i in nums:
        yield(i**3)

my_str = [1, 2, 3, 4, 5]
cubes = cube_numbers_y(my_str)

for i in range(len(my_str)):
    print(next(cubes))
#_____________________________________________

some_code = "print(5 + 4)"
print(some_code)
eval(some_code)
exec(some_code) # exec не возвращает значения