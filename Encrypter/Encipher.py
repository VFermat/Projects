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
        self.encrypted_message = message.lower()
        self.decrypted_message = None

    def validate_decryption(self):
        if self.encrypted_message == self.message :
            return 'Message was not encrypted yet.'
        elif self.decrypted_message is None:
            return 'Message was not decrypted yet.'
        else:
            message = [m for m in self.message if m in self.alphabet]
            if message == self.decrypted_message:
                return 'Decryption is Valid!'
            return 'Decryption was invalid! Someone is trying to break into the system.'

    def encrypt(self, type='ceasar', key=None):
        pass

    def decrypt(self, type='ceasar', key=None):
        pass

    def _ceasar_encryption(self, key=None):
        encrypted_message = ''
        if type(key) is not int:
            if key in self.alphabet:
                key = self.alphabet.index(key)
            else:
                print('Invalid Key. Algorithm is creating a random key for you!')
                key = random.randint(0, 25)
                print('Your key is {}'.format(key))
        # Breaking the message into characters
        word = [m for m in self.encrypted_message if m in self.alphabet]
        for i in range(len(word)):
            # Position of the letter on the alphabet
            m = self.alphabet.index(word[i])
            # Position for the encrypted letter
            e = (m + key) % len(self.alphabet)
            # Adding encrypted letter to the message
            encrypted_message += self.alphabet[e]
        self.encrypted_message = encrypted_message
        return encrypted_message

    def _ceasar_decryption(self, key):
        decrypted_message = ''
        crypted = [c for c in self.encrypted_message]
        for i in range(len(crypted)):
            # Position of the encrypted letter on the alphabet
            c = self.alphabet.index(crypted[i])
            # Position of the decrypted letter on the alphabet
            d = (c - key) % len(self.alphabet)
            # Adding Decrypted Letter to the message
            decrypted_message += self.alphabet[d]
        self.decrypted_message = decrypted_message
        return self.decrypted_message

    def _affine_encryption(self, a_key, b_key):
        if type(a_key) is not int:
            print('Invalid a key. We are creating a random key for you.')
            a_key = self._random_prime()
            print('a key: {}'.format(a_key))
        if type(b_key) is not int:
            print('Invalid b key. We are creating a random key for you.')
            b_key = random.randint(1, 11)
            print('b key: {}'.format(b_key))
        encrypted_message = ''
        # Breaking the message into characters
        word = [m for m in self.encrypted_message if m in self.alphabet]
        for i in range(len(word)):
            # Position of the letter on the alphabet
            m = self.alphabet.index(word[i])
            # Position of the encrypted letter on the alphabet
            e = (a_key*m + b_key) % len(self.alphabet)
            # Adding letter to the encrypted message
            encrypted_message += self.alphabet[e]
        self.encrypted_message = encrypted_message
        return encrypted_message

    def _affine_decryption(self, key):
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
        word = [m for m in self.encrypted_message if m in self.alphabet]
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

    def _random_prime(self):
        primes = self._get_primes(30)
        rand = random.randint(0, len(primes) - 1)
        return primes[rand]

    def _get_primes(self, limit):
        primes = []
        for i in range(limit):
            if self._is_prime(i):
                primes.append(i)
        return primes

    def _is_prime(self, i):
        for divisor in range(2, i-1):
            if i % divisor == 0:
                return False
        return True
