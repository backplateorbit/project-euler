"""
Problem 5: https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def main():
    i = 1
    while True:
        if all([i % a == 0 for a in range(1, 21)]):
            return i
        i += 1

if __name__ == "__main__":
    print(main())