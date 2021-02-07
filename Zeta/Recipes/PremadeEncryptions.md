**Seniaticals Encryption**
```py
from Zeta.Base import Models

Seniatical = Models.Sen()
MyMessage = "Hello, World!"

## To encrypt
EncrpytedMessage = Seniatical.encrypt(MyMessage)

## To decrypt
DecryptedMessage = Seniatical.decrypt(EncrpytedMessage)
```
A simple and secure encryption method
Its decrpytion method is the base layer of how it will decrypt your patterns

**Morse Code**
```py
from Zeta.Base import Models

MorseCode = Models.Morse()
MyMessage = 'Hello, World!'

## To Encrypt
EncrpytedMessage = MorseCode.encrypt(MyMessage)

## To Decrypt
DecryptedMessage = MorseCode.decrypt(EncrpytedMessage)
```

**Ceaser Cipher**
```py
from Zeta.Base import Models

Ceaser = Models.Ceaser()
MyMessage = 'Hello, World!'

## To Encrypt
EncrpytedMessage = Ceaser.encrypt(message=MyMessage, push=1, mode='semi')
'''
message; The string being encrypted
push; how many chars to push the chosen character by
mode; between SEMI and FULL:
		SEMI: Only pushes the chosen character through its subset of chars
		FULL: Pushes every character with no seperation like semi
'''

## To Decrypt
DecryptedMessage = Ceaser.decrypt(EncrpytedMessage)
```
