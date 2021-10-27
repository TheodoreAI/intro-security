# Mateo Estrada
# Intro to Security
# Oregon State University Ecampus
# October 26, 2021
# Bloom Filter: Space efficient probabilistic data structure to tell whether a given element is a member of a set.
# Application: determine whether a password given at creation is one of a large list of easily cracked passwords.
# Please install dependencies.
import math
import mmh3
from bitarray import bitarray

class BloomFilter(object):

    '''
    Class for Bloom Filter, using murmur3 hash function, since this is some of the fastest hash functions to use.'''

    def __init__(self, num_items, fb_prob):
        '''
        num_items: int; number of items to be stored in bloom filter
        fb_prob: float; False positive probability in decimal'''

        self.fb_prob = fb_prob

        # size of bit array to use
        self.size = self.get_size(num_items, fb_prob)

        # number of hash functions to use
        self.num_hashs = self.get_num_hashs(self.size, num_items)

        # bit array of given size
        self.bit_array = bitarray(self.size)

        # initialize all bits as 0
        self.bit_array.setall(0)

    def add(self, item):
        '''
        Adding item into the filter
        '''
        digests = []
        for i in range(0, self.num_hashs):
            # each item has different digest
            # now to use the hash function on the items
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)
            # set a bit to true in the self.bit_array
            self.bit_array[digest] = True
    def check(self, item):
        '''
        Check for existance of an item in filter
        '''
        for i in range(0, self.num_hashs):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                # if any of bit is Flase them its not present
                # in the filter else there is probability that it exist
                return False
        return True

    @classmethod
    def get_size(cls, n, p):
        '''
        Return the size of bit array m to use with the following formula:
        m = -(n*ln(p))/(ln(2)^2)
        n: int
        p: float
        '''
        m = -(n*math.log(p))/(math.log(2)**2)

        return int(m)
    @classmethod
    def get_num_hashs(cls, m, n):
        '''
        Return the hash function (k) to be used using the following formula:
        k = (m/n)*ln(2)
        m: size of bit array
        n: number of items expected to be stored.
        '''
        k = (m/n)*math.log(2)
        return int(k)


#######################################################################################
#    Title: Bloom Filters - Introduction and Implementation
#    Author: Geeksforgeeks.org
#    Date: 28 Jun, 2021
#    Availability: https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
#######################################################################################/
