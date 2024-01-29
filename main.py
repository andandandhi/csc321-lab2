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
    #padding not done, len 16 should be different

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

def conversion(word):
    conversion = ""
    for i in word:
        con = ord(i)
        conversion = conversion  + str(con)
    conversion  = int(conversion)
    return conversion

#words, iv)
def xor(words, iv):
   # words = get_random_bytes(16)
   # iv = get_random_bytes(16)
    print(iv)
    code = b""
    for i in range(0,len(words)):
        byte_1 = words[i]
        byte_2 = iv[i]
        xor_val = bytes([byte_1 ^ byte_2])
        code = code + xor_val
    print(code)
    print(len(iv))
    print(len(code))
    return code


def cbc():
    KEY_SIZE = 16 
    
    plaintextBlock = get_random_bytes(16)
    init_v = get_random_bytes(16)
    key = get_random_bytes(KEY_SIZE)
    xor_val = xor(plaintextBlock, init_v)
    print("xor val:")
    print(xor_val)
    
    simpleCipher = AES.new(key, AES.MODE_ECB)
    print(simpleCipher)
    encryptedBlock = simpleCipher.encrypt(xor_val)# must cast string to bytes for encryption
    
    print("encrypted block:", encryptedBlock)
    #word = conversion(plaintextBlock)

    decryptedBlock = simpleCipher.decrypt(encryptedBlock)
    print(decryptedBlock)

   
    #print(word)

    

if __name__ == '__main__':
    file_reader()
    #xor()
    cbc()

