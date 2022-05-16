class securityLevel:
    def __init__(self):
        self.min_length = 0
        self.max_length = 0
        self.symbols = True
        self.max_symbols = 0
        self.mediumSecurity()

    def lowSecurity(self):
        self.manuelSecurity(8, 12, False)
        return

    def mediumSecurity(self):
        self.manuelSecurity(10, 18, True, 6)
        return

    def highSecurity(self):
        self.manuelSecurity(14, 20, True, 10)
        return

    def insaneSecurity(self):
        self.manuelSecurity(24, 32, True)
        return

    def manuelSecurity(self, min_length, max_length, bSymbols, max_symbols = 0):
        self.min_length = min_length
        self.max_length = max_length
        self.symbols = bSymbols
        self.max_symbols = max_symbols
        return
