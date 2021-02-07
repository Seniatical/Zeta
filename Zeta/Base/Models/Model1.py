"""
Hello There...
"""

''' Imports '''
from Zeta.Base.Models.Encryption_Patterns.Sen_encrypt import *
from Zeta.Base.Models.Encryption_Patterns.Sen_decrypt import *

'''
Globals
'''
global en1, crypt, word, word_former, enc_char_holder, enc_sentence_holder

def reset_encrypter():
    global en1
    en1 = ['$EN!']

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

class Sen:

    @staticmethod
    def encrypt(message: str) -> str:
        global en1, crypt, word, word_former, enc_char_holder, enc_sentence_holder

        # Encrypting mechanasim
        message = list(message) # Listing the inputted message so we can encrypt each character given
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
        result = ''.join(map(str, en1))
        reset_encrypter()
        # return our new encrypted string
        return result

    @staticmethod
    def decrypt(encrypted_message: str) -> str:
        global en1, crypt, word, word_former, enc_char_holder, enc_sentence_holder
        
        # Listing the encrypted message to check for the correct encryption and to decrypt each letter
        listed_message = list(encrypted_message)
        # Check if the given encryption is valid to ours
        try:
            if '$' not in listed_message[0] and '3' not in listed_message[1] and 'N' not in listed_message[2] and '!' not in listed_message[3]:
                # If it returns as true it will break and print the message
                raise TypeError('You havent provided the original encryption. Please encrypt your message again.')
            else:

                # Looping through the characters
                for char in listed_message[4:]:
                    word_former.append(char)
                    crypt += 1
                    if crypt == 4:
                        crypt = 0
                        words = ''.join(map(str, word_former))
                        word_former.clear()
                        word.append(words)
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

            original_message = ''.join(map(str, enc_char_holder))
            enc_char_holder.clear(), word.clear()
            return original_message
            
        except TypeError:
            raise TypeError('The encryption given was too small to be decrypted')
