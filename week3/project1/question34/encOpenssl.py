# Mateo Estrada Jorge
# Intro to security
# Question 3.4
# Goal: Your goal is to write a program to find out this key.


import json
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from Crypto.Random import get_random_bytes

def encrypt_msg(lines):
    # This function will encrypt the message from the json_input.
    # and write it to a cipher.txt file
    
    data = str.encode(lines)
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    print("the key:", type(key)== type(data))
    
    print(type(cipher.encrypt(pad(data, AES.block_size))))
    print("does it get there?")
    iv = b64encode(cipher.iv).decode('utf-8')
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv': iv, 'ciphertext':ct})
    print(result)


def decrypt_msg(lines, json_input):
    # This function is used to decrypt the message and get the key by brute force.
    # Aka using a long list and trying every combination.
    for key in range(0, len(lines)):
        key_length = len(b'lines')
        word = b'lines'
        # If the word is bigger than intended
        if key_length*8 < 128:
            for i in range(key_length, 16):
                word += '0x20'
        print(word)
        try:
            b64 = json.loads(json_input)
            iv = b64decode(b64["iv"])
            
            ct = b64decode(b64["ciphertext"])
             
            print((type(ct) == type(iv) == type(word)))
            cipher = AES.new(word, AES.MODE_CBC, iv)
           
            pt = unpad(cipher.decrypt(ct), AES.block_size())

            print("The message was: ", pt) 
        except ValueError:
            print("Incorrect decryption")
        except KeyError:
            print("Incorrect decryption")



with open("plaintext.txt", "r") as f:
    lines = f.read()
    encrypt_msg(lines)


with open("words.txt", "r") as f:
    
    lines = f.read().splitlines()
    json_obj = '{"iv": "00000000000000000000000000000000" ,"ciphertext": "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"}'
    print(type(json_obj))
    
    decrypt_msg(lines, json_obj)







# This is going to check every possible word from the list and once 
# the right key is found by being able to decrypt the message,
# it will stop.


