class Pai1:
    def metodo_pai1(self):
        print('Método do pai 1')

class Pai2:
    def meotodo_pai2(self):
        print('Método do pai 2')

class Filho(Pai1, Pai2):
    def metodo_filho(self):
        print('Método do Filho')



filho = Filho()

filho.metodo_filho()
filho.metodo_pai1()
filho.meotodo_pai2()

