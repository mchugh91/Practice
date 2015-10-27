__author__ = 'Ciaran'

def triangular(n):
    total = 0
    for x in range(1, n+1):
        total += x
    return total


def main():
    for n in range(1,21):
        print(triangular(n))



main()



