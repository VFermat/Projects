import random


class Encipher:

    def __init__(self, message):
        self.possible_keys = ['vitor', 'insper', 'dessoft', 'iron', 'triathlon',
                              'tiete', 'disney', 'floripa', 'dakar', 'ushuaia']
        self.message = message.lower()
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def encrypt(self, type='ceasar'):
        pass

    def _ceasar_encryption(self, key=None):
        pass

    def _ceasar_decryption(self, key):
        pass

    def _vernam_encryption(self):
        pass

    def _vernam_decryption(self, key):
        pass

    def _vigenere_encryption(self, key=None):
        encrypted_message = ''
        # Getting the Key and Breaking its characters
        if key is None:
            rand_key = random.randint(10)
            key = self.possible_keys[rand_key]
        key = [k for k in key]
        # Breaking the message into characters
        word = [c for c in self.message]
        # Making the key has the same length as the message
        for i in range(len(word)):
            if word[i] not in self.alphabet:
                encrypted_message += word[i]
            else:
                # Position of the letter on the alphabet
                m = self.alphabet.index(word[i])
                # Position of the key letter on the alphabet
                k = self.alphabet
                # Position of the encrypted letter on the alphabet
                e = (m + k) // len(self.alphabet)
                # Adding word to the encrypted message
                encrypted_message += e
        return encrypted_message

    def _vigenere_decryption(self, key):
        pass
