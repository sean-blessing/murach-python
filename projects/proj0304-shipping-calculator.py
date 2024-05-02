print('==================================================')
print("Shipping Calculator")
print('==================================================')

choice = "y"

while (choice.lower() != "n"):
    cost = float(input("Cost of items ordered:  "))
    if (cost <= 0):
        print("You must enter a positive number. Please try again.")
        continue

    shipping_cost = 0
    if (cost < 30):
        shipping_cost = 5.95
    elif (cost < 50):
        shipping_cost = 7.95
    elif cost < 75:
        shipping_cost = 9.95

    total_cost = cost + shipping_cost

    print(f"Shipping cost:  {shipping_cost}")
    # round() method not working correctly in 4/30 test
    print(f"Total cost:     {round(total_cost, 2)}")
    print()
    choice = input("Continue? (y/n): ")
    print('==================================================')
