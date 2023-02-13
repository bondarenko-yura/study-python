# print current time

import time
import random

# hello world
print("Hello World! " + time.strftime("%H:%M:%S", time.localtime()))

# variables
v1, v2, v3 = 1, 2, 3
assert v1 == 1 and v2 == 2 and v3 == 3

# constants
w1 = w2 = w3 = 4
assert w1 == w2 == w3 == 4

# swapping variables
v1, v2 = v2, v1
assert v1 == 2 and v2 == 1

# math
assert 10 % 3 == 1
assert 10 / 3 == 3.3333333333333335
assert 10 // 3 == 3

# rize to power
assert 2 ** 3 == 8

# strings
stringVar = "Hello World!"
print(stringVar)

multiLineString = """\
This is a multi-line string
value. See how it works? We can even put \"quotes\" in it.
So cool!"""
print(multiLineString)

# lists
listVar = [5, 6, 7, 8, 9]
assert listVar[0] == 5 and listVar[1] == 6 and listVar[2] == 7 and listVar[3] == 8 and listVar[4] == 9

# slicing sequences
assert listVar[1:3] == [6, 7]
assert listVar[1:] == [6, 7, 8, 9]
assert listVar[:3] == [5, 6, 7]

# last two elements
assert listVar[-2:] == [8, 9]

# every other element
assert listVar[::2] == [5, 7, 9]

# reverse list
assert listVar[::-1] == [9, 8, 7, 6, 5]

# replace second and trird element
listVar[1:3] = [10, 11]
assert listVar == [5, 10, 11, 8, 9]

# delete second and third element
del listVar[1:3]
assert listVar == [5, 8, 9]

# syntax sugar: list comprehension
modifiedListVal = [x // 2 for x in listVar]
assert modifiedListVal == [2, 4, 4]
print(sorted(modifiedListVal))

# dictionaries
dictVar = {"key1": "value1", "key2": "value2"}
assert dictVar["key1"] == "value1" and dictVar["key2"] == "value2"
for key, value in dictVar.items():
    print(f"{key} = {value}")

# tuples
tupleVar = (1, 2, 3)
assert tupleVar[0] == 1 and tupleVar[1] == 2 and tupleVar[2] == 3

try:
    tupleVar[0] = 4
except TypeError:
    print("Tuples are immutable!")

# sets
setVar = {1, 2, 3, 4, 5}
setVar.add(5)
assert setVar == {1, 2, 3, 4, 5}
assert 3 in setVar
assert 6 not in setVar


# functions with parameters
def my_function(msg):
    print(my_function.__name__)
    if msg == "":
        raise ValueError("msg cannot be empty!")
    print(msg)


# functions with default parameters
def divide(divisor, dividend=94):
    return dividend // divisor


assert divide(12) == 7
assert divide(12, 94) == 7
assert divide(dividend=94, divisor=12) == 7
assert divide(divisor=12) == 7


# function return lambda
def make_adder(augend):
    def add(addend):
        return addend+augend
    return add


add5 = make_adder(5)
add9 = make_adder(9)

assert add5(100) == 105
assert add9(100) == 109


# function return lambda with state
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


c1 = make_counter()
c2 = make_counter()
assert [c1(), c1(), c1()] == [1, 2, 3]
assert [c2(), c2()] == [1, 2]
assert [c1(), c2(), c1()] == [4, 3, 5]

# if statements
if random.randint(0, 10) < 5:
    print("less than 5")

# for loops
prev = -1
for i in range(0, 10):
    prev += 1
    assert i == prev

# while loops
i = 0
while i < 3:
    assert i < 3
    i += 1

# try/except
try:
    my_function("")
    # catch any error and print it
except Exception as e:
    print(e)
finally:
    print("finally")

# null value sample
nullVar = None  # null value
assert nullVar is None  # check if null

myNum = random.randint(0, 6)
if myNum > 3:
    print("Greater than 3")
elif myNum == 3:
    print("Equal to 3")
else:
    print("Less than 3")

# format strings
for letter in 'ciao':
    print(f"give me a {letter}...")
