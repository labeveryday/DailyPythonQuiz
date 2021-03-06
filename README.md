# DailyPythonQuiz

This repo contains the daily python quizzes and answers.

## I am in the process of updating this document. Please be patient!

1. To get started: Download the code and cd the `DailyPythonQuiz` directory.

    ```bash
    git clone https://github.com/labeveryday/DailyPythonQuiz.git
    cd DailyPythonQuiz
    ```

2. Now that you have the repo downloaded, select a quiz to execute.

    ```bash
    DailyPythonQuiz git:(main) ✗ python quiz3.py 
    ```

    ![Lab](./images/example1.png)

## Python Notes

The first thing you need to understand about Python is the data structures. These are the building blocks to your python applications

## Examples

```python
# strings
example1 = 'This is a string'
example2 = "This is a string"
example3 = """ This is 
also a string"""


# list
x = [2, 5, 'labeveryday']

# Tuples
x = (1,)
y = 1,

# Sets
x = {4}

# Dict
x = {'num1': 5, 'num2': 9}
```

### List comprehensions

```python
numbers = [1, 2, 4, 5, 7, 8, 10]
even_numbers = [x for x in numbers if (x %) == 0]
```

### Lambda functions - used to return outputs (Think of a function)

- Normally given an assigned name

- Single line
[x,y are params:  x + y are return values]

sequence = [79, 3]
double = [(lambda x: x * 2)(2) for x in sequence]

```python
add = lambda x, y: x + y
add(2, 4)
```

### Unpacking arguments

```python
numbers = [1, 9]
num_dict = {"x": 5, "y": 9}

def add(x, y):
    return x + y

add(*numbers)

add(**num_dict)


def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*apply(*args, operator)):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(*args)
    else:
        return "No valid operator provided to apply()"

apply(1, 3, 5, 8, operator="+")
```

### Unpacking Keywork arguments

```python
def named(**kwargs):
    print(kwags)

named(name="Du'An", contact="@labeveryday")


def named(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named(**details)
```

___

### About me

Introverted Network Automation Engineer that is changing lives as a Developer Advocate for Cisco DevNet. Pythons scripts are delicious. Especially at 2am on a Saturday night.

My hangouts:

- [YouTube](https://www.youtube.com/c/LabEveryday)

- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)

- [Twitter](https://twitter.com/labeveryday)
