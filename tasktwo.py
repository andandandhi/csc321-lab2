from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys
from main import cbc_encrypt, pkcs7

KEY_SIZE = 16
#below is for task 2
aes_key = get_random_bytes(KEY_SIZE)
iv = get_random_bytes(KEY_SIZE)

def submit():
    words = input("Type words here: ")
    new_words = ""
    for i in words:
        if i == "=":
            new_words = new_words + "%3D"
        elif i == ";":
            new_words = new_words + "%3B"
        else:
            new_words = new_words + i
    data = ""
    data = data + "userid=456;userdata="
    data = data + new_words #to add user words
    data = data + ";session-id=31337"
    byte_data = data.encode('utf-8')
    new_data = pkcs7(byte_data)
    final_enc = cbc_encrypt(new_data, aes_key, iv)

    print(final_enc)

submit()