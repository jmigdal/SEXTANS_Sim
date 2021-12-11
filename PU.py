class PU:
    def __init__(self, scratch):
        self.scratch = scratch

    def cum_mutliply(self, a_val, a_row, b_val):
        self.scratch[a_row] = self.scratch[a_row] + a_val * b_val