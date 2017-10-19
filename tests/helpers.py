class FakePixels(list):
    def __init__(self, n):
        self.n = n
        for i in range(n):
            self.append((0, 0, 0))
