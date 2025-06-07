from calculadora_funç import calculadora
from carrofunc import Carro
from racas import Cachorro
from pessoa import Pessoa
from produto import Produto

pessoa1 = Pessoa('Matheus' , 17)
pessoa1.apresentar()

pessoa2 = Pessoa('Roberta' , 76)
pessoa2.apresentar()


numero = calculadora(10, 20)
numero.soma()
numero.subtrair()
numero.multiplicar()
numero.dividir()


velocidade = Carro("Fusca", 0)
velocidade.acelerar()
velocidade.frear()
velocidade.mostrar_velocidade()


cachorro1 = Cachorro('Roberto' , 'poodle')
cachorro2 = Cachorro('alan cardec' , 'chiwawa')
cachorro3 = Cachorro('dave the magical cheeze wizard' , 'pit bull')

cachorro1.latir()
cachorro2.latir()
cachorro3.latir()

venda = Produto("Canabidiol", 297, 100)
venda.comprar()
venda.mostrar_estoque()
venda.repor()
venda.mostrar_estoque()


