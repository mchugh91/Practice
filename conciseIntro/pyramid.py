__author__ = 'Ciaran'

def pyramid(n):
    total = 0
    for x in range(1, 1 + n):
        total += x**2
    return total

def main():
    for x in range(1, 21):
        print(pyramid(x))

main()