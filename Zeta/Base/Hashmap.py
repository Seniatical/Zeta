import warnings
import Base.templars as templars

__slots__ = ('complexity', 'hashes', 'is_same')

def hash_check(cls):

    def static(complexity: int, hashes: int, is_same: bool = True):
        
        if not type(complexity) == int:
            raise TypeError('Complexity type must be an integer not, {}'.format(type(complexity)))
        if not type(hashes) == dict:
            raise TypeError('Hashes must be a dictionary not, {}'.format(type(hashes)))
        if not hashes:
            raise TypeError('Hashmap provided cannot be empty')
        if not type(is_same) == bool:
            raise TypeError('Bool value for is_same cannot be, {}'.format(type(is_same)))

        for hash in hashes:
            if not is_same and type(hashes[hash]) != list:
                raise TypeError('Hashmap error located at key {}, is_same was False so please make sure you hashes are stored like "A": ["hash_here", hash_length]')
            if not is_same and type(hashes[hash]) == list and len(hashes[hash]) > 2:
                warnings.warn('Key "{}" has identified extra pairs of arguments!'.format(hash), category=templars.TooManyArgs)
            if is_same and type(hashes[hash]) == list:
                raise TypeError('Hash "{}" has identified an error, listed arguments, is_same is True. Please make sure you set is_same as False'.format(hash))
            if not is_same and type(hashes[hash]) == list and len(hashes[hash]) == 2 and type(hashes[hash][0]) != str:
                raise TypeError('Hash "{}" has identified an error, right hand argument must be a string')
        
    return static

def check_key(key, is_same):
    if not is_same and type(key) != list:
        return False
    if not is_same and type(key) == list and len(key) > 2:
        return False
    if is_same and type(key) == list:
        return False
    if not is_same and type(key) == list and len(key) < 2:
        return False
    if not is_same and type(key) == list and len(key) == 2 and type(key) != int:
        return False
    if not is_same and type(key) == list and len(key) == 2 and type(key) != str:
        return False
    return True

@hash_check
class Hashmap:
    def __init__(self, complexity: int, hashes: dict, is_same: bool=True) -> ' \
complexity -> How long is each word in the hashmap, If same is false provide the avg amt \
hashes -> The dict containing the hashes. \
is_same -> If its False with your dict hashmap you must state the length of the character e.g. {"A": ["something", 10]} \
                That is just to show the program your letter is 10 letters \
                Using this method allows you do have hashmaps such as {"A": ["Encryption_Here", 15]}\
':
        
        self.complexity = complexity
        self.hashes = hashes
        self.amt = len(hashes)
        self.same = is_same

        check_hash(self.hashes)

    def __call__(self) -> dict:
        return self.hashes

    def __str__(self) -> str:
        ending = 'equal' if self.same else 'not equal'
        return 'Hashmap Object with {} Hashes with a complexity of {} with each element being {}'.format(self.amt, self.complexity, ending)

    def __repr__(self) -> str:
        return f'<Hashmap ID={id(Hashmap)} Elements={self.amt} Hash_Length={self.complexity} Hash_Complex={self.same}>'

    def __int__(self) -> int:
        return self.complexity

    def __iter__(self) -> list:
        return iter([self.complexity, self.hashes, self.same, self.amt])

    def __len__(self) -> int:
        return self.amt

    def __dict__(self) -> dict:
        return {
            'complexity': self.complexity,
            'hash': self.hashes,
            'same': self.same,
            'hashes': self.amt,
            }

    def delete_hash(self, *keys):
        for key in keys:
            for hash in self.hashes:
                if hash == key:
                    del hashes[hash]
                else:
                    raise templars.KeyNotFound('Cannot find key {}'.format(key))

    def add_hash(self, **keys):
        for key in keys:
            if key in self.hashes:
                raise templars.DuplicateKey('Key {} already exists'.format(key))
            
            if not check_key(keys[key], self.same):
                raise templars.KeyAdditionError('Failed to add key {}'.format(key))
        return True

    def edit_hash(self, *keys):
        for key in keys:
            if key not in self.hashes:
                raise templars.KeyNotFound('Key {} cannot be found in your hash'.format(key))
            if not check_key(keys[key], self.same):
                raise templars.KeyEditError('Failed to edit key {}'.format(key))
        return True

myhash = Hashmap(10, {'A': ['lols', 10, 'test']}, False)
    

    
        
