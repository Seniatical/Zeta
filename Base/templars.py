'''
File containing all the base errors raised by the module!
'''

class TooManyArgs(Warning):
    pass

''' Errors Caused with the Hashmap '''
class DuplicateKey(Exception):
    '''
    Raised when the key trying to be added already exists within the hashmap
    
    :params message <typing.Optional[str]>
    :returns None
    :usage raise DuplicateKey(message...)
    '''
    pass

class KeyAdditionError(Exception):
    '''
    Raised when it fails to add a key to the hashmap
    
    :params message <typing.Optional[str]>
    :returns None
    :usage raise KeyAddtionError(message...)
    '''
    pass

class KeyNotFound(Exception):
    '''
    Raised when a key was not found within a hashmap
    
    :params message <typing.Optional[str]>
    :returns None
    :usage raise KeyNotFound(message...)
    '''
    pass

class KeyEditError(Exception):
    '''
    Raied when it fails to edit a key
    Most likely due to an error within your keys list or some other random error
    
    :params message <typing.Optional[str]>
    :returns None
    :usage raise KeyEditError(message...)
    '''
    pass
