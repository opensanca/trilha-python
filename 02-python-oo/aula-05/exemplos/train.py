class Train:
    def __init__(self, cars):
        self.cars = cars

    def __len__(self):   # len(train)
        return self.cars

    def __iter__(self):
        return ('car #{}'.format(i + 1) for i in range(self.cars))
