# Based on https://www.youtube.com/watch?v=f79MRyMsjrQ

import math  # math module

# STRINGS
string_variable = "I'm a string"
# print(type(string_variable))  # <class 'str'>
CONSTANT = "naming convention for constants, no built-in function"

len(string_variable)  # 12
string_variable.find("str")  # 6
string_variable.replace("s", "S")  # "I'm a String"
"Int" in string_variable  # False
"Int" not in string_variable  # True

# Type annotation with Python3 and mypy linter
int_variable: int = 1
int_variable = "change to string"  # mypy(error)
# print(int_variable)  # "change to string"

learning = "Python3"
len(learning)  # 7
learning[0]  # P
learning[-2]  # n
learning[0:3]  # Pyt

# Formatted String
meal = "lunch"
ate = "sashimi salad"
meal_log = ate + " for " + meal
meal_log = f"{1+1} {ate} for {meal}"   # "2 sashimi salad for lunch"


arithmetic = 10 + 3  # 13
arithmetic = 10 - 3  # 7
arithmetic = 10 * 3  # 30
arithmetic = 10 / 3  # 3.3333
arithmetic = 10 // 3  # 3
arithmetic = 10 % 3  # 1
arithmetic = 10 ** 3  # 1000
arithmetic += 1  # 1001

PI = 3.14
round(PI)  # 3
math.floor(PI)  # 3

age = 22
if age >= 18:
    # print("Adult")
    pass
elif age >= 13:
    print("Teenager")
else:
    print("Child")


# Logical Operators (and or not)
name = ""
if not name:
    ("Name is an empty string")

age = 22
if age >= 18 and age < 65:  # same as 18 <= age < 65
    ("Eligible")


# Ternary
message = "Eligible" if age >= 18 else "Not eligible"


# Iteration (for loops and while loops)

# for loops
for x in ['a', 'b', 'c']:
    x

for x in range(5):
    x


# Range Object (iterable), not a list, take much less memory
# print(type(range(500000000)))  # <class 'range'>
# print(range(500000000)) # range(0, 500000000)

for x in range(0, 10, 2):  # init, final, step
    x

names = ["John", "James"]
for name in names:
    if name.startswith("J"):
        ("Found first name starting with 'J'")
        break  # ends loops
else:
    print("Loop completed without a break")

# while loops
guess = 0
answer = 5

# while answer != guess:
#     guess = int(input("Guess: "))


# Functions

def increment(number: int, by: int = 1) -> tuple:    # set default by=1
    return(number, number + by)


increment(2, 3)
increment(2, by=3)  # optional key for info


# *args to pass arbitrary number of parameters -> tuple
def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


multiply(2, 3, 4, 5)


# **args to pass arbitrary number of key/value pairs -> dictionary
def save_user(**user):
    return(user["id"])  # 1


save_user(id=1, name="admin")  # {'id': 1, 'name': 'admin'}


# SCOPE (local or global)

message = 'a'  # global


def greet():
    message = 'b'  # local
    return message


greet()    # b
# print(message)  # a


# FIZZBUZZ

def fizz_buzz(input):
    if input % 15 == 0:
        return "Fizzbuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
