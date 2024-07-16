from .symbol import Symbol

class Variable(Symbol):

    def __str__(self):
        return self.name