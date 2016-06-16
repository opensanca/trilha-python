class Lampada:
    ligada = False

    def __init__(self, cor, voltagem=110):
        self.cor = cor
        if voltagem:
            self.voltagem = voltagem

    def liga_desliga(self):
        self.ligada = not self.ligada
