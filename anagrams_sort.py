# Imports the file 
file_in = open('words.txt')

# Dictionary stores the words found as anagrams 
the_dict = {}

# Max word length from a set of letters
max_length = 0

""" 
Iterate through every word in the file

1.) Strips off white spaces
2.) Sorts words in alphabetical format 
3.) Makes "key" of the sorted words

"""

for grams in file_in:
    tuple_testing = ()
    word = grams.strip() 
    tuple_testing = tuple(sorted(word))
    # Checks for the sorted key and if found; adds it as "object" in the_dict
    if tuple_testing in the_dict: 
        the_dict[tuple_testing].append(word)
        # Checks for the length of the word; if max, that's stored as the max length.  
        if len(the_dict[tuple_testing]) >= max_length: 
                max_length = len(the_dict[tuple_testing])
    # Adds new words in the tuple
    else: 
        the_dict[tuple_testing] = [word]

test_length = max_length
my_anagrams = 0

"""
Iterates through every word in the dictionary stored as a key

1.) Search for same length keys and find its duplicates and print them. 
2.) Prints them in descending order of length 

"""

for i in range (max_length):
    for anagram in the_dict:    
        if (len(the_dict[anagram]) == test_length) and (len(the_dict[anagram]) > 1):            
            print (the_dict[anagram]) # Prints all words with anagram property
            my_anagrams +=1
    test_length -=1


print ("Total anagrams found:", (my_anagrams))
