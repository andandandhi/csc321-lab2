# csc321-lab2
Symmetric Key Cryptography

###Set up task one instructions:

install python3

install pip

pip install pycryptodome

python3 main.py cp-logo.bmp

eog ecb_ciphertext.bmp

eog cbc_cipertext.bmp


##Write up
###Task One

With the ECB image we saw a picture similar to the original bmp in shape. The color changed but two different white pixels would be changed to the same new color. This is because ECB applies the same key to each block of data. With the CBC image it looked like rainbow colored noise. There was no data leakage. This is because the previous block is used to modify the current block of data. Two white pixels will now be different colors. The result is that the original image's data is diffused throughout the resulting image.

