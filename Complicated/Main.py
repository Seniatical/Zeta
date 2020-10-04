'''
Encrypter and Decrypter made by Senatical.
'''

''' Imports '''
from Encrypter import *
from Decrypter import *

''' Variables '''
# Encrypted message holder
en1 = ['$3N!']

# Decrypter splitting method
word_former = []
word = []
crypt = 0

# Decrypting Character Holder
enc_char_holder = []
enc_sentence_holder = []

# Running code
while True:
    # Option of encrypt or decrypt
    
    msg = str(input('Enter 1 for encrypting and 2 for decrypting\n\n'))
    if msg == '1':
        msg1 = str(input('What will you like to encrypt?\t'))
        
        # Encrypting mechanasim
        message = list(msg1) # Listing the inputted message so we can encrypt each character given
        for char in message: # Looping through all characters that are in the listed message
            if char in lower:   # If the character is in lower
                en1.append(lower[char]) # It will append its encrypted form into en1
            if char in upper:
                en1.append(upper[char])
            if char in numbers:
                en1.append(numbers[char])
            if char in unclassified:
                en1.append(unclassified[char])
        # Same cycle continues through the rest of the code

        # Join the encrypted letters in en1 to form 1 big message
        x = ''.join(map(str, en1))
        en1 = ['S3N!']
        # Print the final result
        print('The message " {} " has been encrypted below!\n\n'.format(msg1) + x)

    # Decrypting method
    elif msg == '2':

        # Asking for the encrypted message
        encrypted_message = str(input('What is your encrypted message?\n\n'))

        # Listing the encrypted message to check for the correct encryption and to decrypt each letter
        y = list(encrypted_message)

        # Check if the given encryption is valid to ours
        try:
            if '$' not in y[0] and '3' not in y[1] and 'N' not in y[2] and '!' not in y[3]:

                # If it returns as true it will break and print the message
                print('You havent provided the original encryption. Please encrypt your message again.')
            else:
                
                # We pop the first characters used to check the encryption type
                y.pop(0)
                y.pop(1)
                y.pop(0)    
                y.pop(0)

                # Looping through the characters
                for char in y:
                    word_former.append(char)
                    crypt += 1
                    if crypt == 4:
                        crypt = 0
                        words = ''.join(map(str, word_former))
                        word_former = []
                        word.append(words)
                    # Creates 1, 4 letter character string and places it into the list. This is the first encrypted message
                    # Continues this cycle till no characters are left

            
                # Now we decrypt the encrypted message
                # We loop through the encoded 4 letter keys
                for enc_char in word:
                    if enc_char in reversed_lower:
                        enc_char_holder.append(reversed_lower[enc_char])
                    if enc_char in reversed_upper:
                        enc_char_holder.append(reversed_upper[enc_char])
                    if enc_char in reversed_number:
                        enc_char_holder.append(reversed_number[enc_char])
                    if enc_char in reversed_unclassified:
                        enc_char_holder.append(reversed_unclassified[enc_char])
                # Were now checking in the character matches one of the key's of letters in out codes
                # If it does it will append the correct character to the list

            sentence = ''.join(map(str, enc_char_holder))
            print(sentence)
            enc_char_holder = []
            word = []
        except TypeError:
            print('The encryption given was too small to be decrypted')



    
