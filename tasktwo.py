from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from main import cbc_encrypt, pkcs7
from typing import Generator

KEY_SIZE = 16
#below is for task 2
AES_KEY = get_random_bytes(KEY_SIZE)
IV = get_random_bytes(KEY_SIZE)

def debug_print(message, opt=False):
    """Optional print for debugging purposes, default is false.
    Change default opt=True to print everything.
    """
    if opt:
        print(message)

def get_buf_pad(message: bytes) -> Generator[bytes, None, None]:
    """Splits the message into 16 byte blocks, adding end padding.
    """
    buf = bytearray()
    for b in message:
        buf.append(b)
        if len(buf) == 16:
            encoding = bytes(buf)
            debug_print("Block: " + str(encoding))
            yield encoding
            buf = bytearray()
    padding = pkcs7(bytes(buf))
    debug_print("Block: " + str(padding))
    yield padding

def get_buf(message: bytes) -> Generator[bytes, None, None]:
    """Splits the message into 16 byte blocks.
    Len(input) must be multiple of 16
    """
    buf = bytearray()
    for b in message:
        buf.append(b)
        if len(buf) == 16:
            yield bytes(buf)
            buf = bytearray()

def submit() -> bytes:
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
    
    ciphertext = bytearray()
    prev_cipherblock = IV
    for byte16 in get_buf_pad(byte_data):
        cipherblock = cbc_encrypt(byte16, AES_KEY, prev_cipherblock)
        ciphertext.extend(cipherblock)
        prev_cipherblock = cipherblock
    return(bytes(ciphertext))


def verify(ciphertext: bytes):
    algorithm = AES.new(AES_KEY, AES.MODE_ECB)
    
    for cipherblock in get_buf:
        prev_cipherblock = cipherblock #scope == verify(), not for-loop
        

    xor_val = xor(plaintextBlock, init_v) #xoring plaintext and init vector
    
    
    encryptedBlock = simpleCipher.encrypt(xor_val)
    

if __name__ == '__main__':
    debug_print(submit(), True)