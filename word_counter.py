# Jaxon Terrell
# 8/4/20
# Script to print total number of words in file, top 20 most frequent words, and number of occurrences
from collections import Counter

def count_words(file):
    f = open(file, "r")
    words = f.read().strip().lower().split()
    num_words = len(words)
    top_20 = str(Counter(words).most_common(20))
    top_20 = top_20.replace("[", "")
    top_20 = top_20.replace("]", "")
    top_20 = top_20.replace("('", "")
    top_20 = top_20.replace("',", ":")
    top_20 = top_20.replace("), ", "\n\t")
    print(f'Total Words:\n\t{num_words}')
    print(f'Top 20 Words:\n\t{top_20.upper()}')