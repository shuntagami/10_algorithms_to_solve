# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

import collections
#Approach 1
def solution1(word):
    frequency = {}
    for i in word:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] +=1
    for i in range(len(word)):
        if frequency[word[i]] == 1:
            return i
    return -1

print(solution1('alphabet'))
print(solution1('barbados'))
print(solution1('aaaaaaa'))

print('###')

def solution2(word):
    frequency = {}
    for i in word:
        frequency.setdefault(i, 0)
        frequency[i] += 1
    for i in range(len(word)):
        if frequency[word[i]] == 1:
            return i
    return -1

print(solution2('alphabet'))
print(solution2('barbados'))
print(solution2('aaaaaaa'))

print('###')

def solution3(word):
    frequency = collections.defaultdict(int)
    for i in word:
        frequency[i] += 1
    for i in range(len(word)):
        if frequency[word[i]] == 1:
            return i
    return -1

print(solution3('alphabet'))
print(solution3('barbados'))
print(solution3('aaaaaaa'))

print('###')

#Approach 2
def solution4(word):
    # build hash map : character and how often it appears
    count = collections.Counter(word) # <-- gives back a dictionary with words occurrence count
                                         #Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    # find the index
    for idx, ch in enumerate(word):
        if count[ch] == 1:
            return idx
    return -1

print(solution4('alphabet'))
print(solution4('barbados'))
print(solution4('aaaaaaa'))
