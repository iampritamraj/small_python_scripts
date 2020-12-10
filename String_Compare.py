"""There are many methods of comparing string in python. Some of the main methods are:

Using regex

Simple compare Using difflib

But one of the very easy method is by using fuzzywuzzy library where we can have a score out of 100, 
that denotes two string are equal by giving similarity index.

FuzzyWuzzy is a library of Python which is used for string matching. Fuzzy string matching is the process of

finding strings that match a given pattern.
"""
# Python code showing all the rattos together,

# make sure you have installed fuzzywuzzy module

from fuzzywuzzy import fuzz

from fuzzywuzzy import process

s1 = "I love copytest" 
s2 = "I am loving copytest"

print("FuzzyWuzzy Ratto: ",

fuzz.ratio(s1, s2)) 
print("FuzzyWuzzy PartialRatio: ",fuzz.partial_ratio(s1, s2))

print("Fuzzywuzzy TokenSortRatto: ", fuzz.token_sort_ratio(s1, s2))

print("FuzzyWuzzy TokenSetRatto: ",fuzz.token_set_ratio(s1, s2))

print("FuzzyWuzzy WRatio: ", fuzz.WRatio(s1, s2))

# for process library, 
query = "copytest new"

choices = ['copyas test new', 'copyass the words', 'assignment python' ]

print("List of ratios: ") 
print(process.extract(query, choices)) 
print("Best among the above list: ",process.extractOne( query, choices))