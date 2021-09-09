from constants.colors import black

class Points():
    def __init__(self, *vectors, color=black):
        self.vectors = list(vectors)
        self.color = color
