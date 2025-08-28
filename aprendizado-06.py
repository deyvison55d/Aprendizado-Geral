class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    
    def ImprimirPet(self):
        print(f'Nome do pet:', self.nome)
        print(f'Peso do pet:', self.peso)
    
    def AlimentarPet(self, comida):
        self.peso += comida
    
#---------------------------------------------

class Abrigo:
    def __init__(self):
        self.catalogo = []

    def AdicionarPet(self, pet):
        self.catalogo.append(pet)
    
    def ImprimirAbrigo(self):
        print('Pets no abrigo:')
        print('-'*20)

        for pet in self.catalogo:
            pet.ImprimirPet()
            print('-'*20)

#---------------------------------------------

abrigo = Abrigo()
pet = Pet('Jujuba', 10)
abrigo.AdicionarPet(pet)

pet = Pet('Carlinho', 100)
abrigo.AdicionarPet(pet)

abrigo.ImprimirAbrigo()