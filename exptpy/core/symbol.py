import math

from .constant import Constant
from .numeric import Numeric, Float

class Symbol:
    def __init__(self, name:str):
        self.name = name

    def __str__(self):
        return self.name

class Infinity(Constant, Numeric, Symbol):
    def __init__(self):
        super().__init__("Infinity")

class Pi(Constant, Symbol):
    def __init__(self):
        super().__init__("π", Float(math.pi))

class E(Constant, Symbol):
    def __init__(self):
        super().__init__("e", Float(math.e))