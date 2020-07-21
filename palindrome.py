# Jaxon Terrell
# 7/3/20
# Program to find whether a word or phrase is a palindrome
# Ignores case and only considers letters in the string

import re


def is_palindrome(phrase):
    forwards = []
    backwards = []
    y = 1
    for letter in phrase:
        forwards.append([letter])
        backwards.append([phrase[-y]])
        y += 1
    return forwards == backwards


def main():
    expression = re.sub('[^a-z]', '', input("Enter your word or phrase for palindrome evaluation: ").lower())
    print(is_palindrome(expression))


if __name__ == "__main__":
    main()
