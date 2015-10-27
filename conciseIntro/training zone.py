__author__ = 'Ciaran'

# function zone(age, rate) that returns a description of a persons
# training zone based on his or her age and training heart rate, rate.
# The zone is determined by comparing rate with the person's maximum
# heart rate m:
#               Training Zone
#                   rate > .90 m interval training
#           .70 m < rate < .90 m threshold training
#            .50 m < rate < .70 m aerobic training
#                    rate < .50 m couch potato
# Use the function from Exercise 3.15 to determine m. Write a main() to
# ask the user for input and display the result.



def zone(age, rate):

    m = 208 - (0.7 * age)

    if rate >= (0.9 * m):
        return "Interval Training"
    elif rate >= (.7 * m):
        return "Threshold Training"
    elif rate >= (0.5 * m):
        return "Aerobic Training"
    else:
        return "Couch Potato"

def main():
    age = int(input("Please enter your age: "))
    rate = float(input("Please enter your Heart Rate: "))
    print(zone(age, rate))

main()