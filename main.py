from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys

KEY_SIZE = 16

def file_reader():
    aes_key = get_random_bytes(16)
    
    n = len(sys.argv)
    if(n < 1):
        print("Missing file name")
    
    filename = sys.argv[1]
    with open(filename, "rb") as in_file, \
         open("ecb_ciphertext", "wb") as ecb_file:
        buf = in_file.read(KEY_SIZE)
        while len(buf) == KEY_SIZE:
            ecb_file.write(ecb_encrypt(buf, aes_key))
            buf = in_file.read(KEY_SIZE)        
        ecb_file.write(ecb_encrypt(pkcs7(buf)))

def pkcs7(buf: bytes) -> bytes:
    pad_len =  KEY_SIZE - len(buf)
    return pad_len.to_bytes(2, 'big') * pad_len

def ecb_encrypt(plaintextBlock: bytes, aes_key: bytes) -> bytes:
    simpleCipher = AES.new(aes_key, AES.MODE_ECB)
    
    encryptedBlock = simpleCipher.encrypt(plaintextBlock)
    print("original block:", plaintextBlock)
    print("encrypted block:", encryptedBlock)
    print("\nperforming decryption:")
    decryptedBlock = simpleCipher.decrypt(encryptedBlock)
    print(decryptedBlock)


if __name__ == '__main__':
    file_reader()

