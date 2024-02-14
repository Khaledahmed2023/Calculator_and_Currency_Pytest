

class CurrencyConverter():
    def __init__(self, crown, euro):
        self.crown = crown
        self.euro = euro

    def crown_to_euro(self):
        # self.crown * 0.1075
        return self.crown * 0.1075
    
    def euro_to_crown(self):
        return self.euro / 0.1075
    
    
