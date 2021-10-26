# Mateo Estrada Jorge
# Intro to security
# Question 3.4
# Goal: Your goal is to write a program to find out the key of an encrypted message given 
# the original message (plaintext) and the encryped (ciphertext) message.
# The message is in string hexidecimal
# The plaintext is in string format
# I need to:
#   turn the key into bytes
#   iv into bytes
#   the plaintext into bytes


import json
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from Crypto.Random import get_random_bytes

"""
If the keyword length is less than 16, 
then add spaces at the end. 
return the new keyword with the spaces at the end.
"""
def key_length(keywords):
    if len(keywords) != 16:
        for i in range(0, 16 - len(keywords)):
            keywords += ' '
    return keywords

def encrypt_msg(lines, keywords, ciphertext_str):
    # This function will encrypt the message (lines)
    # using the (keyword) and compare it to (ciphertext_str).
    encrypt_msg = ''
    for i in range(0, len(keywords)):
        if ciphertext_str == encrypt_msg:
            return keywords[i-1]
        else:
            if len(keywords[i]) > 16:
                continue
            data = str.encode(lines)
            key = bytearray(key_length(keywords[i]), encoding="utf-8")
            iv = bytearray.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
            cipher = AES.new(key, AES.MODE_CBC, iv)
            ciphertext_in_hex = cipher.encrypt(pad(data, AES.block_size)).hex()
            encrypt_msg = ciphertext_in_hex


def decrypt_msg(keys, json_input):
    # This function is used to decrypt the message and get the key by brute force.
    # Aka using a long list and trying every combination.
    for i in range(0, len(keys)):
        key_length = len(keys[i])
        key = keys[i]
        # If the word is bigger than intended
        if key_length < 16:
            for j in range(0, 16 - len(keys[i])):
                key += ' '
        try:
            b64 = json.loads(json_input)
            iv = bytearray.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
            ciphertext_str = b64["ciphertext"]
            ciphertext_bytes = bytearray.fromhex(ciphertext_str)
            print(key)
            cipher = AES.new(bytearray(key, encoding='utf-8'), AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ciphertext_bytes), AES.block_size)
            print("The message was: ", pt.decode('utf-8')) 
            return key
        except ValueError:
            print("Incorrect decryption")
        except KeyError:
            print("Incorrect decryption")

"""
Opens the plaintext file to encrypt the message.

"""
def open_plaintext_words(ciphertext_str):
    f = open("plaintext.txt", "r")
    w = open("words.txt", "r")
    plaintext = f.read()
    keywords = w.read().splitlines()
    f.close()
    w.close()
    return encrypt_msg(plaintext, keywords, ciphertext_str)
    
    
"""
Opens the words text file to compare the ciphertext 
to the encrypted text and then check for the key.

"""
def open_words():
    f = open("words.txt", "r")
    keys = f.read().splitlines()
    json_obj = '{"iv": "00000000000000000000000000000000" ,"ciphertext": "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"}'
   
    f.close()
    return  decrypt_msg(keys, json_obj)


"""
Main function that executes everything

"""
def main():
    key_word_method_1 = open_words()
    print("Test method 1 (word):", key_word_method_1)
    key_word_method_2 = open_plaintext_words('8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9')
    print("Test method 2 (word):", key_word_method_2)

main()


# This is going to check every possible word from the list and once 
# the right key is found by being able to decrypt the message,
# it will stop. I seem to be getting different results. 
# One gets method gets median and the other method gets mediate


