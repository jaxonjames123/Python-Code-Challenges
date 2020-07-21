# Jaxon Terrell
# 7/3/20
# Program to find all prime factors of a number


def prime_getter(x):
    factors = []
    y = 2
    while y <= x:
        if x % y != 0:
            y += 1
        if x % y == 0:
            x = x / y
            factors.append(y)
    return factors


def main():
    number = int(input("Enter your value so I can determine the prime factors: "))
    print(prime_getter(number))


if __name__ == "__main__":
    main()
