class Carro:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False
    
    def estacionar(self):
        self.estacionado = True
    
    def sair_da_vaga(self):
        self.estacionado = False
#------------------------------------
class Moto:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False
#------------------------------------

class Vaga:
    def __init__(self, identificador, tipo):
            self.id = identificador
            self.livre = True

            if tipo is not 'carro' and tipo is not 'moto':
                raise ValueError(f'O tipo de vaga {tipo} não foi reconhecido')
            self.tipo = tipo
            self.placa = None
#-------------------------------------
    def ocupar(self, placa):
        self.placa = placa
        if self.livre is False:
            raise ValueError(f'A vaga {self.id} já está ocupada')
        self.livre = False

    def desocupar(self):
        if self.livre is True:
            raise ValueError(f'A vaga {self.id} já está livre')
        self.placa = None
        self.livre = True
#----------------------------------------

class Estacionamento:
    def __init__(self, total_vagas_livres_carro, total_vagas_livre_moto_):
        self.carro_para_vaga = {}
        self.moto_para_vaga = {}
        self.total_vagas_livres_carro = total_vagas_livres_carro
        self.total_vagas_livres_moto = total_vagas_livre_moto_
        self.inicializar_vagas()
    
        def inicializar_vagas(self):
            self.vagas_carro = {} # id da vaga para objeto de vaga de carro
            self.vagas_moto = {} # id da vaga para objeto de vaga de moto

            tipo = 'carro'
            for i in range(self.total_vagas_livres_carro): # do zero até quatro
                self.vagas_carro[i] = Vaga(i, tipo)
            
            primeiro_id_motos = self.total_vagas_livres_carro
            ultimo_id_motos = primeiro_id_motos + self.total_vagas_livres_moto

            tipo = 'moto'
            for j in range(primeiro_id_motos, ultimo_id_motos):
                self.vagas_motos[j] = Vaga(i, tipo)

                #qqqqqqqqqqqq