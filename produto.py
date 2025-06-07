import random
class Produto:
    def __init__(self, def_nome, def_preco, def_estoque):
        self.nome = def_nome
        self.preco = def_preco
        self.estoque = def_estoque
    def comprar(self):
        if self.estoque >= 1:
            print(self.estoque - random.randint(1, 10))
        else:
            print(self.estoque, "Não há mais.")
    def repor(self):
        print(self.estoque + 1)
    def mostrar_estoque(self):
        print(self.estoque)
