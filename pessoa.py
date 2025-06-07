class Pessoa:
    def __init__(self, def_nome, def_idade):
        self.nome = def_nome
        self.idade = def_idade
    
    
    def apresentar(self):
        print('oi meu nome é' , self.nome , 'eu tenho' , self.idade, 'anos')