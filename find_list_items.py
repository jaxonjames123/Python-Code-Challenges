# Jaxon Terrell
# 7/10/20
# Program to sort an input string of words, alphabetically


def index_all(search_list, item):
    index = list()
    for i in search_list:
        if search_list[i] == item:
            index.append([i])
        elif isinstance(search_list, list):
            for j in index_all(search_list[i], item):
                index.append([i] + index)
    return index

