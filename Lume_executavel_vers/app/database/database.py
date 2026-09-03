import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "data", "lume.db")


def conectar():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conexao = sqlite3.connect(DB_PATH)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def inicializar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        bio TEXT DEFAULT '',
        foto_perfil TEXT DEFAULT '',
        data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    )
    """)

    categorias = [
        ("Arte",), ("Poesia",), ("Fotografia",),
        ("Música",), ("Desenho",), ("Vídeo",)
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO categorias (nome) VALUES (?)",
        categorias
    )

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publicacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        categoria_id INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        descricao TEXT,
        arquivo TEXT,
        data_publicacao DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS curtidas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        publicacao_id INTEGER NOT NULL,
        UNIQUE(usuario_id, publicacao_id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comentarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        publicacao_id INTEGER NOT NULL,
        texto TEXT NOT NULL,
        data_comentario DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS seguidores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seguidor_id INTEGER NOT NULL,
        seguido_id INTEGER NOT NULL,
        UNIQUE(seguidor_id, seguido_id),
        CHECK(seguidor_id != seguido_id),
        FOREIGN KEY (seguidor_id) REFERENCES usuarios(id),
        FOREIGN KEY (seguido_id) REFERENCES usuarios(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS amizades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        amigo_id INTEGER NOT NULL,
        UNIQUE(usuario_id, amigo_id),
        CHECK(usuario_id != amigo_id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (amigo_id) REFERENCES usuarios(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publicacao_tags (
        publicacao_id INTEGER NOT NULL,
        tag_id INTEGER NOT NULL,
        PRIMARY KEY (publicacao_id, tag_id),
        FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id),
        FOREIGN KEY (tag_id) REFERENCES tags(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS favoritos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        publicacao_id INTEGER NOT NULL,
        UNIQUE(usuario_id, publicacao_id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        descricao TEXT,
        capa TEXT,
        data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projeto_publicacoes (
        projeto_id INTEGER NOT NULL,
        publicacao_id INTEGER NOT NULL,
        PRIMARY KEY (projeto_id, publicacao_id),
        FOREIGN KEY (projeto_id) REFERENCES projetos(id),
        FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id)
    )
    """)

    conexao.commit()
    conexao.close()
