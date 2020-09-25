"""
Problem 7: https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from sympy import isprime

def main():
    primes = []
    i = 1

    while len(primes) < 10001:
        if isprime(i):
            primes.append(i)
        i += 1

    return primes[-1]

if __name__ == "__main__":
    print(main())