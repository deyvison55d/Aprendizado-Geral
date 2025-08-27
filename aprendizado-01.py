class Cliente():
    listaplanos = ['basic','premium']
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        if plano in self.listaplanos:
            self.plano = plano
        else:
            raise Exception('Plano inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.listaplanos:
            self.plano = novo_plano
        else:
            print('Plano inválido')
    
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Faça upgrade para premium para ver esse filme')


cliente = Cliente('Lira', 'lira@gmail.com', 'basic')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')
cliente.mudar_plano('premium')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')


