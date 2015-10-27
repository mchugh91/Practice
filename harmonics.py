__author__ = 'Ciaran'



def harmonic(n):
    # Compute the sum of 1/k for k=1 to n.
    total = 0
    for k in range(1, n + 1):
        total += 1 / k
    return total

def main():
    n = int(input("Enter a positive integer: "))
    decimel = format(harmonic(n), ".5f")
    print("The sum of 1/k for k = 1 to", n, "is", decimel)

main()

print((1/1)+(1/2)+(1/3)+(1/4)+(1/5)+(1/6))

for i in range(1, 10):
        i = 1
        if surf == vol:
            print(i)
            break
