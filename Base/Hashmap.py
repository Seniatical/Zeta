class Hashmap:
    def __init__(self, complexity: int, hashes: dict, same: bool=True) -> ' \
Complexity -> How long is each word in the hashmap, If same is false provide the avg amt \
hashes -> The dict containing the hashes. \
Same -> If its False with your dict hashmap you must state the length of the character e.g. {"A": ["something", 10]} \
                That is just to show the program your letter is 10 letters \
                Using this method allows you do have hashmaps such as {"A": ["Encryption_Here", 15]}\
':

        ## This model is just going to be used for when we use your hashmap!

        super(Hashmap).__init__(self, *args, **kwargs)

        if not type(complexity) == int:
            raise TypeError('Complexity type must be an integer not string!')
        if not type(hashes) == dict:
            raise TypeError('Hashes must be a dictionary not, {}'.format(type(hashes)))
        
        self.complexity = complexity
        if not hashes:
            raise TypeError('Hash map provided cannot be empty')
        self.hashes = hashes
        self.amt = len(hashes)
        self.same = same

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

    

    

    
        
