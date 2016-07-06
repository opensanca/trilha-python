class arq:
    def __init__(self, *args, **kwargs):
        self.arq = open(*args, **kwargs)

    def __enter__(self):
        return self.arq

    def __exit__(self, *args):
        self.arq.close()
