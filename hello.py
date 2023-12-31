
# Lists
a = [5]

# Tuple
# Tuple is immutable
b = [7]


# Operators
# Arithmetic Operators


# Addition
print("Addition: ", 2 + 3)


# Subtraction
print("Subtraction: ", 2 - 3)


# Multiplication
print("Multiplication: ", 2 * 3)


# Division
print("Division: ", 2 / 3)


# Floor Division
print("Floor Division: ", 2 // 3)


# Modulus
print("Modulus: ", 5 % 2)


# Exponent
print("Exponent: ", 2 ** 3)


# Assignment Operators
# =
a = 12
print("Assignment: ", a)




print("Comparison Operators")
print("--------------------")
# Comparison Operators returns boolean value (True or False)
# To compare two values are equal or not
# ==
print("Comparison: ", 2 == 3)

# !=
print("Comparison: ", 2 != 3)


# To compare two values are greater or not
# >
print("Comparison: ", 2 > 3)


# To compare two values are less or not
# <
print("Comparison: ", 2 < 3)


# To compare two values are greater than or equal or not
# >=
print("Comparison: ", 2 >= 3)


# To compare two values are less than or equal or not
# <=
print("Comparison: ", 2 <= 3)




print("Comparison 1: ", 2 >= 4)


print("Comparison 2: ", 2<= 4)


# Strings in depth
# String is a sequence of characters


# String Declaration
# Single Quotes
str1 = 'Hello World'
# Double Quotes
str2 = "Hello World"


# Wrong use of quotes
# str3 = 'Hello World"
# str4 = "Hello" "World"
str5 = "Hello\" \"World"


# String Concatenation
str6 = "Hello " + "World"
print(str6)
str7 = "hello" + "my" + "name" + str6
print(str7)


# Input from user
# input() - function
# input() - function always returns string


# name = input("Enter your name: ")
# print(name)


# Python Program to Add Two Numbers 


# Python Program to Swap Two Variables


# Python Program to Check if a Number is Positive, Negative or 0 (Refer to line 47)

# loops

## For loop

# Syntax
# for <variable> in <sequence>:

print("For Loop")
for i in ['bread', 'milk', 'butter', 'jam', 'cheese']:
    print(i)

sum = 0
for a in [1, 2, 3, 4, 5]:
    print('a: ', a)
    print('sum: ', sum)
    sum = sum + a
    # process
    # sum = 0
    # a = 1
    # sum + a
    # sum = 0 + 1
    # sum = 1
    print('sum: ', sum)

# if condition
# if <condition>:
#     <statement>
# elif <condition>:
#     <statement>
# else:
#     <statement>

if 2 > 3:
    print("2 is greater than 3")
elif 2 < 3:
    print("2 is less than 3")
else:
    print("2 is equal to 3")

# Python Program to Check if a Number is Positive, Negative or 0 (Refer to line 47)
a = 0
if a > 0:
    print('positive')
elif a < 0:
    print('negative') 
else: 
    print('equal to')
    

# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

# range(start, stop, step)
for a in range(1500,2705,5):
    if a % 5 == 0 and a % 7 == 0:
        print('a: ', a)

# Explanation
# a = 1500
# if a % 5 == 0 and a % 7 == 0:
# a % 5 == 0
# a % 7 == 0
# a % 5 =????
# / operator ---> quotient
# % operator ---> remainder
# a % 5 = 0
# a % 5 == 0 # True
# a % 7 == 0 # False
# if True and False:
# False

# range(1500, 1515, 5)
# write each step in the following way:
# a = 1500
# a % 5 = 0
# a % 5 == 0 (True) 
# a % 7 = 2
# a % 7 == 0 (False)
# a % 5 == 0 and a % 7 == 0 (False)
# print statement (not)



# if a % 5 == 0:
#     print(a)


# print('a: ', list(a))
print('-------------------------------------------------')
print(b)


# Write Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for a in  datalist:
    print(a, type(a))   
    
print('datalist: ', datalist[-1])


# type() - function
#type(datalist)
#print (type)(datalist)
#print(datalist)


# and, or, not -> logical operators

# More datatypes

# list datatype

a = [1, 2, 3, 4, 5]
b = [1,2,3,4,5, a]
# b = [1,2,3,4,5, [1,2,3,4,5]]

for i in b:
    print(i)

# tuple datatype
a = (1, 2, 3, 4, 5)

# set datatype
# has only unique values
a = {1, 2, 3, 4, 5}

# dictionary datatype
a = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': [1, 2, 3, 4, 5],
    'key4': {
        'key1': 'value1',
    }
}

a = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4
}

print(a)

list1 = [1, 2, 3, 4, 5, 5, 2]
print(set(list1)) # {1, 2, 3, 4, 5}


# Function syntax
# def <name>(<args>):
#   <statement>

def is_even(value):
    # it has to be divisible by 2
    if value % 2 == 0:
        print("Even")





    else:
        print("Odd")

is_even(12)
 

def hello(val1="Chris"):
    print("Hello", val1)


print('hi there')
hello("William")




a = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4
}

print(a.values())

# import <library>
import random

coin = random.choice(['heads','tails'])
print(coin)


# generate a random number between 0 and 100
#Choice = Variable Random.randint gives you a random interger bettween the given range as here it is 1 - 100.
choice = random.randint(1,100)
print(choice)



# number a list of numbers between 0 - 10
# random.shuffle randomizes shuffles the list
# Then we print the list

number = list(range(11))
random.shuffle(number)
print(number)


# Errors and Exceptions

# print("hello, world)

# x = int(input("What's x? "))
# print(f"x is {x}")

# try:
#   <statement>
# except:
#   <statement>


# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")


# try:
#     x = int(input("What's x?"))
# except ValueError as ne: # Runs when the try statement fails
#     pass
# else: # Runs when the try statement passes/works
#     print(f"x is {x}")

# def test_func():
#     pass



# File handling

# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(name)
# file.close()

# \n = new lines
# \t = tab


with open("names.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    print(line)
print(lines)

import pandas as pd

df = pd.read_csv('addresses.csv')
print(df)

df.to_csv('new.csv')