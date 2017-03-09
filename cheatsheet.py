
# Python cheet sheet for Samuel and Kishan's python workshop
# Don't try to run this file; you'll just get a lot of undefined
# variable errors

# define variable a to be 5
a = 5

# define variable b to be the string: Hello World!
b = "Hello World!"

# print(...) prints whatever is inside the parenthesis to the console
print("Wheee!")

# if you want to be able to change the data that your program uses while
# it's running, here's how you can get information from the user;
string = input("Please type a number: ")
# asks the user to type a number and press enter. what the user types gets
# stored in the data variable.
# note that the response will always be a string, not a number.
# (even if that's what you prompted the user for.)

# to convert a string into a number:
x = float(string)

# numbers can be added like this:
a + b

# they can be subtracted:
a - b

# multiplied:
a * b

# devided:
a / b

# raise a to the power of b
a ** b

# to find the square root of a number:
math.sqrt(x)
# but remember to to this sometime beforehand:
import math
# alternatively, you can raise x to the one-half power
x ** (1/2)

# to define a function called foo:
def foo():
    print("bar!")
# after you do this, anytime you say:
foo()
# bar! will be printed

# functions can also take argments (a.k.a. parameters):
def quux(a, b):
    c = a + b
    print(c)
# the above function takes 2 arguments, adds them, and prints the result.

# functions can also return values; translating from math,
# a Python function's return value is very similar to the evaluated value
# of a function in math.
# for example: y = 3 * x  is expressed in Python as:
def multiply_by_three(x):
    return 3 * x

# you can test if a is less than b like so:
a < b
# the result of this expression is True or False depending on whether
# a is actually less than b
a > b
# checks if a is greater than b
a == b
# checks if a and b are equal

# now suppose that we only want to do something if a certain condition
# holds true (like x is greater than 4)
if x > 4:
    print("Guess what? x is greater then 4!")

# but what if we want to do something else if x isn't greater than 4?
if x > 4:
    print("Guess what? x is greater then 4!")
else:
    print("Oh crap! Whatever happened to x?")

# Well that's all well and good, but what about those piecewise functions
# from math?
if x < 2:
    y = 3 + x
elif x > 2:
    y = x * 17
else:
    print("x is 2! value undefined!")

# One thing computers are really great at is doing lots of repetitious tasks.
# like processing hundreds of personell records...
# How do we do stuff like this?
# for example, suppose we want to find all of the fibonacci numbers
# less than 1000:
a = 1
b = 1
while b < 1000:
    print(b)
    c = a + b
    b = a
    a = c
