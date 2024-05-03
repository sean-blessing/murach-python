balance = 100.10
balance += 100.10
balance += 100.10
print(f"balance = {balance}")
balance = round(balance, 2)
print(f"balance = {balance}")

#p. 259 Math module
import math as m
#How to use the pow() and sqrt() functions 
result = m.pow(2, 3)
print(f"result = {result}")
result = m.sqrt(16) 
print(f"result = {result}")
result = m.pow(125, 1/3)
print(f"result = {result}")
#How to use the pi constant 
radius = 12
circumference = m.pi * radius * 2 
print(f"circumference: {circumference}")
area = m.pi * m.pow(radius, 2) 
print(f"area: {area}")
area = m.pi * radius**2
print(f"area: {area}")

#How to use the floor() and ceil() functions 
result = m.floor(12.545)
print(f"result = {result}")
result = m.ceil(12.545) 
print(f"result = {result}")
result = m.floor(-3.432) 
print(f"result = {result}")
result = m.ceil(-3.432)
print(f"result = {result}")

#How to use the ceil() function to work with decimal places 
result = m.ceil(2.0083)
print(f"result = {result}")
result = m.ceil(2.0083 * 10) / 10 
print(f"result = {result}")
result = m.ceil(2.0083 * 100) / 100
print(f"result = {result}")

#How to use the floor() function to work with decimal places 
result = m.floor(2.0083)
print(f"result = {result}")
result = m.floor(2.0083 * 10) / 10 
print(f"result = {result}")
result = m.floor(2.0083 * 1000) / 1000
print(f"result = {result}")

#p. 261 f strings to format numbers
print("floating point number formatting")
fp_number = 12345.6789 
print(f"{fp_number:.2f}") 
print(f"{fp_number:,.2f}") 
print(f"{fp_number:15,.2f}") 
print(f"{fp_number:.2e}")
fp_number = .12345 
print(f"{fp_number:.0%}") 
print(f"{fp_number:.1%}")
int_number = 12345 
print(f"{int_number:d}") 
print(f"{int_number:,d}")
# How to format a string literal 
print(f"{'Description':15}")
spec = 15
print(f"{'Description':{spec}}") # enclose the variable in brackets
#How to use field widths to align results 
print(f"{'Description':15} {'Price':>10} {'Qty':>5}") 
print(f"{'Hammer':15} {9.99:10.2f} {3:5d}")
