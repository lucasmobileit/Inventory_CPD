# Importando sqlite 3
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# criando tabela
with con:
    cur=con.cursor()   # criando cursor
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE,valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")
