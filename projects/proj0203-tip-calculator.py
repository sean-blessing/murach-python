print("Tip Calculator\n")

meal_cost = float(input("Cost of meal: "))
tip_pct = float(input("Tip percent:  "))

print()
tip_amt = round(meal_cost * (tip_pct / 100), 2)
total = round(meal_cost + tip_amt, 2)

print(f'Tip amount:    {tip_amt}')
print(f'Total amount:  {total}')




print("Bye")