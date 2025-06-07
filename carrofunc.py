class Carro:
    def __init__(self, def_modelo, def_velocidade):
        self.velocidade = def_velocidade
        self.modelo= def_modelo
    def acelerar(self):
        print(self.velocidade + 10)
    def frear(self):
        if self.velocidade == True:
            print(self.velocidade - 10)
        else:
            print(self.velocidade)
    def mostrar_velocidade(self):
        print(self.velocidade)

velocidade = Carro("Fusca", 0)
velocidade.acelerar()
velocidade.frear()
velocidade.mostrar_velocidade()