from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from main import cbc_encrypt, pkcs7
from typing import Generator


KEY_SIZE = 16
#below is for task 2
aes_key = get_random_bytes(KEY_SIZE)
iv = get_random_bytes(KEY_SIZE)

def get_buf(message: bytes) -> Generator[bytes, None, None]:
    buf = bytearray()
    for b in bytes:
        if len(buf) >= 16:
            yield bytes(buf)
            buf = bytearray()
        else:
            buf.append(b)
    yield pkcs7(bytes(buf))

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
    
    for byte16 in get_buf(byte_data):
        _

    final_enc = cbc_encrypt(new_data, aes_key, iv)

    print(final_enc)

submit()