__author__ = 'Ciaran'

from math import sqrt

def calcHyp(x, y):
    hypotenuse = sqrt(x**2 + y**2)
    return hypotenuse

def main():
    adjacent = float(input("Please enter adjacent length:"))
    opposite = float(input("Please enter opposite length:"))
    hypotenuse = calcHyp(adjacent, opposite)
    print(hypotenuse)

main()