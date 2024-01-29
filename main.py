from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.strxor import strxor
#import sys.argv

def get_aes_key():
    get_random_bytes(16)

def main():
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
    plaintextBlock = "7AFD39E82B4A6FC1D70E9B3F8C12D5A6"
    
    init_v = "4F8D3E72A91B5C6EF20A9D4B1E73FBCD"
    #plaintextBlock = "16_byte_in_block"
    
    plaintextBlock = get_random_bytes(16)
    init_v = get_random_bytes(16)
    xor_val = xor(plaintextBlock, init_v)
    print("xor val:")
    print(xor_val)
    
    simpleCipher = AES.new(xor_val, AES.MODE_ECB)
    #encryptedBlock = simpleCipher.encrypt(bytes(plaintextBlock, 'utf-8'))
    print(simpleCipher)
    #encryptedBlock = simpleCipher.encrypt(bytes(str(xor_val), 'utf-8')) # must cast string to bytes for encryption
    
   
   # print("encrypted block:", encryptedBlock)
    #word = conversion(plaintextBlock)
   
    #print(word)

    

if __name__ == '__main__':
    #xor()
    cbc()

