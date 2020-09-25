"""
Problem 6: https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def main():
    sum_squares = sum([
        i**2 for i in range(1, 101)
    ])

    square_of_sum = sum([i for i in range(1, 101)]) ** 2

    return square_of_sum - sum_squares

if __name__ == "__main__":
    print(main())