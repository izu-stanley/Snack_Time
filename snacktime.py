'''
A file comtaining my implementation of the Cipher Creation Snack for Terragon Group's internship application. 
I implemented the Caesar Cipher Technique 
Application at http://recruit-ife.terragongroup.com/#pages/ip-finder.html
'''
def encrypt(text,shift): 
    try:
        result = "" 
        for i in range(len(text)): 
            char = text[i] 
            # Encrypt uppercase characters 
            if (char.isupper()): 
                result += chr((ord(char) + shift-65) % 26 + 65) 
            # Encrypt lowercase characters 
            else: 
                result += chr((ord(char) + shift - 97) % 26 + 97)  
    except TypeError:
        return 'Error! Shift must be a Number'
    return result



text = "ITS_snack_Time"
shift = 2019

cipher = encrypt(text,shift)
if (cipher.split('!')[0] != 'Error!'):
    print ("Text : " + text) 
    print ("Shift : " + str(shift))
    print ("Cipher: " + cipher) 
