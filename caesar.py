from cipher import Cipher  

class CaesarCipher(Cipher):
    '''
    A cipher where each letter is shifted a certain number of places down the alphabet.
    '''
    def __init__(self):
        '''
        Initializes the CaesarCipher class with a default shift value of 3.
        '''
        super().__init__()
        self._shift = 3
    
    def _encrypt_letter(self, letter):
        '''
        Encrypts a single letter using the Caesar cipher.

        Parameters:
        letter (str): The letter to be encrypted.

        Returns:
        str: The encrypted letter.
        '''
        index = self._alphabet.index(letter)
        return self._alphabet[(index + self._shift) % 26]
    
    def _decrypt_letter(self,letter):
        '''
        Decrypts a single letter using the Caesar cipher.

        Parameters:
        letter (str): The letter to be decrypted.

        Returns:
        str: The decrypted letter.
        '''
        index = self._alphabet.index(letter)
        return self._alphabet[(index - self._shift) % 26]