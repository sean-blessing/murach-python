#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

choice = "y"
while choice.lower() == "y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_gallon = float(input("Cost of gas per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_gallon <= 0:
        print("Cost of gas must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        print("Miles Per Gallon:          ", mpg)
        total_cost = gallons_used * cost_gallon
        print("Total cost of gas:         ", total_cost)
        cost_per_mile = total_cost / miles_driven
        print("Cost per mile:             ", cost_per_mile)
    choice = input("Continue?(y/n): ")

print()
print("Bye!")



