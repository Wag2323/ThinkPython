import random
import string
from dictionaries import histogram2


def choose_from_hist(histogram):
    """takes a histogram in the form of a dictionary (letter : count) and 
    returns a random value from the histogram that is weighted based on the
    frequency of occurrence"""
    t = []
    for key in histogram:
        for val in range(0, histogram[key]):
            t.append(key)
            
    return random.choice(t)


def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    
    return hist
  
  
def process_line(line, hist):
    line = line.replace('-', ' ')
    
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        
        hist[word] = hist.get(word, 0) + 1
  
  
if __name__ == '__main__':
    
    # h = histogram2('aab')
    # for x in range(10):
        # print choose_from_hist(h)
        
    h = hist = process_file('emma.txt')  
    for key in h:
        print key, h[key]
        