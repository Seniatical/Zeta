import string

chars = list(string.printable)
__modes__ = ('full', 'semi')
__chars__ = {
        'lower': string.ascii_lowercase,
        'upper': string.ascii_uppercase,
        'numbers': string.digits,
        'punc': string.punctuation 
        }

def _push(letter: str, push: int) -> str:
    if letter in list(string.ascii_lowercase):
        char_set = list(__chars__['lower'])
        current_pos = char_set.index(letter, 0)
        if current_pos + push > (len(char_set) - 1):
            index = (len(char_set) - current_pos) - push
        else:
            index = push + current_pos

    elif letter in list(string.ascii_uppercase):
        char_set = list(__chars__['upper'])
        current_pos = char_set.index(letter, 0)
        if current_pos + push > (len(char_set) - 1):
            index = (len(char_set) - current_pos) - push
        else:
            index = push + current_pos

    elif letter in list(string.digits):
        char_set = list(__chars__['numbers'])
        current_pos = char_set.index(letter, 0)
        if current_pos + push > (len(char_set) - 1):
            index = (len(char_set) - current_pos) - push
        else:
            index = push + current_pos

    elif letter in list(string.punctuation):
        char_set = list(__chars__['punc'])
        current_pos = char_set.index(letter, 0)
        if current_pos + push > (len(char_set) - 1):
            index = (len(char_set) - current_pos) - push
        else:
            index = push + current_pos
    else:
        raise UnicodeError(f'Cannot find char {letter}')
    new_letter = char_set[index]
    return new_letter

def _fullpush(letter: str, push: int) -> str:
    char_set = chars
    current_pos = char_set.index(letter, 0)
    if current_pos + push > (len(char_set) - 1):
        index = (len(char_set) - current_pos) - push
    else:
        index = push + current_pos
    new_letter = char_set[index]
    return new_letter

class Ceaser:
    
    @staticmethod
    def encrypt(message: str, push: int = 1, mode: str = 'semi') -> str:
        if not type(message) == str:
            raise TypeError('Message to be encrypted must be a string')
        if not type(push) == int:
            raise TypeError('Letter push must be a number')
        if not mode.lower() in __modes__:
            raise TypeError('mode was not SEMI or FULL')
        former = []
        for char in message:
            if mode.lower() == 'semi':
                new_char = _push(char, push)
            else:
                new_char = _fullpush(char, push)
            former.append(new_char)
        new_message = ''.join(former)
        return new_message

    @staticmethod
    def decrypt(message: str, push: int = 1, mode: str = 'semi') -> str:
        if not type(message) == str:
            raise TypeError('Message to be encrypted must be a string')
        if not type(push) == int:
            raise TypeError('Letter push must be a number')
        if not mode.lower() in __modes__:
            raise TypeError('mode was not SEMI or FULL')
        former = []
        if not push < 0:
            push = push * -1
            ## Simple way of moving backwards without over complicating stuff
        for char in message:
            if mode.lower() == 'semi':
                new_char = _push(char, push)
            else:
                new_char = _fullpush(char, push)
            former.append(new_char)
        new_message = ''.join(former)
        return new_message
        
        
