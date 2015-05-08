
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
        if  c not in d:
            d[c] = 1
        else:
            d[c] += 1
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


if __name__ == '__main__':

    # fin = open('words.txt')
    # words = list_to_dict(fin)
    # print 'benefit' in words

    h = histogram('brontosaurus')
    print_hist(h)
    # k = reverse_lookup(h, 2)
    # print k
    r = invert_dict(h)
    print_hist(r)
    
    
    # h = histogram('a')
    # print h
    # print h.get('a', 0)
    # print h.get('b', 0)
    
    