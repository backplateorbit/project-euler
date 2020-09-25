"""
Problem 3: https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from sympy import isprime

def main():
    number = 600851475143
    factors = [i for i in range(1, int((number + 1) ** 0.5)) if number % i == 0]
    prime_factors = filter(lambda x: isprime(x), factors)
    return list(prime_factors)[-1]
    

if __name__ == "__main__":
    print(main())