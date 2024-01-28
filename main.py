from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.strxor import strxor


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
    
   
    

if __name__ == '__main__':
    main()

