from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from main import cbc_encrypt, pkcs7, xor
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
    Does NOT remove padding. 
    TODO: remove padding.
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

def submit_manual_input(words: str) -> bytes:
    """Same as submit(), but with args instead of input.
    Used to work on hack(), delete this function when finished.
    """
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
    data = data + new_words
    data = data + ";session-id=31337"
    byte_data = data.encode('utf-8')
    
    ciphertext = bytearray()
    prev_cipherblock = IV
    for byte16 in get_buf_pad(byte_data):
        cipherblock = cbc_encrypt(byte16, AES_KEY, prev_cipherblock)
        ciphertext.extend(cipherblock)
        prev_cipherblock = cipherblock
    return(bytes(ciphertext))


def cbc_decrypt(ciphertext: bytes) -> str:
    """Decrypts CBC ciphertext.
    Does NOT remove padding. 
    """
    algorithm = AES.new(AES_KEY, AES.MODE_ECB)    
    decrypted_bytearray = bytearray()
    prev_cipherblock = IV
    for cipherblock in get_buf(ciphertext):
        aes_out = algorithm.decrypt(cipherblock)
        plainblock = xor(aes_out, prev_cipherblock)
        decrypted_bytearray.extend(plainblock)
        prev_cipherblock = cipherblock
    return decrypted_bytearray.decode('utf-8', errors='ignore')

def verify(ciphertext: bytes) -> bool:
    plaintext = cbc_decrypt(ciphertext)
    return plaintext.find(';admin=true') != -1

def hack():
    encrypted_message=submit_manual_input('9admin9true')
    em_ba = bytearray(encrypted_message)
    em_ba[4] = em_ba[4] ^ (1 << 1) #index on bytearray returns int
    em_ba[10] = em_ba[10] ^ (1 << 2)
    # userid=456;userd
    # ata=9admin9true5
    # '9' + 0x02 = ';'   '9' + 0x04 = '='
    # add 2 to 5th byte, add 4 to 11th byte
    malcious_msg = em_ba
    debug_print(cbc_decrypt(malcious_msg), True)
    print(verify(malcious_msg))

if __name__ == '__main__':
    #encrypted_message = submit()
    #debug_print(encrypted_message)
    #debug_print("\n"+cbc_decrypt(encrypted_message), True)
    hack()