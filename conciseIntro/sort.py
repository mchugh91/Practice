__author__ = 'Ciaran'

from random import randint


# Write a function sort3(x, y, z) that returns the three values x, y, and z
# in sorted order (a, b, c), where a  b  c. Do not use any built-in
# Python sorting functions, but you may put if statements inside of other
# if statements. Write a main() that thoroughly tests your function.

def sort3(x, y, z):
    if x > y and x > z and y > z:
        return (z, y, x)
    elif x > y and x > z and z > y:
        return (y, z, x)
    elif y > x and x > z:
        return (z, x, y)
    elif y > x and y > z:
        return (x, z, y)
    elif z > x and x > y:
        return (y, x, z)
    else:
        return (x, y, z)

def main():
    for x in range(0,10):
        x = randint(0,1000)
        y = randint(0,1000)
        z = randint(0,1000)
        print(x, y, z)
        print(sort3(x, y, z))

main()


