class Crud:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor
    
    def criar(self, nome, idade, email):
        """
        Cria um novo registro de pessoa na tabela 'pessoas'.
    
        Parâmetros:
            nome (str): Nome da pessoa. Apenas letras e espaços.
            idade (int ou str): Idade da pessoa. Deve ser maior que 0.
            email (str): Email válido contendo '@' e domínio.
    
        Não retorna nada. Insere os dados no banco e faz commit.
        """
        while True:
            if not nome.replace(' ', '').isalpha():
                print('\033[31mNome inválido, digite só letras\031[m') 
                nome = input('Digite o nome novamente: ').strip()
                continue
            try:
                idade = int(idade)                                         
                if idade <= 0:
                    raise ValueError                                                                                                        
            except:                                                     
                print('\033[31mIdade inválida\031[m')                                       
                idade = input('Digite a idade novamente: ')
                continue
            if "@" not in email or "." not in email.split("@")[-1]:
                print('\033[31mEmail inválido\031[m')
                email = input('Digite o email novamente: ').strip()
                continue

            break

        self.cursor.execute('INSERT INTO pessoas (nome, idade, email) VALUES (%s, %s, %s)',(nome, idade, email))
        self.conexao.commit()
#---------------------------------------------------------------------------------------------------------------------

    def ler(self):
        self.cursor.execute('SELECT * FROM pessoas')
        dados = self.cursor.fetchall()
        for linha in dados:
            print(f'ID: {linha[0]}, Nome: {linha[1]}, Idade: {linha[2]}, Email: {linha[3]}')
#---------------------------------------------------------------------------------------------------------------------
    
    def atualizar(self, id):
        while True:
            try:
                id = int(id)
                if id <= 0:
                    raise ValueError
            except:
                print('\033[31mID inválida\033[m')
                id = input('Digite novamente: ').strip()
                continue
            self.cursor.execute("SELECT id FROM pessoas WHERE id = %s",(id,))
            resultado = self.cursor.fetchone()
            if resultado is None:
                print('\033[31mID não encontrado\033[m')
                id = input('Digite novamente: ').strip()
                continue
            break

        while True:
            print("""
\033[32m----------------------------------------------------------
O que deseja atualizar?
1 - NOME
2 - IDADE
3 - EMAIL
----------------------------------------------------------\033[m
                """)
            escolha = input('Escolha uma opção: ').strip()

            if escolha == '1': # Valida Nome e Atualiza
                while True:
                    novo_nome = input('Digite o novo nome: ').strip()
                    if not novo_nome.replace(' ', '').isalpha():
                        print('\033[31mNome inválido, digite só letras\033[m')
                        continue
                    break
                self.cursor.execute('UPDATE pessoas SET nome = %s WHERE id = %s',(novo_nome, id))
                self.conexao.commit()
            
            elif escolha == '2': # Valida Idade e Atualiza
                while True:
                    nova_idade = input('Digite a nova idade: ').strip()
                    try:
                        nova_idade = int(nova_idade)
                        if nova_idade <= 0:
                            raise ValueError
                    except:
                        print('\033[31mIdade inválida\033[m')
                        continue
                    break
                self.cursor.execute('UPDATE pessoas SET idade = %s WHERE id = %s',(nova_idade, id))
                self.conexao.commit()
            
            elif escolha == '3': #Valida Email e Atualiza
                while True:
                    novo_email = input('Digite o novo email: ').strip()
                    if "@" not in novo_email or "." not in novo_email.split("@")[-1]:
                        print('\033[31mEmail inválido\033[m')
                        continue
                    break
                self.cursor.execute('' \
                'UPDATE pessoas SET email = %s WHERE id = %s',(novo_email, id))
                self.conexao.commit()

            else:
                print('\033[31mOpção inválida\033[m')

            continuar = input('Deseja atualizar outro campo? [S/N]: ').strip().upper()[0]
            if continuar != 'S': #Para caso usúario queira atualizar mais campos
                break
#---------------------------------------------------------------------------------------------------------------------

    def deletar(self, id): #Valida ID e deleta linha do ID
        while True:
            try:
                id = int(id)
                if id <= 0:
                    raise ValueError
            except:
                print('\033[31mID inválida\033[m')
                id = input('Digite novamente: ').strip()
                continue
            self.cursor.execute("SELECT id FROM pessoas WHERE id = %s", (id,))
            resultado = self.cursor.fetchone()
            if resultado is None:
                print('\033[31mID não encontrado\033[m')
                id = input('Digite novamente: ').strip()
                continue
            break
        self.cursor.execute("DELETE FROM pessoas WHERE id = %s", (id,))
        self.conexao.commit()