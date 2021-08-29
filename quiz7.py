#! /usr/bin/env python
"""
Date: 8-29-2021
Twitter Link: https://twitter.com/labeveryday/status/1431260882252836866?s=20
-----------------------------------------------------------------------------

Python quiz question for the day?

def add_num(x=4, y):
    return x + y

print(add_num(10))

If we execute this code, what is the result?

#LabEverydayDailyPythonQuiz #Day7
"""

# Example 1: How to Define a function?
def add_num1():
    print(3 + 4)


# Example 2: How to call a function
add_num1()


# Example 3: Understanding Print vs Return
def add_num2():
    print(3 + 4)

x = add_num2()
print(f"X is {x}")


def add_num3():
    return 3 + 4

y = add_num3()
print(f"Y is {y}")


# Example 4: How to pass arguments into a function?
def add_num4(x, y):
    return x + y

print(add_num4(50, 25))


# Example 5: Understanding standing positional arguments.
def print_name(first_name, last_name):
    print(f"My first name is {first_name}")
    print(f"My last name is {last_name}")

print_name("Lightfoot", "Du'An")
print_name("Lightfoot", "Du'An")
print_name(first_name="Du'An", Lightfoot="Lightfoot")


# Example 6: Using Keyword Arguments
def print_name2(first_name, last_name):
    print(f"My first name is {first_name}")
    print(f"My last name is {last_name}")

print_name2("Du'An", fist_name="Lightfoot")
print_name2(last_name="Lightfoot", first_name="Du'An")

# Example 7: Assigning default values
def print_name2(first_name, last_name="Lightfoot"):
    print(f"My first name is {first_name}")
    print(f"My last name is {last_name}")

print_name2(first_name="Du'An", last_name="Lightfoot")

# Quiz Question - This will fail!
def add_num(x=4, y):
    return x + y

print(add_num(10))
