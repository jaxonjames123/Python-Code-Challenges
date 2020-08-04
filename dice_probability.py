# Jaxon Terrell
# 8/3/20
# Program to simulate rolling dice 1,000,000 times to find out the
# probability of a certain outcome when rolling the dice (Monte Carlo Method)
from random import randint
from collections import Counter


def probability(*dice, trials=1_000_000):
    count = Counter()
    for roll in range(trials):
        count[sum((randint(1, sides) for sides in dice))] += 1
    print("\nOUTCOME\tPROBABILITY")
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome, count[outcome]*100/trials))
