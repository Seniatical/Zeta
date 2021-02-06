# Zeta
A simple module which allows you to make your own hashes and encryptions, whilst still allowing you to play around other ciphers and hashes!

As for now just do `pip install git+https://github.com/Seniatical/Zeta/`

**Base Model Usage:**
```py
>>> from Zeta.Base import Models

>>> BaseModel = Models.Sen()	## This is for my custom encryption method!
>>> MyMessage = 'Hello, World!'
>>> BaseModel.encrypt(MyMessage)

'$3N!S+=2;^3z.*<,.*<,£6&X1}+=><><~S#"£6&X&'#|.*<,!35d&&4_'

>>> BaseModel.decrypt('$3N!S+=2;^3z.*<,.*<,£6&X1}+=><><~S#"£6&X&'#|.*<,!35d&&4_')

'Hello, World!'
```
**.** If you would like to see all the base models so far just simply do this `Models.__models__`

**.** With this module you can also create and use your own hashes and encryptions!

```py
from Zeta.Base import Creator
from Zeta.Base import Hashmap

## This is were you provide a hashmap or a dict for it be saved!

MyHash = Hashmap(5, {'A': 'something_unique'}, True)
## Now we have the hashmap object which we can create your encryption from
## 5 -> The size of each hashmap key, If your hash key are different from one another give the avg of them all
## The dict is your hashmap. To keep things simple you can just do that!
## True -> Shows all of the hash sizes are equal to 5

'''
Want custom lengths?
Input your dict like this:
	{
	"A": ['Something Unique', 16]	## Size of the hash this is just to make the deciphering easier
	}
'''
MyCrypter = Creator.MakeCrypt(MyHash)
MyMessage = 'Hello, World!'

Encrypted = MyCrypter.encrypt(MyMessage)

## Same as the premade models

Decrypted = MyCrypter.decrypt(Encrypted)
```

In the Near future I will make it allowable to use files such as `.json` and `.yml` to be used as your hash maps!
