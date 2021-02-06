class TooManyArgs(Warning):
    '''
    Raised when you use the Custom Lengthed Hashmap
    -> Extra Args rather than the base set 2, may cause interferences
        Example:
            {
                "A": ['KEY', 3, *extra_args]
            }
    
    :requirement is_same = False
    :params <message... typing.AnyStr>
    :returns None
    :usage warnings.warn(message..., category=TooManyArgs)
    '''
    pass

''' Errors Caused with the Hashmap '''
class DuplicateKey(Exception):
    '''
    Error raised when you try adding a new key to your hashmap which already exists in the hashmap
    
    :params <message... typing.Optional[str]>
    :returns None
    :usage raise DuplicateKey(message...)
    '''
    pass

class KeyAdditionError(Exception):
    '''
    Error raised when you try adding a key which has mistakes in it
    e.g.:
        MyHash.add_key(Key=[10, 'Test']); Args a backwards
        MyHash.add_key(Key=10); Key link is a int rather than str
        
    :params <message... typing.Optional[str]>
    :returns None
    :usage raise KeyAdditionError(message...)
    '''
    pass

class KeyNotFound(Exception):
    '''
    Error raised when the given key cannot be found in the hashmap
    Usually raised from:
        Delete Key
        Edit Key
        Fetching the Key
        
    :params <message... typing.Optional[str]>
    :returns None
    :usage raise KeyNotFound(message...)
    '''
    pass

class KeyEditError(Exception):
    '''
    Error raised from when editing a Key from your hashmap
        -> Due to an error within the key itself
        
    MyHashmap.edit_key(Key=10); Must a string for the key not a int
    MyHashmap.edit_key(Key=[10, 'Lols']); Args are backwards
    
    :params <message... typing.Optional[str]>
    :returns None
    :usage raise KeyEditError(message...)
    '''
    pass
