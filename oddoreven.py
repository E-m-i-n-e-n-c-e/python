
n=input("Enter a number:\n")
n=int(n)
if (n%2==0):
    print("Even")
else:
    print("Odd")    
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

n = int(input("Enter the number of terms in the Fibonacci series: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(n)
    print("Fibonacci Series:")
    for number in result:
        print(number)