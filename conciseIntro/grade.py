__author__ = 'Ciaran'

# Write a function grade(score) that returns the corresponding letter
# grade for a given numerical score. Use 90 or above for an A, 80 for a B,
# etc. Write a main() that tests your function.


def ridof(score):
    if "%" in score:
        score = int(score[0:2])
        return score
    else:
        score = int(score)
        return score

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"

def main():
    score = str(input("Enter the score that you got:"))
    score = ridof(score)
    print("Your grade is a ", grade(score))

main()