# caesarCipher.py
# @coneill 21/01/2026
key = -1
# Single Letter
plaintext = "P"
plainASCII = ord(plaintext)
cipherASCII = plainASCII + key
ciphertext = chr(cipherASCII)
print("Plaintext:",plaintext,"Ciphertext:",ciphertext)
# Full word
plaintext = "PYTHON"
print("plaintext:",plaintext)
print("Ciphertext:")
for letter in plaintext:
    plainASCII = ord(letter)
    cipherASCII = plainASCII + key
    ciphertext = chr(cipherASCII)
    print(ciphertext)
    
