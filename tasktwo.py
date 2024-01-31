from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys
from main import cbc_encrypt

KEY_SIZE = 16
#below is for task 2
aes_key = get_random_bytes(KEY_SIZE)
iv = get_random_bytes(KEY_SIZE)

def submit():
    words = input("Type words here: ")
    data = ""
    data = data + "userid=456;userdata="
    data = data + words #to add user words
    data = data + ";session-id=31337"
    print(data)