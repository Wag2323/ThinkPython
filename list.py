import random

def is_sorted(t):
    """takes a list of parameters and returns True if the list is sorted
    in ascending order"""
    for i in range(0, len(t)-1):
        if t[i] > t[i+1]:
            return False
    return True
    
def is_anagram(string1, string2):
    """Checks if the two strings can be rearranged to form the other"""
    
    """Broken doesnt work with duplicate letters in a word 
    ex. hello and heloo : could fix maybe with dict and count number of 
    occurrences to see if they match for each word"""
    
    if len(string1) != len(string2):
        return False
        
    for letter in string1:
        if not(letter in string2):
            return False
        
    return True        

def has_duplicates(t):
    """check if any element appears more than once in a sequence"""
    return len(set(t)) < len(t)
    
def rand_int_list(n, start, stop):
    """generates a random list of length n with numbers between  start and 
    stop including the start and stop"""
    t = []
    for i in range(0, n):
        t.append(random.randint(start, stop))
    return t    
    
def count_matches(length, startrange, stoprange, samples):
    """generates a set of samples of length given and checks if a duplicate
    occurs"""
    count = 0
    for i in range(0, samples):
        test = rand_int_list(length, startrange, stoprange)
        if has_duplicates(test):
            count += 1
    return count
        
    
if __name__ == '__main__':
  
    # print is_sorted([1,2,2])
    # print is_sorted(['b', 'a'])
    
    # print is_anagram('strng', 'ginrst')
    # print is_anagram('hello', 'heloo')
    
    # t = [1, 2, 3]
    # print has_duplicates(t)
    # t.append(1)
    # print has_duplicates(t)
    
    # for n in range(0, 10):
        # print rand_int_list(5, 1, 31)
        
    num_students = 23
    rangestart = 1
    rangestop = 365
    num_simulations = 1000
    count = count_matches(num_students, rangestart, rangestop, num_simulations)
    
    print 'After %d simulations' % num_simulations
    print 'with %d students' % num_students
    print 'there were %d simulations with at least one match' % count