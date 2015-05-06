
def find_index(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index

        index = index + 1

    return -1


if __name__ == '__main__':

    print find_index('hello', 'o', 0)
    print find_index('adyfabfadfefjlafdnybeidahgbdb', 'y', 4)
