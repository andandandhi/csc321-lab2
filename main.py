from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.strxor import strxor

words = "asdfghjklqwertyu"

#can use pycryptodome's ciper to do decryption

def main():
    data = 'secret data to transmit'.encode()

    #padding not done, len 16 should be different
    len16 = len(data) // 16

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


    aes_key = get_random_bytes(16)
    ciphertext = b''

    for i in range (len16):
        ciphertext += strxor(aes_key, data[i : i+16])
    
    print(ciphertext)
    

 
    

#in order to XOR character into byte, convert character into ascii (ord or char)
   
   
if __name__ == '__main__':
    main()
<<<<<<< HEAD
    
=======
>>>>>>> 88973225fe2ff0870b01d35c708b81affac5d993
