
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

data = 'secret data to transmit'.encode()




def get_aes_key():
    get_random_bytes(16)

def main():
    


if __name__ == '__main__':
    aes_key =  get_aes_key()
