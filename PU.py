class PU:
    def __init__(self, scratch):
        self.scratch = scratch

    def cummutliply(self, aval, arow, bval):
        self.scratch[arow] = self.scratch[arow] + aval * bval