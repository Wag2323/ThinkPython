
def count_letters(word, n):
    """Takes a word and counts if it has at least n number of characters"""
    if len(word) > n-1:
        return True
    else:
        return False
    

def word_w_length(object, n):
    """takes an object holding one text word per line and returns a list of
    words that are at least n characters long"""
    list = []
    for line in object:
        word = line.strip()
        if count_letters(word, n):
            list.append(word)
    return list
    
def has_no_letter(word, letter):
    """takes a word and returns true if it does not have the specified letter
    in the word"""
    for char in word:
        if char == letter:
            return False
    return True
    
def list_wo_letter(object, letter):
    """takes an object holding one text word per line and returns a list of 
    words with out the specified letter and also returns the percentage of 
    words from the list without that letter"""
    list = []
    countlines = 0
    for line in object:
        word = line.strip()
        if has_no_letter(word, letter):
            list.append(word)
        countlines = countlines + 1
    
    length = len(list)
    percentage = float(length) / float(countlines) * 100.00

    return (list, percentage)    
    
def avoid(object, string):
    """gives a list of words that do not contain any letter from the string"""
    list = []
    innerlist = []
    #creates the first list 
    innerlist, pct = list_wo_letter(object, string[0])
    #loops the other letters
    if len(string) < 2:
        list = innerlist
    else:
        for letter in string[1:]:
            list, pct = list_wo_letter(innerlist, letter)
            innerlist = list
    
    count = len(list)
    return (list, count)
    
def is_abecedarian(word):
    """returns True if letters in a word are in alphabetical order"""
    lower = word.lower()
    for i in range(0,len(lower)-1):
        if lower[i] > lower[i+1]:
            return False
    return True    
      
def abecedarian_list(object):
    """gives a list of words that are abecedarian"""
    list = []
    for line in object:
        word = line.strip()
        if is_abecedarian(word):
            list.append(word)
    
    count = len(list)
    return (list, count)

if __name__ == '__main__':
    
    # print count_letters('hello', 3)
    # print count_letters('hello', 6)
    # print count_letters('testthis', 5)
    # print count_letters('testthis', 8)
    
    fin = open('words.txt')
    # print word_w_length(fin, 20)
    
    # words = ['hello', 'test', 'chicken']
    # letters = ['e', 'h', 's', 'c']
    # for word in words:
        # for letter in letters:
            # value = has_no_letter(word, letter)
            # print 'Does %s have no letter %s?' %(word, letter),
            # print value
    
    # letter = 'e'
    # list, percentage = list_wo_letter(fin, letter)
    # print list, '\n'
    # print '%.2f percent of words from the list do not have %s' %(percentage,letter)
    
    # string = 'e'
    # list, count = avoid(fin, string)
    # print list, '\n'
    # print count
    
    # list, count = abecedarian_list(fin)
    # print list
    # print count    