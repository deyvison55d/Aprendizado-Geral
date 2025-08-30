import mysql.connector
from mysql.connector import *
try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'Cr@sh12345',
        database = 'bancoteste'
    )
    if conexao.is_connected():
        print('Conectado com sucesso!')
        cursor = conexao.cursor()


        # READ(SELECT)
        # cursor.execute('SELECT * FROM vendas')
        # resultado = cursor.fetchall()
        # print(resultado)


        # CREATE(INSERT)
        # nome_produto = 'Chocolate'
        # valor = 15
        # cursor.execute(f"INSERT INTO vendas (nome_produto, valor) VALUES ('{nome_produto}',{valor})")
        # conexao.commit()


        # UPDATE(UPDATE)
        # cursor.execute('SELECT * FROM vendas')
        # print(cursor.fetchall())
        # cursor.execute('UPDATE vendas SET valor = 7 WHERE nome_produto = "Abobora"')
        # conexao.commit()
        # cursor.execute('SELECT * FROM vendas')
        # print(cursor.fetchall())


        # DELETE(DELETE)   
        # cursor.execute('DELETE FROM vendas WHERE nome_produto = "Abobora"')
        # conexao.commit()


        cursor.close()
#---------------------------------------------------
except Error as e: 
    print('Erro ao conectar:', e)

finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('Conexão encerrada')