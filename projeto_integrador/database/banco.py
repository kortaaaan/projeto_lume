import sqlite3

CAMINHO_BANCO = "database/lume.db"


def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao