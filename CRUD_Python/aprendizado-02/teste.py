import mysql.connector
from mysql.connector import *
from crud_principal import Crud

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'senh@12345',
        database = 'bancoteste')
    
    if conexao.is_connected():
        print('Conectado com sucesso!')
        cursor = conexao.cursor()

#----------------------------------------------------
# COMANDOS ABAIXO
        crud = Crud(conexao = conexao, cursor = cursor)    
        crud.deletar(1)


# COMANDOS ACIMA
#----------------------------------------------------
except Error as e:
    print(f'Erro ao conectar: {e}')
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexao' in locals() and conexao:
        conexao.close()
    print('Conexão encerrada')
