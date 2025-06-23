"""
print("Hello Guys!\nThis is a sample text coming from my code")
print('I am trying something new')


print("Printing Pattern 01: ")
# # # #
# # # #
# # # #
# # # #

for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()


print("Printing Pattern 02: ")
#
# #
# # #
# # # #

for i in range(5):
    for j in range(i):
        print("# ", end="")
    print("")

print("Printing Pattern 03: ")
# # # #
# # #
# #
#

for i in range(4):
    for j in range(4 - i):
        print("# ", end="")
    print("")

print("Completed the Patterns")

# 1. Finding Prime Numbers
print("Trying Find Prime Numbers")

number = int(input("Enter a Integer number (1-100): "))
print("Entered Number is %s" % number)

for i in range(2, number):
    if number % i == 0:
        print(f"Entered Number is '{number}' not prime number, Sorry!!")
        break
else:
    print("Hola!! Entered number is a prime number.")
"""

# from array import array
from array import *

# values = array('i', [5, 4, 6, 7, 3, 1])
values = array('u', ['a', 'h', 'c', 'b', 'r', 'p'])
print("In single print: ", values)
print("Value present in Index '2':", values[2])

print("Printing with range given: ")
for i in range(6):
    print(values[i])

print("Printing with the variable given: ")
for i in values:
    print(i)

# Creating new Array with old Array
newArray = array(values.typecode, (a for a in values))
print("Newly Created Array 'newArray' values: ", newArray)




print("Exiting, bye!!")
