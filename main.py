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
    for i in range(0,len(words)): #taking each byte in each variable and xoring
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
   
    #plaintextBlock = "16_byte_in_block"
    
    plaintextBlock = get_random_bytes(16) #in bytes
    init_v = get_random_bytes(16) #in bytes
    key = get_random_bytes(KEY_SIZE) #in bytes
    xor_val = xor(plaintextBlock, init_v) #xor_val is in bytes
    print("xor val:") #checking to see successful xor, you can remove these 2 lines
    print(xor_val)
    
    simpleCipher = AES.new(key, AES.MODE_ECB) #creating encryption algorithm with key, applying ECB

    encryptedBlock = simpleCipher.encrypt(xor_val)# applying encryption to xor val
    
    print("encrypted block:", encryptedBlock) #checking encryption
    

    decryptedBlock = simpleCipher.decrypt(encryptedBlock) #checking decryption

    print(decryptedBlock)

   


    

if __name__ == '__main__':
    #xor()
    cbc()

