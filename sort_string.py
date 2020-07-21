# Jaxon Terrell
# 7/9/20
# Program to sort an input string of words, alphabetically


def sort_string():
    phrase = input(str("Type input phrase here: "))
    words = phrase.split()
    sorted_words = sorted(words, key=str.casefold)
    print(' '.join(sorted_words))


if __name__ == "__main__":
    sort_string()
