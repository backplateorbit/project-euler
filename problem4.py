"""
Problem 4: https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def main():
    products = [
        i * j
        for i in range(100, 1000) for j in range(100, 1000)
    ]
    palindromic = sorted(filter(
        lambda x: str(x) == str(x)[::-1],
        products
    ))
    return list(palindromic)[-1]

if __name__ == "__main__":
    print(main())