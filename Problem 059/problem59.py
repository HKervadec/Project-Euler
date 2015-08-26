# Each character on a computer is assigned a unique code and the preferred standard 
# is ASCII (American Standard Code for Information Interchange). For example, 
# uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, 
# then XOR each byte with a given value, taken from a secret key. The advantage 
# with the XOR function is that using the same encryption key on the cipher text, 
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, 
# and the key is made up of random bytes. The user would keep the encrypted message 
# and the encryption key in different locations, and without both "halves", it is 
# impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method 
# is to use a password as a key. If the password is shorter than the message, which 
# is likely, the key is repeated cyclically throughout the message. The balance for 
# this method is using a sufficiently long password key for security, but short 
# enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case 
# characters. Using cipher1.txt, a file containing the encrypted ASCII codes, and 
# the knowledge that the plain text must contain common English words, decrypt the 
# message and find the sum of the ASCII values in the original text.
from time import time

def xor(text, password):
    result = ''
        
        
    i = 0
    reste = len(text) % 3
    lim = len(text) - reste
    global iter
    while i < lim:
        for j in iter:
            result += chr(ord(text[i+j]) ^ ord(password[j]))
        
        i += len(password)
        
        
    for j in range(reste):
        result += chr(ord(text[lim+j]) ^ ord(password[j]))
        
        
    return result
    
    
def valide(text):
    global charList
    
    for letter in text:
        if not letter in charList:
            return False
            
    return True
    
    
def nextPassword(password):
    if password[2] == 'z':
        if password[1] == 'z':
            password[0] = chr(ord(password[0]) + 1)
            password[1] = 'a'
            password[2] = 'a'
            
        else:
            password[1] = chr(ord(password[1]) + 1)
            password[2] = 'a'
            
    else:
        password[2] = chr(ord(password[2]) + 1)
            
    return password
    
    
def sumText(text):
    sum = 0
    
    for carac in text:
        sum += ord(carac)
        
    return sum

# ******************************************************************************
startTime = time()

file = open('cipher1.txt', 'r')

content = file.read().split(',')

encryptedText = ""
for letter in content:
    encryptedText += chr(int(letter))
    
charList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 (),.;:\'"?-_!'
password = ['a', 'a', 'a']
iter = range(len(password))

validText = ''
while password != ['{', 'a', 'a']:
    decryptedText = xor(encryptedText, password)

    if valide(decryptedText):
        validText = decryptedText
        # print(decryptedText[:30], password)
        break
    
    password = nextPassword(password)
    
print("{0}: {1}".format(password, validText))
print(sumText(validText))
print(time() - startTime)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    