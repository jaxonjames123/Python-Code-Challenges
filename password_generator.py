# Jaxon Terrell
# 8/6/20
# Script to generate password passphrases
from random import randint

def generate_passphrase(num_words):
    word_num = 0
    while word_num < num_words:
        numbers = []
        count = 0
        while count < 5:
            numbers.append(randint(1, 6))
            numbers_to_string = [str(number) for number in numbers]
            joined_string = "".join(numbers_to_string)
            count += 1
        check_file(joined_string)
        word_num += 1

def check_file(number_in):
    with open("diceware.txt") as file:
        line = file.readline()
        count = 1
        while line:
            if number_in in line:
                print(line[5:].strip())
            line = file.readline()
            count += 1