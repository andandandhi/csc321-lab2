
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

data = 'secret data to transmit'.encode()

words = "asdfghjklqwertyu"

#can use pycryptodome's ciper to do decryption



def get_aes_key():
    get_random_bytes(16)
#block size is exactly 16 and block size is less than 16
    #can have fixed string and test that
def main():
    print("hello")
    
    aes_key =  get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_ECB)

    #how do we XOR the aes key with words (our plaintext)
    print(cipher) #returning object location and not the legible cipher



 
    

#in order to XOR character into byte, convert character into ascii (ord or char)
   
   
if __name__ == '__main__':
    main()
    
