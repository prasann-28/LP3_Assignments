# python3 aes.py
from Crypto.Cipher import AES

#key has to be either 16, 24 or 32 bytes
def paddedKey(key):
    while len(key) % 8 !=0:
        key +=' '
    return key
    
#text has to in multiples of 26 bytes
def paddedText(text):
    while len(text) % 16 != 0:
        text += ' '
    return text
        
plain_input = input("Enter the text to be encrypted: ")
plain = paddedText(plain_input)
 
key_input = input("Enter in a key between 16 and 32 characters: ")
key = paddedKey(key_input)
 
if(len(key_input)< 16 & len(key_input)> 32):
 print("key must be between 16 and 32 characters!")
 
cipher = AES.new(key)
ciphertext = cipher.encrypt(plain)
print(ciphertext)
 
cleartext = cipher.decrypt(ciphertext)
print(cleartext)
