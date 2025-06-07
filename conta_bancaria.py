# padrão de nomeação de classe é o CamelCase
class ContaBancaria:
    #atributos
    #metodo construtor
    def __init__(self , def_titular , def_saldo):
        self.titular = def_titular
        self.__saldo = def_saldo
        
    #metodos
    def consultar_saldo(self):
        print(self.__saldo)
        
    def sacar(self, valor):
        self.__saldo = self.__saldo - valor
        
    def depositar(self, valor):
        self.__saldo = self.__saldo + valor
