from Zeta.Base.Models.Encryption_Patterns import morse

class Morse:

	@staticmethod
	def encrypt(message: str) -> str:
		if not type(message) == str:
			raise TypeError('Message must be a string!')
		listed_message = list(message)
		collected = []
		for character in listed_message:
			if not character.upper() in morse.codes:
				raise UnicodeError(f'Cannot find char {character} in morse_code!')
			morse_character = morse.codes[character.upper()]
			collected.append(morse_character)
		new_message = ' '.join(collected)
		return new_message

	@staticmethod
	def decrypt(message: str) -> str:
		if not type(message) == str:
			raise TypeError('Message must be string!')
		listed_message = message.split()
		new_characters = []
		for morse_code in listed_message:
			if not morse_code in morse.rcodes:
				raise UnicodeError(f'Character {morse_code} wasn\'t found in the morse hashmap')
			real_character = morse.rcodes[morse_code]
			new_characters.append(real_character)
		new_message = ''.join(new_characters)
		return new_message
