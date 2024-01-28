from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys

def file_reader():
    n = len(sys.argv)
    if(n < 1):
        print("Missing file name")
    
    filename = sys.argv[1]
    with open(filename, "rb") as file:
        buf = file.read(16)
        while len(buf) == 16:
            a = ecb_encrypt(buf)
            buf = file.read(16)        
        a = ecb_encrypt(pkcs7(buf))

def pkcs7(buf: bytes) -> bytes:
    pad_len =  16 - len(buf)
    return pad_len.to_bytes(2, 'big') * pad_len


def get_aes_key():
    get_random_bytes(16)

def ecb_encrypt(plaintextBlock: bytes, aes_key: bytes) -> bytes:
    KEY_SIZE = 16   
    plaintextBlock = "16_byte_in_block"
    aes_key = get_random_bytes(16)
    simpleCipher = AES.new(aes_key, AES.MODE_ECB)
    
    
    encryptedBlock = simpleCipher.encrypt(bytes(plaintextBlock, 'utf-8')) # must cast string to bytes for encryption
    
    print("original block:", plaintextBlock)
    print("encrypted block:", encryptedBlock)
    print("\nperforming decryption:")
    
    decryptedBlock = simpleCipher.decrypt(encryptedBlock)
    print(decryptedBlock.decode('utf-8'))
    #plaintexttwo = str(decryptedBlock)
# What is decryptedBlock? String or bytes?
    #print(plaintexttwo)

    

    #padding not done, len 16 should be different
    
   
    

if __name__ == '__main__':
    main()

