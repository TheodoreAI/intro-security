# Mateo Estrada
# Intro to Security
# Oregon State University Ecampus
# October 26, 2021
# Test Bloom Filter: Space efficient probabilistic data structure to tell whether a given element is a member of a set.
# Application: determine whether a password given at creation is one of a large list of easily cracked passwords.
# Please install dependencies.

from bloom import BloomFilter
import sys


def get_words_txt(filename):
    '''
    object: files; its a list and I have to set the encoding 
    so that it detects special characters.
    return: list of bytes
    '''
    files = open(filename, "r", encoding='latin_1')
    words = files.read().splitlines()
    files.close()
    return words

def sample_output(bf, filename):
    '''
    class: bf; will be used to check words
    list: words; list of the words from the dictionary
    '''
    # Get the words from the sample_input
    words = get_words_txt(filename)
    # open a file and dump the outcomes
    sample_txt = open("output.txt", "w")
    for i in range(0, len(words)):
        if bf.check(words[i]):
           
            sample_txt.write('maybe \n')
        else:
            sample_txt.write('no \n')
    
    # Close the file
    sample_txt.close()
    
def print_statements(bf, words):
    '''
    class: bf; all the class methods I will need are in this object.
    list: all the words that are in the dictionary are here.
    '''
    print("Size of bit array: {}".format(bf.size))
    print("False positive Probability: {}".format(bf.fb_prob))
    print("Number of hash functions: {}".format(bf.num_hashs))
    input_count = input("Please input how many times you would like to test a password: ")
    for i in range(0, int(input_count)):
        # this will have the password we want to check against the dictionary
        input_pass = input("Please input a password:")
        if bf.check(input_pass):
            print("{} - probably already exists!".format(input_pass))
        else:
            print("{} - is definitely not used!".format(input_pass))


def main():
    # Words that will be added:
    words = get_words_txt("dictionary.txt")
    # The number of items to add
    n = len(words)
    # False positive probability
    p = 0.10
    bf = BloomFilter(n, p)
    # Add the words into the BloomFilter object
    for word in words:
        bf.add(word)
    print("To try passwords manually say 'Yes' \nTo automatically test the sample_input.txt file say 'No'")

    if input() == 'Yes':
        print_statements(bf, words)
    else:
        # Sample output of passwords that are checked against the dictionary list
        sample_output(bf, "sample_input.txt")


if __name__=='__main__':
    main()