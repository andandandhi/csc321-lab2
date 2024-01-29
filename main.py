from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys

KEY_SIZE = 16

def file_reader():
    aes_key = get_random_bytes(KEY_SIZE)
    
    n = len(sys.argv)
    if(n < 1):
        print("Missing file name")
    
    filename = sys.argv[1]
    with open(filename, "rb") as in_file, \
         open("ecb_ciphertext", "wb") as ecb_file:
        
        ecb_file.write(in_file.read(54)) #i dont know how big bmp header is; this is guess

        buf = in_file.read(KEY_SIZE)
        while len(buf) == KEY_SIZE:
            ecb_file.write(ecb_encrypt(buf, aes_key))
            buf = in_file.read(KEY_SIZE)
        ecb_file.write(ecb_encrypt(pkcs7(buf), aes_key))

def pkcs7(buf: bytes) -> bytes:
    pad_len =  KEY_SIZE - len(buf)
    ba_buf = bytearray(buf) 
    for _ in range (pad_len):
        ba_buf.append(pad_len)
    return bytes(ba_buf)

def ecb_encrypt(plaintextBlock: bytes, aes_key: bytes) -> bytes:
    simpleCipher = AES.new(aes_key, AES.MODE_ECB)
    
    encryptedBlock = simpleCipher.encrypt(plaintextBlock)
    return(encryptedBlock)


if __name__ == '__main__':
    file_reader()

