#p.359 recursive functions
#iterative function
# def add_numbers(upper):
#     total = 0
#     for number in range(upper+1):
#         total+=number
#     return total

#recursive function
def add_numbers(upper):
    if upper == 0:
        return upper
    else:
        return upper + add_numbers(upper - 1)

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def fib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_range(n):
    fib_str = ""
    for i in range(n):
        fib_str += str(fib(i)) + ", "
    return fib_str[:-2]
        
def main():
    total = add_numbers(5)
    print(f"Total: {total}")
    print(f"Factorial 5: {factorial(5)}")
    print(f"Fibonacci(10): {fib_range(10)}")

if __name__ == "__main__":
    main()