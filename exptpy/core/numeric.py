from .constant import Constant

class Numeric:
    def __init__(self):
        self.significant_digit = 0
        self.exponent = 0
    pass

class Integer(Constant, Numeric):
    def __init__(self, value:int):
        super().__init__()
        if type(value) == int:
            self.value = value
        elif type(value) == str:
            self.value = int(value)
        else:
            TypeError()
        self.significant_digit
    pass

class Float(Constant, Numeric):
    pass

class Rational(Constant, Numeric):
    pass