from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.strxor import strxor


def main():
    data = 'secret data to transmit'.encode()

    #padding not done, len 16 should be different
    len16 = len(data) // 16

    aes_key = get_random_bytes(16)
    ciphertext = b''

    for i in range (len16):
        ciphertext += strxor(aes_key, data[i : i+16])
    
    print(ciphertext)
    

if __name__ == '__main__':
    main()
