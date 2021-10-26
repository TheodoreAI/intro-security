# Mateo Estrada Jorge
# Intro to security
# Question 3.8
# Goal: Test the weak collision (one-way-collision) 
# by building random strings of length 24 bits, and counting how many times,
# it takes for me to build random strings that will have the 
# same hash value for different messages.
# Let m1 != m2 and yet hash(m1) == hash(m2)

import random
import string as st
import hashlib
from Crypto.Hash import SHA256


def build_random_string():
    # Builds a string of length 20
    return ''.join([random.choice(st.ascii_letters + st.digits + st.punctuation) for n in range(0,20)])

def run_test(HASH_VALUE):
    count = 0
    value = True
    arr_trials = []
    while value:
        random_str = build_random_string()
        hash_object = hashlib.sha1(random_str.encode())
        # turn the hash_object into a string
        hash_string = int(hash_object.hexdigest(), 16)
        # check the first 24 bits of the hash value against HASH_VALUE
        count +=1
        string_num = str(hash_string)
        # print(string_num[0:6], HASH_VALUE, "type string_num:", type(string_num), "Type HASH_VALUE", type(HASH_VALUE))
        if string_num[0:6] == HASH_VALUE:
            arr_trials.append(count)
            print(len(arr_trials))
            count = 0
        if len(arr_trials) == 30:
            f = open("oneway_trials_table_sha1.txt", "w")
            f.write(str(arr_trials))
            f.close()
            return count


def main():
    HASH_VALUE = '342564'
    num_trials = run_test(HASH_VALUE)
    print(num_trials)
main()



#######################################################################################
#    Title: Hash Algorithm Tests
#    Author: Cui, Victor
#    Date: 2016
#    Availability: https://github.com/victorcui96/hash-algorithm-tests
#######################################################################################/