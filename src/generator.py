import random

from .securityLevel import securityLevel
from . import symbols

class generator:

    def __init__(self, syms = []):
        self.secLevel = securityLevel()
        self.length = 0
        self.psw = []
        self.partition = [0,0,0,0]
        self.syms = []
        self.setSymbols()
        
    def generate_parition(self):
        symbol_length = 0
        num_length = 0
        char_lower_length = 0
        char_upper_length = 0
        self.length = random.randint(
            self.secLevel.min_length, self.secLevel.max_length)

        remaining_chars = self.length - 3

        if self.secLevel.symbols == True:
            if self.secLevel.max_symbols == 0 or self.secLevel.max_symbols > remaining_chars:
                symbol_length = random.randint(1, remaining_chars)
            else: 
                symbol_length = random.randint(1, self.secLevel.max_symbols)

        remaining_chars = remaining_chars - symbol_length + 1

        num_length = random.randint(1, remaining_chars)
        remaining_chars = remaining_chars - num_length + 1

        char_lower_length = random.randint(1, remaining_chars)
        remaining_chars = remaining_chars - char_lower_length + 1

        char_upper_length = remaining_chars
        
        if self.secLevel.symbols and self.secLevel.max_symbols == 0:
            self.partition = [symbol_length, num_length, char_lower_length, char_upper_length]
            random.shuffle(self.partition)
        else:
            temp = [num_length, char_lower_length, char_upper_length]
            random.shuffle(temp)
            self.partition = [symbol_length] + temp 
        return
    
    def create_password(self):
        self.generate_parition()
        sym_array = random.choices(self.syms, k=self.partition[0])
        num_array = [chr(ord('0') + i) for i in random.choices([i for i in range(10)], k=self.partition[1])]
        lower_array = [chr(ord('a') + i) for i in random.choices([i for i in range(ord('z') - ord('a'))], k=self.partition[2])]
        upper_array = [chr(ord('A') + i) for i in random.choices([i for i in range(ord('z') - ord('a'))], k=self.partition[3])]
        array = sym_array + num_array + lower_array + upper_array
        random.shuffle(array)
        self.psw = ''.join(array)

    def setSymbols(self, symbol_list = []):
        if symbol_list:
            self.syms = symbol_list
        else:
            self.syms =  symbols.us_symbols
        return

    def save(self, file = 'psw.txt'):
        with open(file, 'w') as f:
            f.write("[psw] {}".format(self.psw))