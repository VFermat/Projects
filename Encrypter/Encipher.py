import random


class Encipher:

    def __init__(self, message):
        self.possible_keys = ['vitor', 'insper', 'dessoft', 'iron', 'triathlon',
                              'tiete', 'disney', 'floripa', 'dakar', 'ushuaia']
        self.message = message.lower()
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                         'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't',
                         'u', 'v', 'w', 'x', 'y', 'z']
        self.key = None
        self.encrypted_message = None
        self.decrypted_message = None

    def encrypt(self, type='ceasar', key=None):
        if type.lower() == 'vigenere':
            return self._vigenere_encryption(key)

    def _ceasar_encryption(self, key=None):
        pass

    def _ceasar_decryption(self, key):
        pass

    def _vernam_encryption(self):
        pass

    def _vernam_decryption(self, key):
        pass

    def _vigenere_encryption(self, key):
        encrypted_message = ''
        # Getting the Key and Breaking its characters
        if key is None:
            rand_key = random.randint(0, 9)
            key = self.possible_keys[rand_key]
        self.key = key
        key = [k for k in key]
        # Breaking the message into characters
        word = [m for m in self.message if m in self.alphabet]
        for i in range(len(word)):
            if word[i] in self.alphabet:
                # Position of the letter on the alphabet
                m = self.alphabet.index(word[i])
                # Position of the key letter on the alphabet
                k_pos = i % len(key)
                k = self.alphabet.index(key[k_pos])
                # Position of the encrypted letter on the alphabet
                e = abs(m + k) % len(self.alphabet)
                # Adding word to the encrypted message
                encrypted_message += self.alphabet[e]
        self.encrypted_message = encrypted_message
        return encrypted_message

    def _vigenere_decryption(self, key):
        decrypted_message = ''
        key = [k for k in key]
        # Breaking the message into characters
        crypted = [c for c in self.encrypted_message]
        for i in range(len(crypted)):
            # Position of the crypted letter on the alphabet
            c = self.alphabet.index(crypted[i])
            # Position of the key letter on the alphabet
            k_pos = i % len(key)
            k = self.alphabet.index(key[k_pos])
            # Position of the decrypted word on the alphabet
            d = (c - k) % len(self.alphabet)
            # Adding the word to the decrypted message
            decrypted_message += self.alphabet[d]
        self.decrypted_message = decrypted_message
        return decrypted_message



encipher = Encipher('No InFinance estudamos')

print(encipher.encrypt(type='vigenere', key='vitor'))

print(encipher._vigenere_decryption('vitor'))
