from .expression import Expression
from .numeric import *

class Operator(Expression):
    def __init__(self, a, b):
        self.args = (a, b)

class Add(Operator):
    def __str__(self):
        return "{} + {}".format(*self.args)

class Mul(Operator):
    def __new__(cls, a, b):
        if not isinstance(a, Constant) and not isinstance(b, Constant):
            pass
        elif isinstance(a, Constant) and isinstance(b, Constant):
            return a.mul(b)
        else:
            if isinstance(b, Constant):
                a, b = b, a
            if a == 1:
                return b
            return super().__new__(cls, a, b)
    def __str__(self):
        return "{} * {}".format(*self.args)