print("Paycheck Calculator")

tax_rate = 18
hours_worked = float(input("Hours worked:     "))
hourly_pay_rate = float(input("Hourly pay rate:  "))

gross_pay = round(hours_worked * hourly_pay_rate, 2)
tax_amount = round(gross_pay * (tax_rate / 100), 2)
take_home_pay = round((gross_pay - tax_amount), 2)

print(f'Gross pay:       {gross_pay}')
print(f'Tax rate:        {tax_rate}%')
print(f'Tax amount:      {tax_amount}')
print(f'Take home pay:   {take_home_pay}')
print("Bye")