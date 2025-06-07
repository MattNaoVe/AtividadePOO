class Cachorro:
    #atributos
    #metodo construtor
    def __init__(self , def_nome , def_raca):
        self.nome = def_nome
        self.raca = def_raca
        
    #metodos
    def latir(self):
        print('au au au, eu sou' , self.nome , 'da raça' , self.raca )