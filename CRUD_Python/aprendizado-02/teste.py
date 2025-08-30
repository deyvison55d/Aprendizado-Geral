import mysql.connector
from mysql.connector import *
from crud_principal import Crud

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Cr@sh12345',
        database = 'bancoteste')
    
    if conexao.is_connected:
        print('Conectado com sucesso!')
        cursor = conexao.cursor()

#----------------------------------------------------
# COMANDOS ABAIXO

        crud = Crud(conexao = conexao, cursor = cursor)
        crud.atualizar(2)




# COMANDOS ACIMA
#----------------------------------------------------
except Error as e:
    print(f'Erro ao conectar: {e}')
finally:
    print('Conexão encerrada')
    cursor.close()
    conexao.close()
