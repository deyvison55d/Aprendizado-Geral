"""
Crie uma classe que modele o objeto 'carro' 
Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
Crie uma instância da classe carro.
Faça o carro 'andar' utilizando os métodos da sua classe.
Faça o carro 'parar' utilizando os métodos da sua classe.
    
"""


class Carro:
    def __init__(self, cor, modelo):
        '''
        Inicializa uma nova instância da classe Carro.

        Args:
            cor (str): Cor do carro.
            modelo (str): Modelo do carro.

        Attributes:
            _ligado (bool): Indica se o carro está ligado.
            cor (str): Cor do carro.
            modelo (str): Modelo do carro.
            _velocidade (int): Velocidade atual do carro.
        '''
        self._ligado = False
        self.cor = cor
        self.modelo = modelo
        self._velocidade = 0


    def ligar(self):
        if self._ligado:
            print('O carro já está ligado!')
        else:
            self._ligado = True
            print('O carro foi ligado')


    def desligar(self):
        if not self._ligado:
            print('O carro já está desligado!')
        elif self._velocidade > 0:
            print('Diminua a velocidade primeiro!')
        else:
            self._ligado = False
            print('O carro foi desligado')


    def acelerar(self):
        if self._velocidade >= 100:
            print('O carro ja está na sua velocidade máxima!')
        elif not self._ligado:
            print('Ligue o carro primeiro!')
        else:
            self._velocidade += 10
            print('Acelerando...')
            print(f'Velocidade atual:', self._velocidade)


    def desacelerar(self):
        if self._velocidade <= 0:
            return
        else:            
            self._velocidade -= 10
            print('Desacelerando...')
            print(f'Velocidade atual:', self._velocidade)


    def parar(self):
        if self._velocidade <= 0:
            print('O carro já está parado!')
        elif not self._ligado:
            print('Ligue o carro e acelere antes')
        else:
            print('Parando...')
            while self._velocidade > 10:
                self._velocidade -= 10
                print(f'{self._velocidade}')
            print(f'O carro parou!')
        
    
    def buzinar(self):
        if not self._ligado:
            print('É necessário o carro estar ligado')
        else:
            print('PIii! PIii!')
#---------------------------------------------------------------------
carro = Carro('Vermelho', 'honda civic')
carro.ligar()
carro.acelerar()
carro.acelerar()
carro.buzinar()
carro.acelerar()
carro.acelerar()
carro.parar()
help(Carro)