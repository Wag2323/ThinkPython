import time


def list_to_dict(object):
    """Takes an object holding one text word per line and returns a dictionary
    with the words as the keys for searching"""
    dict = {}
    for line in object:
        word = line.strip()
        dict[word] = word

    return dict


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram2(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1

    return d


def print_hist(h):
    for c in h:
        print c, h[c]


def reverse_lookup(d, v):
    keys = []
    for k in d:
        if d[k] == v:
            keys.append(k)

    return keys


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)

    return inverse


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


known = {0: 0, 1: 1}


def fibonacci2(n):
    if n in known:
        return known[n]
    result = fibonacci2(n-1) + fibonacci2(n-2)
    known[n] = result

    return result

if __name__ == '__main__':

    # fin = open('words.txt')
    # words = list_to_dict(fin)
    # print 'benefit' in words

    # h = histogram('brontosaurus')
    # print_hist(h)
    # h2 = histogram2('brontosaurus')
    # print_hist(h2)
    # k = reverse_lookup(h, 2)
    # print k
    # r = invert_dict(h)
    # print_hist(r)

    # h = histogram('a')
    # print h
    # print h.get('a', 0)
    # print h.get('b', 0)

    # Fibonacci variants
    # start_time = time.time()
    # for n in range(0, 35):
        # print fibonacci(n)
    # elapsed_time = time.time() - start_time
    # print elapsed_time, 'seconds'

    start_time = time.time()
    for n in range(998, 1000):
        print fibonacci2(n)
    elapsed_time = time.time() - start_time
    print elapsed_time, 'seconds'
