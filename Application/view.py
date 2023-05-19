# Importando sqlite 3
import sqlite3 as lite   # Parte do Back-End

# Criando conexão
con = lite.connect('dados.db')

# CRUD

# Inserir dados
def inserir_form(i):
    with con:
        cur= con.cursor()
        query= "INSERT INTO inventario (nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


# Ver dados
def ver_form():
    ver_dados = []
    with con:
        cur= con.cursor()
        query= "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()   # Pega tudo do select
        for row in rows:
            ver_dados.append(row)

    return ver_dados


# Atualizando dados
def atualizar_form(i):
    with con:
        cur= con.cursor()
        query= "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


# Deletando dados
def deletar_form(i):
    # o execute não aceita int, ai tenho que converter em string.
    with con:
        cur= con.cursor()
        query= "DELETE FROM inventario WHERE id=?"
        cur.execute(query, i)


# Ver dados individualmente
def ver_item(id):
    with con:
        ver_dados_individual = []
        cur= con.cursor()
        query= "SELECT * FROM inventario WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()   # Pega tudo do select
        for row in rows:
            ver_dados_individual.append(row)

    return ver_dados_individual