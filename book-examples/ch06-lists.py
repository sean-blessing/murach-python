temps = [48.0, 30.5, 20.2, 100.0, 42.0]
inventory = ["staff", "hat", "shoes"]
movie = ["The Holy Grail", 1975, 9.99]
test_scores = []

# repetition operator *
scores = [0]*5
print(f'scores: {scores}')

# index positions
print(f'{temps[0]} {temps[-5]}')
print(f'{temps[1]} {temps[-4]}')
print(f'{temps[2]} {temps[-3]}')
print(f'{temps[3]} {temps[-2]}')
print(f'{temps[4]} {temps[-1]}')
# print(f'{temps[5]} {temps[-6]}') index out of range

# p. 167 - modifying a list
temps.append(99.5)
print(temps)
temps.insert(2,40.0)
print(temps)
temps.remove(20.2)
print(temps)
temps.pop()
print(temps)
temps.pop(2)
print(temps)
print(temps.index(100.0))
print("for loop...")
for item in temps:
    print(item)
for i in range(len(temps)):
    print(f'i[{i}]: {temps[i]}')

seven_dwarfs = ["Dopey", "Grumpy", "Bashful", "Sneezy", "Sleepy", "Happy", "Doc"]
seven_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# process both lists using zip
for dwarf, day in zip(seven_dwarfs, seven_days):
    print(f'{dwarf}, {day}')

# p. 185 count, reverse, sort lists
num_list = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
count = num_list.count(14)
print(f'count: {count}')
print(f'num_list: {num_list}')
num_list.reverse()
print(f'num_list.reverse(): {num_list}')
num_list.sort()
print(f'num_list.sort(): {num_list}')
letters = ["a", "b", "C", "d", "E"]
print(f'letters: {letters}')
letters.sort()
print(f'letters: {letters}')
letters.sort(key=str.lower)
print(f'letters: {letters}')

# p. 187
minimum = min(num_list)
maximum = max(num_list)
total1 = sum(num_list)
total2 = sum(num_list, start=100)
print('min {minimum} max {maximum} sum {sum}')
import random
choice = random.choice(num_list)
print(f'random.choice= {choice}')
random.shuffle(num_list)
print(f'num_list: {num_list}')

# p. 189 deep copy of a list 
import copy
num_list_2 = copy.deepcopy(num_list)
num_list_3 = [2, 4, 6, 8, 10, 12]
print(f'num_list_3: {num_list_3}')
print(f'num_list_3[0:2]: {num_list_3[0:2]}')
print(f'num_list_3[:2]: {num_list_3[:2]}')
print(f'num_list_3[:3]: {num_list_3[:3]}')
print(f'num_list_3[4:]: {num_list_3[4:]}')
print(f'num_list_3[0:4:2]: {num_list_3[0:4:2]}')
print(f'num_list_3[0:4]: {num_list_3[0:4]}')
print(f'num_list_3[::-1]: {num_list_3[::-1]}')

# p. 191 map, filter, reduce
num_list = [1,2,3,4,5,6]
def square(n):
    return n*n

squares = map(square, num_list)
print(f'num_list: {num_list}')
print(f'squares: {squares}')
print(f'list(squares): {list(squares)}')

def is_even(n):
    return n % 2 == 0

evens = filter(is_even, num_list)
evens = list(evens)
print(f'evens: {evens}')

import functools
def add_square(total, current):
    return total + (current*current)

print(f'num_list used in next examples: {num_list}')
total = functools.reduce(add_square, num_list)
print(f'total: {total}')
total = functools.reduce(add_square, num_list, 10)
print(f'total: {total}')
#total = functools.reduce(add_square, num_list, start=10)
#print(f'total: {total}')

#list comprehension
print("** list comprehensions **")
print(f'num_list used in next examples: {num_list}')
squares = []
for n in num_list:
    squares.append(n*n)
print(f'squares:        {squares}')
squares_1 = [n * n for n in num_list]
print(f'squares_1:      {squares_1}')
even_squares = [n*n for n in num_list if n % 2 == 0]
print(f'even_squares:   {even_squares}')
def square(n):
    return n*n
def is_even(n):
    return n % 2 == 0
even_squares_2 = [square(n) for n in num_list if is_even(n)]
print(f'even_squares_2: {even_squares_2}')

def get_number():
    return random.randrange(1, 10)

squares_2 = [square(num) for n in range(10) if (num := get_number()) <= 6]
print(f'squares_2: {squares_2}')

# p. 195 tuples
print("** tuples **")
stats = (48.0, 30.5, 20.2, 100.0, 48.0)
herbs = ("lavender", "pokeroot", "chamomile", "valerian", "nettles", "oatstraw")
movie = ("Monty Python and the Holy Grail", 1975, 9.99)

print(f'herbs[0]:   {herbs[0]}')
print(f'herbs[-1]:   {herbs[-1]}')
print(f'herbs[1:4]:   {herbs[1:4]}')
# herbs[1] = "abc"
title, year, price = movie;
print(f'{title}, {year}, {price}')

def get_nums():
    x = 1
    y = 5
    z = 10
    return x, y, z

a, b, c = get_nums()
print(f'{a}, {b}, {c}')


