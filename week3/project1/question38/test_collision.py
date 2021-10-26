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

def run_test_strong():
    count = 0
    value = True
    arr_trials = []
    while value:
        random_str_1 = build_random_string()
        random_str_2 = build_random_string()
        hash_object_1 = hashlib.sha1(random_str_1.encode())
        hash_object_2 = hashlib.sha1(random_str_2.encode())

        # turn the hash_object into a string
        hash_string_1 = int(hash_object_1.hexdigest(), 16)
        hash_string_2 = int(hash_object_2.hexdigest(), 16)
        hash_str_1 = str(hash_string_1)
        hash_str_2 = str(hash_string_2)
        # check the first 24 bits of the hash value against HASH_VALUE
        # print("One", hash_str_1, "two", hash_str_2)
        count +=1
        if hash_str_1[0:6] == hash_str_2[0:6]:
            arr_trials.append(count)
            print(len(arr_trials))
            count = 0
        if len(arr_trials) == 30:
            f = open("table_trials_collision_sha1.txt", "w")
            f.write(str(arr_trials))
            f.close()
            return count



def main():
    HASH_VALUE = '286755'
    num_trials = run_test_strong()
    print("The number of trials", num_trials)


main()