import random
from structshape import structshape
from dictionaries import histogram2


def sumall(*args):
    nums = args
    sum = 0
    for n in nums:
        sum += n

    return sum


def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True

    return False


def sort_by_length(words):
    """Sort a list of words in reverse order by length with matching lengths
    have a random ordering

    words: list of strings
    returns: list of strings
    """
    t = []
    for word in words:
        t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    result = []
    for length, num, word in t:
        result.append(word)

    return result


def most_frequent(string):
    """Sort a string by decreasing order of frequency

    string: a set of characters
    returns: list with count of characters
    """
    s = string.lower()
    d = histogram2(s)
    t = []
    for key in d:
        t.append((d[key], key))

    t.sort(reverse=True)

    return t


def signature(s):
    """Returns a string of the string with all letters in order"""
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def list_anagrams(filename):
    """takes an file holding one text per line and returns a list of words
    that are anagrams of each other
    """
    dict = {}
    for line in open(filename):
        word = line.strip().lower()
        sig = signature(word)

        if sig not in dict:
            dict[sig] = [word]
        else:
            dict[sig].append(word)

    return dict


def print_anagram_sets_in_order(d):
    t = []
    for val in d.values():
        if len(val) > 1:
            t.append((len(val), val))

    t.sort()

    for x in t:
        print x


if __name__ == "__main__":

    # print sumall(1, 2, 3, 4 ,5)
    # print sumall(1, 2, 3, 5)

    # words = ['John', 'Joe', 'Ralph', 'Randy', 'Mike', 'Michael']
    # t = sort_by_length(words)
    # for x in t:
        # print x

    # s = 'Testing Testing 1 2 3'
    # t = most_frequent(s)
    # print structshape(t)
    # for x in t:
        # print x

    d = list_anagrams('words.txt')
    print_anagram_sets_in_order(d)
