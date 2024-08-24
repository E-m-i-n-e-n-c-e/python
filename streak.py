#  write a program to convert a list of integers into a list of their prime factors

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def prime_factors_list(lst):
    return [prime_factors(x) for x in lst]

input=input("Enter a list of integers separated by space: ").split()
lst = [int(x) for x in input]
print(prime_factors_list(lst))