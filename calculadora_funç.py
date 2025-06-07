class calculadora:
    def __init__(self, def_primeiro, def_segundo):
        self.primeiro = def_primeiro
        self.segundo = def_segundo
    def soma(self):
        print(self.primeiro, "+", self.segundo, "=", self.primeiro + self.segundo)
    def subtrair(self):
        print(self.primeiro, "-", self.segundo, "=", self.primeiro - self.segundo)
    def multiplicar(self):
        print(self.primeiro, "*", self.segundo, "=", self.primeiro * self.segundo)
    def dividir(self):
        print(self.primeiro, "/", self.segundo, "=", self.primeiro / self.segundo)
