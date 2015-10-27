__author__ = 'Ciaran'

def distConversion(miles):
    return miles * 1.609

def main():
    for x in range(100, 1500, 100):
        print(x, "miles is equal to", distConversion(x), "kilometres")

main()