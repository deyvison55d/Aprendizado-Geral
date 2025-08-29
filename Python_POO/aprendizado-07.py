
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

    def imprimir_nome(self):
        print(f'O nome do animal é:', self.nome)

class Cachorro(Animal):
    def fazer_som(self):
        return 'Au au!'

class Gato(Animal):
    def fazer_som(self):
        return 'Miauu!'

class Passarinho(Animal):
    def fazer_som(self):
        return 'Piu Piu!'

#--------------------------------------

"""cachorro = Cachorro('Bilu')
gato = Gato('Fofoxo')
passarinho = Passarinho('Pinto')

print(cachorro.nome , 'faz:' , cachorro.fazer_som())
print(gato.nome , 'faz:' , gato.fazer_som())
print(passarinho.nome , 'faz:' , passarinho.fazer_som())

cachorro.imprimir_nome()
gato.imprimir_nome()
passarinho.imprimir_nome()"""


def fazer_barulho(animal):
    print(animal.nome , 'faz:', animal.fazer_som())

cachorro = Cachorro('bilu')
gato = Gato('xoxota')
passarinho = Passarinho('Pinto')

fazer_barulho(cachorro)
fazer_barulho(gato)
fazer_barulho(passarinho)
